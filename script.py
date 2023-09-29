"""
A program that simply cleans up a messy folder by doing the 
equivalent of shoving all the dirty clothes underneath the bed.
"""

import tkinter as tk
from tkinter import filedialog
import shutil as sh
import os

root = tk.Tk()
root.withdraw()

folder_path = filedialog.askdirectory()
new_directory = "Junk"
path = os.path.join(f'{folder_path}', new_directory)

print("\n" + "-"*20 + " Start of program " + "-"*20 + "\n")
print("Creating Junk-folder...")

try:
    os.mkdir(path)
    print(f"{new_directory}-folder has successfully been created.")
except FileExistsError:
    print(f"{new_directory} directory already exist.")
except Exception as e:
    print(f"An error occurred: {e}")


file_to_process = f'{folder_path}'

junk_folder = f"{folder_path}/Junk"

print("\nList all files in directory:\n")

files_obj = os.scandir(f'{folder_path}')

list_of_files = []

with files_obj as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
            list_of_files.append(entry)

list_length = len(list_of_files)
i = 0

while i < list_length:
    files_obj = os.scandir(f'{folder_path}')

    list_of_files = []

    with files_obj as entries:
        for entry in entries:
            if entry.is_file():
                list_of_files.append(entry)

    file_from_list = str(list_of_files[0])
    pos_start = file_from_list.find("'") + 1
    file_from_list = file_from_list[pos_start:]
    pos_end = file_from_list.find("'")
    file_from_list = file_from_list[0:pos_end]
    custom_file_to_process = f"{folder_path}/{file_from_list}"

    print(f"\nFILE: {file_from_list.upper()}")

    try:
        sh.copy2(custom_file_to_process, junk_folder)
        print(f"{custom_file_to_process} successfully copied to Junk-folder.")
    except FileNotFoundError:
        print(f"{custom_file_to_process} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        os.remove(custom_file_to_process)
        print(f"{custom_file_to_process} has been successfully deleted.")
    except FileNotFoundError:
        print(f"{custom_file_to_process} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    i += 1

print("\n" + "-"*20 + " End of program " + "-"*20 + "\n")
