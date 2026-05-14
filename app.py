import gradio as gr
import os
import tempfile
from voice_engine import VoiceEngine

# Initialize the engine
engine = VoiceEngine()

# Custom CSS for a premium, glassmorphism look
custom_css = """
body {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #f8fafc;
    font-family: 'Inter', sans-serif;
}
.gradio-container {
    max-width: 900px !important;
    margin: auto;
}
.primary-btn {
    background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%) !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4) !important;
    transition: transform 0.2s, box-shadow 0.2s !important;
}
.primary-btn:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(139, 92, 246, 0.6) !important;
}
.glass-panel {
    background: rgba(30, 41, 59, 0.7) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 16px !important;
    padding: 24px !important;
    margin-bottom: 24px !important;
}
.header-title {
    text-align: center;
    background: -webkit-linear-gradient(45deg, #60a5fa, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}
.header-subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}
"""

def generate_speech(text, reference_audio, language_choice):
    if not text:
        raise gr.Error("Please enter the text you want to generate.")
    if not reference_audio:
        raise gr.Error("Please upload a reference audio file (10-30s).")
        
    lang_map = {"Arabic": "ar", "English": "en"}
    lang_code = lang_map.get(language_choice, "en")
    
    temp_dir = tempfile.gettempdir()
    output_file = os.path.join(temp_dir, f"cloned_{lang_code}_output.wav")
    
    try:
        engine.clone_voice(
            text=text,
            reference_audio_path=reference_audio,
            language=lang_code,
            output_path=output_file
        )
        return output_file
    except Exception as e:
        raise gr.Error(f"Engine Error: {str(e)}")

with gr.Blocks(css=custom_css, theme=gr.themes.Monochrome()) as demo:
    gr.HTML("<h1 class='header-title'>Dialect Adaptor</h1>")
    gr.HTML("<p class='header-subtitle'>Next-Generation Zero-Shot Voice Cloning</p>")
    
    with gr.Column(elem_classes=["glass-panel"]):
        gr.Markdown("### 1. Upload Reference Voice")
        ref_audio = gr.Audio(label="Drop your voice sample here (10-30 seconds)", type="filepath", interactive=True)
        
    with gr.Column(elem_classes=["glass-panel"]):
        gr.Markdown("### 2. Configure Output")
        with gr.Row():
            language = gr.Dropdown(choices=["Arabic", "English"], value="Arabic", label="Target Language", interactive=True)
        input_text = gr.Textbox(label="Script", lines=4, placeholder="Enter the text you want the voice to speak...", interactive=True)
        
    with gr.Column(elem_classes=["glass-panel"]):
        gr.Markdown("### 3. Generate")
        generate_btn = gr.Button("✨ Synthesize Voice", variant="primary", elem_classes=["primary-btn"])
        output_audio = gr.Audio(label="Generated Result", interactive=False)
        
    generate_btn.click(
        fn=generate_speech,
        inputs=[input_text, ref_audio, language],
        outputs=output_audio
    )

if __name__ == "__main__":
    demo.launch(inbrowser=True)
