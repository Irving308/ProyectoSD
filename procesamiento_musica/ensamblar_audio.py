from pydub import AudioSegment
import os

def reensamblar_audio(fragment_dir):
    fragments = sorted([
        f for f in os.listdir(fragment_dir)
        if f.endswith(".mp3")
    ], key=lambda x: int(x.split("_")[1].split(".")[0]))

    if not fragments:
        return False

    combined = AudioSegment.empty()
    for frag in fragments:
        audio = AudioSegment.from_file(os.path.join(fragment_dir, frag))
        combined += audio

    output_path = os.path.join("static", "audio_final_completo.mp3")
    combined.export(output_path, format="mp3")
    return True
