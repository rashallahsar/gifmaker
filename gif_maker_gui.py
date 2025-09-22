import os
import subprocess
import platform
import tkinter as tk
from tkinter import filedialog, messagebox

# ================= CONFIG =================
# Your video path (symlinked in examples)
DEFAULT_VIDEO_PATH = os.path.expanduser('~/projects/gifmaker/examples/Gifmakervideo/myvideo.mkv')
OUTPUT_CLIP_PATH = os.path.expanduser('~/projects/gifmaker/examples/clip.mkv')
OUTPUT_GIF_PATH = os.path.expanduser('~/projects/gifmaker/examples/clip.gif')
# ==========================================

def open_file(path):
    """Open file in default system viewer."""
    system = platform.system()
    try:
        if system == "Darwin":       # macOS
            subprocess.run(["open", path])
        elif system == "Windows":
            os.startfile(path)
        else:                         # Linux
            subprocess.run(["xdg-open", path])
    except Exception as e:
        messagebox.showerror("Error", f"Could not open file: {e}")

def generate_gif():
    start_time = start_slider.get()
    duration = duration_slider.get()
    fps = fps_slider.get()
    scale = width_slider.get()

    # Step 1: Create clip
    cmd_clip = [
        "ffmpeg",
        "-ss", str(start_time),
        "-i", DEFAULT_VIDEO_PATH,
        "-t", str(duration),
        "-c", "copy",  # use re-encoding for frame-accurate cutting if needed
        OUTPUT_CLIP_PATH
    ]
    subprocess.run(cmd_clip)

    # Step 2: Convert to GIF
    cmd_gif = [
        "ffmpeg",
        "-i", OUTPUT_CLIP_PATH,
        "-vf", f"fps={fps},scale={scale}:-1:flags=lanczos",
        OUTPUT_GIF_PATH
    ]
    subprocess.run(cmd_gif)
    messagebox.showinfo("Done", f"GIF created at:\n{OUTPUT_GIF_PATH}")

    # Step 3: Open GIF
    open_file(OUTPUT_GIF_PATH)

# ================= GUI ====================
root = tk.Tk()
root.title("GIF Maker Prototype")

# Start time slider (seconds)
tk.Label(root, text="Start Time (seconds)").pack()
start_slider = tk.Scale(root, from_=0, to=600, orient=tk.HORIZONTAL)  # adjust max to video length
start_slider.set(45)  # default to 45s
start_slider.pack()

# Duration slider (seconds)
tk.Label(root, text="Duration (seconds)").pack()
duration_slider = tk.Scale(root, from_=1, to=60, orient=tk.HORIZONTAL)
duration_slider.set(30)  # default 30s
duration_slider.pack()

# FPS slider
tk.Label(root, text="GIF FPS").pack()
fps_slider = tk.Scale(root, from_=5, to=30, orient=tk.HORIZONTAL)
fps_slider.set(15)
fps_slider.pack()

# Width slider
tk.Label(root, text="GIF Width (px)").pack()
width_slider = tk.Scale(root, from_=100, to=1280, orient=tk.HORIZONTAL)
width_slider.set(320)  # default width
width_slider.pack()

# Generate button
tk.Button(root, text="Generate GIF", command=generate_gif).pack(pady=10)

root.mainloop()
