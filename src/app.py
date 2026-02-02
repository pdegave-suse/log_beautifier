from textual.app import App
from textual.widgets import Header, Footer, DataTable, Input, Static
from rich.markup import escape

from src.loadaudit import load_audit_logs
from src.jsonpopup import JsonPopup

class AuditApp(App):
    CSS = """
    DataTable { height: 1fr; }
    Input { margin: 1; border: solid white; }
    #results_count { margin-left: 2; color: $text-muted; }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("c", "clear", "Clear Search"),
        ("tab", "focus_next", "Switch Focus")
    ]

    def __init__(self, log_file_path):
        super().__init__()
        self.log_file_path = log_file_path
        self.all_logs = []
        self.current_logs = []

    def compose(self):
        yield Header()
        yield Input(placeholder="Search logs...", id="search_input")
        yield Static("Found 0 logs", id="results_count")
        yield DataTable(zebra_stripes=True, cursor_type="row")
        yield Footer()

    def on_mount(self):
        # Load the data and show it in the table
        self.all_logs = load_audit_logs(self.log_file_path)
        self.current_logs = self.all_logs

        table = self.query_one(DataTable)
        table.add_columns("TIME", "USER", "CODE", "METHOD", "URI")
        self.update_table(self.all_logs)
        self.query_one("#search_input").focus()

    def update_table(self, logs_to_show):
        self.current_logs = logs_to_show
        table = self.query_one(DataTable)
        table.clear()

        # Update the counter text
        count_label = self.query_one("#results_count")
        count_label.update(f"Logs: {len(logs_to_show)}")

        for index, log in enumerate(logs_to_show):
            user = escape(log.get("user", {}).get("name", "unknown"))
            code = str(log.get("responseCode", ""))
            time = log.get("requestTimestamp", "")[11:19]
            method = log.get("method", "")
            uri = log.get("requestURI", "")

            # Set the color based on the code
            if code.startswith("4") or code.startswith("5"):
                color = "[red]"
            else:
                color = "[green]"

            table.add_row(time, user, f"{color}{code}[/]", method, uri, key=str(index))

    def on_input_changed(self, event):
        search_text = event.value.lower()

        if search_text == "":
            self.update_table(self.all_logs)
            return

        filtered_list = []
        for log in self.all_logs:
            user = log.get("user", {}).get("name", "").lower()
            code = str(log.get("responseCode", ""))
            uri = log.get("requestURI", "").lower()
            method = log.get("method", "").lower()
            time = log.get("requestTimestamp", "").lower()

            if search_text in user:
                filtered_list.append(log)
            elif search_text in code:
                filtered_list.append(log)
            elif search_text in uri:
                filtered_list.append(log)
            elif search_text in method:
                filtered_list.append(log)
            elif search_text in time:
                filtered_list.append(log)

        self.update_table(filtered_list)

    def on_input_submitted(self):
        self.query_one(DataTable).focus()

    def on_data_table_row_selected(self, event):
        row_index = int(event.row_key.value)
        selected_log = self.current_logs[row_index]
        self.push_screen(JsonPopup(selected_log))

    def action_clear(self):
        search_bar = self.query_one("#search_input")
        search_bar.value = ""
        search_bar.focus()
