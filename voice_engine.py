import os
import torch
from TTS.api import TTS

class VoiceEngine:
    def __init__(self):
        # Determine if GPU is available
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Initializing TTS on {self.device}...")
        
        # Initialize XTTS-v2. This model supports zero-shot voice cloning
        # and multiple languages including Arabic (ar) and English (en).
        self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)
        print("TTS Engine initialized successfully.")

    def clone_voice(self, text, reference_audio_path, language, output_path):
        """
        Clones the voice from the reference audio to speak the given text.
        text: The text to be spoken
        reference_audio_path: Path to the sample voice file
        language: Language code ('ar' for Arabic, 'en' for English)
        output_path: Path to save the generated wav file
        """
        print(f"Generating audio in {language}...")
        
        # Run the synthesis
        self.tts.tts_to_file(
            text=text,
            speaker_wav=reference_audio_path,
            language=language,
            file_path=output_path
        )
        print(f"Audio generated and saved to {output_path}")
        return output_path
