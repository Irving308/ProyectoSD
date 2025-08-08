from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from procesamiento_musica.split_audio import split_audio
from procesamiento_musica.ensamblar_audio import reensamblar_audio

app = FastAPI()

STATIC_DIR = "static"
FRAGMENT_DIR = os.path.join(STATIC_DIR, "fragmentos")
FINAL_AUDIO_PATH = os.path.join(STATIC_DIR, "audio_final_completo.mp3")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    input_path = os.path.join(STATIC_DIR, file.filename)
    with open(input_path, "wb") as f:
        f.write(await file.read())

    try:
        split_audio(input_path, FRAGMENT_DIR, num_fragments=10)
        return {"message": "Audio dividido exitosamente", "filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/fragment/{index}")
def get_fragment(index: int):
    fragment_path = os.path.join(FRAGMENT_DIR, f"fragment_{index}.mp3")
    if not os.path.exists(fragment_path):
        raise HTTPException(status_code=404, detail="Fragmento no encontrado")
    return FileResponse(fragment_path, media_type="audio/mpeg")

@app.get("/ensamblar/")
def ensamblar():
    success = reensamblar_audio(FRAGMENT_DIR)
    if not success or not os.path.exists(FINAL_AUDIO_PATH):
        raise HTTPException(status_code=500, detail="Error al ensamblar el audio")
    return FileResponse(FINAL_AUDIO_PATH, media_type="audio/mpeg")
