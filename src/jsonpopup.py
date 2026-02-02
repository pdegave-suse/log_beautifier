import json
from textual.widgets import Static, Label
from textual.screen import ModalScreen
from textual.containers import Vertical, VerticalScroll

class JsonPopup(ModalScreen):
    def __init__(self, log_data):
        super().__init__()
        # Store the log data inside screenn
        self.log_data = log_data

    def compose(self):
        with Vertical():
            #  scrollable area for the JSON text
            with VerticalScroll(id="json_scroll_area"):
                # Convert the dictionary to text
                pretty_text = json.dumps(self.log_data, indent=4)
                yield Static(pretty_text, markup=False)


            yield Label(" ← Back (Press ESC)", id="back_hint")

    def on_key(self, event):
        if event.key == "escape":
            self.app.pop_screen()

    DEFAULT_CSS = """
    JsonPopup { background: $background; }
    #json_scroll_area { height: 1fr; padding: 1; }
    #back_hint {
        background: $surface;
        color: $text-muted;
        width: 100%;
        height: 3;
        content-align: center middle;
        border-top: solid $panel;
    }
    """
