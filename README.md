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

1. **Run the application:**
   ```bash
   python app.py
   ```
2. The UI will automatically open in your default web browser (usually at `http://localhost:7860`).
3. Upload a clean, short reference audio of the voice you want to clone.
4. Select the target language (Arabic or English).
5. Enter your text and click **Generate**. Note: The first time you run this, it will download the XTTS-v2 model weights automatically.

## Disclaimer
Please use this tool responsibly and ethically. Only clone voices with permission.
