import subprocess
import sys
import os

def make_gif(input_file, start_time, duration, output_file="output.gif"):
    """
    Create a GIF from a video using ffmpeg.

    input_file: path to video
    start_time: timestamp in seconds or hh:mm:ss
    duration: length of clip in seconds
    output_file: name of GIF file
    """
    cmd = [
        "ffmpeg",
        "-ss", str(start_time),
        "-t", str(duration),
        "-i", input_file,
        "-vf", "fps=10,scale=480:-1:flags=lanczos",  # 10 FPS, width 480px
        "-gifflags", "+transdiff",
        "-y",  # overwrite output
        output_file
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"GIF saved as {output_file}")
    except subprocess.CalledProcessError as e:
        print("Error creating GIF:", e)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python src/gifmaker.py <input_file> <start_time> <duration> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    start_time = sys.argv[2]
    duration = sys.argv[3]
    output_file = sys.argv[4] if len(sys.argv) > 4 else "output.gif"

    make_gif(input_file, start_time, duration, output_file)

