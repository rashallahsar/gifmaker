# GifMaker GUI

GifMaker GUI is a Python application for extracting clips from videos and converting them into GIFs. It provides a graphical interface to select start time, duration, FPS, and output width for GIFs. The GIF is generated and automatically opened for preview.

---

## Quick Start

1. **Clone the repository:**

```bash
git clone https://github.com/rashallahsar/gifmaker.git
cd gifmaker
````

2. **Install dependencies** (Arch/Garuda Linux + Fish):

```bash
sudo pacman -S python tk ffmpeg
```

3. **Place your videos** in the `examples/` folder, or create symlinks to your local videos.
   *Note: Personal videos are not included in the repo.*

4. **Run the GIF Maker GUI:**

```bash
python3 gif_maker_gui.py
```

5. **Use the GUI:**

* Adjust **Start Time**, **Duration**, **FPS**, and **Width** sliders.
* Click **Generate GIF** to extract the clip, convert it to a GIF, and automatically open it.

---

## Features

* Cut a portion of any video clip
* Convert video clips into GIFs with adjustable FPS and width
* Automatically open the generated GIF
* Safe to use with symlinks; personal videos are ignored and not uploaded to Git

---

## Requirements

* **Python 3**
* **Tkinter** (for GUI)
* **FFmpeg** (for video processing)

---

## Optional: Virtual Environment (Recommended)

1. Create a virtual environment:

```bash
python3 -m venv venv
```

2. Activate it:

```bash
source venv/bin/activate.fish
```

3. Install optional Python packages (for advanced scripts):

```bash
pip install ffmpeg-python
```

4. Deactivate when done:

```bash
deactivate
```

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/rashallahsar/gifmaker.git
cd gifmaker
```

2. Place your videos locally or use symlinks in the `examples/` folder
   **Do not commit personal videos.** `.gitignore` already ignores video files and GIF outputs

3. Run the GUI:

```bash
python3 gif_maker_gui.py
```

---

## Usage

* **Start Time** – beginning of the clip (seconds)
* **Duration** – length of the clip (seconds)
* **FPS** – GIF frames per second
* **Width** – output width in pixels

Click **Generate GIF** to:

1. Extract the video clip
2. Convert it to a GIF
3. Automatically open the GIF

---

## Notes

* Longer clips, higher FPS, or larger widths increase rendering time
* For better quality and smaller GIFs, palette optimization can be used (advanced FFmpeg)
* Your personal videos stay local; `.gitignore` prevents accidental commits

---

## License

This project is released under the **Unlicense**. You can copy, modify, publish, use, compile, sell, or distribute the software, for any purpose, commercial or non-commercial, and by any means.

For more details, see [https://unlicense.org](https://unlicense.org)

```

