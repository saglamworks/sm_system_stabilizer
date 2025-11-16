# SM System Stabilizer

**Version:** 1.0.0  
**Type:** CLI-based System Optimizer  

SM System Stabilizer is a fast, command-line tool designed to monitor, clean, and optimize Windows system performance. It helps users keep their systems stable, remove unnecessary files, and manage running processes efficiently. It features system monitoring (CPU, RAM, Disk usage), cleaning of temporary files, killing unnecessary tasks via a customizable kill_list.txt, and generating performance reports. The tool is entirely CLI-based and requires no GUI.

Installation: Make sure you have Python 3.x installed and added to your system PATH. Clone the repository using `git clone https://github.com/saglamworks/sm_system_stabilizer.git`, navigate into the folder with `cd sm_system_stabilizer`, and optionally install dependencies with `pip install psutil`.

Usage: On Windows, double-click `run_stabilizer.bat` to launch the CLI interface. Or run directly with Python using `python sm_stabilizer.py`. Follow the prompts to monitor system performance, clean temporary files, optionally kill unnecessary tasks, and generate a performance report. The tool will display system status and execute actions with confirmation prompts.

Folder structure: sm_system_stabilizer/ contains sm_stabilizer.py (main Python script), utils.py (helper functions), run_stabilizer.bat (Windows batch launcher), kill_list.txt (list of processes to kill, user editable), README.md (this file), LICENSE (MIT license or your choice), and .gitignore (to ignore unnecessary files).

License: This project is licensed under the MIT License. See LICENSE for details.
