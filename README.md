# GifMaker GUI

GifMaker GUI is a Python application for extracting clips from videos and converting them into GIFs. It provides a graphical interface to select start time, duration, FPS, and output width for GIFs. The GIF is generated and automatically opened for preview.

---

## Features

- Cut a portion of any video clip.
- Convert video clips into GIFs with adjustable FPS and width.
- Automatically open the generated GIF.
- Safe to use with symlinks; personal videos are ignored and not uploaded to Git.

---

## Requirements

- **Python 3**
- **Tkinter** (for GUI)
- **FFmpeg** (for video processing)

---

## Optional: Virtual Environment (recommended)

1. Create a virtual environment:

```bash
python3 -m venv venv

    Activate it:

source venv/bin/activate.fish

    Install optional Python packages if needed (for advanced scripts):

pip install ffmpeg-python

    Deactivate when done:

deactivate

Installing Dependencies (Arch/Garuda Linux + Fish)

sudo pacman -S python tk ffmpeg

Verify installation:

python3 -m tkinter  # should open a test GUI window
ffmpeg -version     # should show version info

Setup

    Clone the repository:

git clone <repo-url>
cd gifmaker

    Place your videos locally or use symlinks in the examples/ folder.
    Do not commit personal videos. .gitignore already ignores video files and GIF outputs.

    Run the GUI:

python3 gif_maker_gui.py

Usage

    Start Time – beginning of the clip (seconds)

    Duration – length of the clip (seconds)

    FPS – GIF frames per second

    Width – output width in pixels

Click Generate GIF to:

    Extract the video clip.

    Convert it to a GIF.

    Automatically open the GIF.

Notes

    Longer clips, higher FPS, or larger widths increase rendering time.

    For better quality and smaller GIFs, palette optimization can be used (advanced FFmpeg).

    Your personal videos stay local; .gitignore prevents accidental commits.

