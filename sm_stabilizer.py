# sm_stabilizer.py
"""
SM System Stabilizer - CLI
A simple tool to monitor system usage, clean temp files, and manage processes.
"""

import os
import sys
import platform
from utils import check_system_status, clean_temp_files, kill_processes, generate_report

def main():
    while True:
        print("\n=== SM System Stabilizer ===")
        print("1. Check system status")
        print("2. Clean temp files")
        print("3. Kill unnecessary processes")
        print("4. Generate system report")
        print("5. Exit")
        
        choice = input("\nSelect an option: ").strip()
        
        if choice == "1":
            check_system_status()
        elif choice == "2":
            clean_temp_files()
        elif choice == "3":
            kill_processes()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            print("Exiting SM System Stabilizer.")
            break
        else:
            print("Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    # Ensure script is running on supported OS
    if platform.system() not in ["Windows", "Linux"]:
        print("Unsupported OS. Only Windows and Linux are supported.")
        sys.exit(1)
    main()
