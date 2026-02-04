# Rancher & RKE2 Audit Log beautifier/Parser

This is a simple terminal tool (TUI) to make Rancher and RKE2(WIP) audit logs easier to read. Raw audit logs are usually just long lines of JSON that are hard to look through. This tool puts them into a clean table and beautifies the output.

## Features

* **Table View:** It takes the JSON and shows the important data (Time, User, Code, URI) in columns.
* **Color Highlights:** Successful HTTP status code(200) are green and errors (4xx/5xx) are red, so you can spot problems quickly.
* **Search:** You can type a username, a status code, or a URL to filter the list.
* **Details:** If you find a log you want to investigate, press Enter to see the full JSON data formatted.

## How to use it

1. **Clone the project:** `git clone https://github.com/pdegave-suse/log_beautifier.git`
2.  **Give it permission:** Open your terminal in the project folder and run:  
   `cd log_beautifier`  `chmod +x run.sh`
   
4. **Run it:** Just type:  
   `./run.sh`  
   *(This will automatically set up the Python environment and install the two libraries needed: textual and rich.)*

5. **Custom log file:** If you have a specific log file you want to check, run it like this:  
   `./run.sh path/to/your/file.log`

## Controls

* **Tab:** Move between the search bar and the log list.
* **Enter:** View the full details of a log entry.
* **Esc:** Close the detail window.
* **C:** Clear your search and show all logs.
* **Q:** Quit/exit the tool.
