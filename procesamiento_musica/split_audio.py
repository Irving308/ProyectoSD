from pydub import AudioSegment
import os

def split_audio(input_path, output_dir, num_fragments=10):
    audio = AudioSegment.from_file(input_path)
    duration = len(audio)
    fragment_length = duration // num_fragments

    os.makedirs(output_dir, exist_ok=True)

    for i in range(num_fragments):
        start = i * fragment_length
        end = start + fragment_length if i < num_fragments - 1 else duration
        fragment = audio[start:end]
        fragment.export(os.path.join(output_dir, f"fragment_{i}.mp3"), format="mp3")
