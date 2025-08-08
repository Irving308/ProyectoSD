import subprocess
import os

def split_audio(input_audio, output_dir, num_fragments=10):
    os.makedirs(output_dir, exist_ok=True)
    
    duration = float(subprocess.check_output(
        f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {input_audio}", 
        shell=True
    ).decode('utf-8').strip())
    
    segment_duration = duration / num_fragments
    for i in range(num_fragments):
        start = i * segment_duration
        end = (i + 1) * segment_duration
        output_file = os.path.join(output_dir, f"fragment_{i}.mp3")
    
        subprocess.run(
            f"ffmpeg -y -ss {start} -to {end} -i {input_audio} -c copy {output_file}",
            shell=True, check=True
        )
    print(f"Audio dividido en {num_fragments} fragmentos en {output_dir}")

if __name__ == "__main__":
    input_audio = "input.mp3"  # Cambia a tu archivo de audio
    split_audio(input_audio, "music_fragments")