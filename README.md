# Dialect Adaptor

A professional local Python tool for zero-shot voice cloning and text-to-speech generation using Coqui XTTS-v2. It fully supports **Arabic** and **English**.

## Features
- **Zero-Shot Voice Cloning:** Clone a voice using only a short 10-30 second audio sample.
- **Multilingual Support:** Generate perfectly natural speech in Arabic or English.
- **Modern Web Interface:** Easy-to-use Gradio web UI.

## Installation

### Prerequisites
- Python 3.9 - 3.12
- Highly Recommended: An NVIDIA GPU for fast audio generation.

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/musaabhasan/Dialect-Adaptor.git
   cd Dialect-Adaptor
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

You have two beautiful ways to use the Dialect Adaptor:

### 1. Premium Web Interface (Browser)
Run the following command to launch the Gradio web application:
```bash
python app.py
```
The UI will automatically open in your default web browser (usually at `http://localhost:7860`).

### 2. Premium Terminal Interface (TUI)
If you prefer staying in the terminal but still want a highly polished interface, run:
```bash
python tui.py
```
This launches an interactive, mouse-supported Terminal UI using Textual. You can upload files, select languages, and view real-time logs directly in your console.

## General Steps
1. Upload or specify a clean, short reference audio of the voice you want to clone (10-30s `.wav` file).
2. Select the target language (Arabic or English).
3. Enter your script text and hit **Generate**.

> Note: The first time you run generation, it will download the XTTS-v2 model weights automatically.

## Disclaimer
Please use this tool responsibly and ethically. Only clone voices with permission.
