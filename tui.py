from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Header, Footer, Input, Label, Button, Select, Log, TextArea
from voice_engine import VoiceEngine
import os
import threading
import tempfile

class VoiceClonerTUI(App):
    """A Textual app to manage voice cloning."""

    CSS = """
    Screen {
        background: $surface-darken-1;
    }
    
    #main-container {
        layout: vertical;
        padding: 1 2;
        width: 100%;
        height: 100%;
    }

    .form-group {
        margin-bottom: 1;
        height: auto;
    }

    #path-input {
        width: 100%;
    }

    #text-input {
        height: 8;
        width: 100%;
    }

    #generate-btn {
        width: 100%;
        background: $success;
        color: $text;
        text-style: bold;
        margin-top: 1;
        margin-bottom: 1;
    }

    #log-view {
        height: 1fr;
        border: solid $primary;
        background: $panel;
    }
    
    Label {
        padding-bottom: 1;
        color: $text-muted;
    }
    """

    BINDINGS = [("q", "quit", "Quit"), ("ctrl+g", "generate", "Generate")]

    def __init__(self):
        super().__init__()
        self.engine = None
        self.temp_dir = tempfile.gettempdir()

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(show_clock=True)
        
        with Container(id="main-container"):
            with Vertical(classes="form-group"):
                yield Label("Reference Audio Path (.wav):")
                yield Input(placeholder="/path/to/voice.wav", id="path-input")
            
            with Vertical(classes="form-group"):
                yield Label("Target Language:")
                yield Select(
                    (("Arabic", "ar"), ("English", "en")),
                    value="ar",
                    id="lang-select"
                )
            
            with Vertical(classes="form-group"):
                yield Label("Text to speak:")
                yield TextArea(id="text-input")
            
            yield Button("Synthesize Audio (Ctrl+G)", id="generate-btn")
            
            yield Label("System Logs:")
            yield Log(id="log-view")
            
        yield Footer()

    def on_mount(self) -> None:
        self.log_view = self.query_one("#log-view", Log)
        self.log_view.write_line("[*] Welcome to Dialect Adaptor TUI.")
        self.log_view.write_line("[*] Loading Voice Engine in background...")
        # Load engine in a thread so UI doesn't freeze
        threading.Thread(target=self.load_engine).start()

    def load_engine(self):
        try:
            self.engine = VoiceEngine()
            self.call_from_thread(self.log_view.write_line, "[+] Voice Engine successfully initialized!")
        except Exception as e:
            self.call_from_thread(self.log_view.write_line, f"[-] Error loading engine: {str(e)}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "generate-btn":
            self.action_generate()

    def action_generate(self) -> None:
        if not self.engine:
            self.log_view.write_line("[-] Engine is not loaded yet. Please wait.")
            return
            
        ref_path = self.query_one("#path-input", Input).value.strip()
        text = self.query_one("#text-input", TextArea).text.strip()
        lang = self.query_one("#lang-select", Select).value

        if not os.path.exists(ref_path):
            self.log_view.write_line(f"[-] Error: Reference file not found at '{ref_path}'")
            return
            
        if not text:
            self.log_view.write_line("[-] Error: Text cannot be empty.")
            return

        self.log_view.write_line(f"[*] Starting synthesis for language: {lang}...")
        self.log_view.write_line(f"[*] Text: {text[:30]}...")
        
        # Run generation in a thread
        threading.Thread(target=self.generate_audio, args=(text, ref_path, lang)).start()

    def generate_audio(self, text, ref_path, lang):
        output_file = os.path.join(self.temp_dir, f"tui_cloned_{lang}.wav")
        try:
            self.engine.clone_voice(
                text=text,
                reference_audio_path=ref_path,
                language=lang,
                output_path=output_file
            )
            self.call_from_thread(self.log_view.write_line, f"[+] Success! Audio saved to: {output_file}")
        except Exception as e:
            self.call_from_thread(self.log_view.write_line, f"[-] Generation failed: {str(e)}")

if __name__ == "__main__":
    app = VoiceClonerTUI()
    app.run()
