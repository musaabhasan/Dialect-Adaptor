import gradio as gr
import os
import tempfile
from voice_engine import VoiceEngine

# Initialize the engine
engine = VoiceEngine()

def generate_speech(text, reference_audio, language_choice):
    if not text:
        raise gr.Error("Please enter some text.")
    if not reference_audio:
        raise gr.Error("Please provide a reference audio file.")
        
    # Map the dropdown choice to the language code
    lang_map = {
        "Arabic": "ar",
        "English": "en"
    }
    lang_code = lang_map.get(language_choice, "en")
    
    # Create a temporary file to save the output
    temp_dir = tempfile.gettempdir()
    output_file = os.path.join(temp_dir, "cloned_output.wav")
    
    try:
        engine.clone_voice(
            text=text,
            reference_audio_path=reference_audio,
            language=lang_code,
            output_path=output_file
        )
        return output_file
    except Exception as e:
        raise gr.Error(f"Error generating audio: {str(e)}")

# Define the Gradio interface
with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue", neutral_hue="slate")) as demo:
    gr.Markdown(
        """
        # 🎙️ Dialect Adaptor - Zero-Shot Voice Cloning
        Upload a sample of a voice (10-30 seconds of clear speech), enter your text, and generate high-quality cloned speech in **Arabic** or **English**.
        """
    )
    
    with gr.Row():
        with gr.Column(scale=1):
            ref_audio = gr.Audio(label="Reference Audio (Voice to Clone)", type="filepath")
            language = gr.Dropdown(choices=["Arabic", "English"], value="Arabic", label="Target Language")
        
        with gr.Column(scale=1):
            input_text = gr.Textbox(label="Text to Speak", lines=5, placeholder="Enter text in Arabic or English here...")
            generate_btn = gr.Button("Generate Cloned Speech", variant="primary")
            
    with gr.Row():
        output_audio = gr.Audio(label="Generated Audio", interactive=False)
        
    generate_btn.click(
        fn=generate_speech,
        inputs=[input_text, ref_audio, language],
        outputs=output_audio
    )

if __name__ == "__main__":
    demo.launch(inbrowser=True)
