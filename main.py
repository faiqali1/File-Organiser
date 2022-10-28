import pathlib
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import os

label = ""

ext_list = []

# Tasks:
# search through folder to find files
# identify file types
# create new folder for each file type
# move files to new folder

pre_text: str = ""
post_text: str = "Files"


def select_folder():
    path = askdirectory(title='Select your folder')

    assert os.path.isdir(path), "Invalid path"
    os.chdir(path)

    # construct path object
    d = pathlib.Path(path)

    # search through folder to find files
    for file in d.iterdir():
        if file.is_file():
            ext = file.suffix

            ext_list.append(ext)
            print(ext)
            # create new folder for each file type
            new_folder = d / (pre_text + " " + ext[1:].upper() + " " + post_text)
            if not new_folder.is_dir():
                new_folder.mkdir()
            # move files to new folder
            file.replace(new_folder / file.name)
            # text to show transfer complete
    print(f'File Types{set(ext_list)}')
    status = ttk.Label(text=f"Transfer Complete with {len(ext_list)} Files Transferred created")
    status.pack()


root = Tk()
root.title('select your folder')
root.resizable(True, True)
root.geometry('400x200')
open_button = ttk.Button(root, text='Select Folder', command=select_folder)
open_button.pack(expand=True)
multiple_label = ttk.Label(root, text=label)
root.mainloop()
