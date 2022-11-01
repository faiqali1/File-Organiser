import pathlib
from tkinter import ttk
from tkinter.filedialog import askdirectory
import os

PREFIX_TEXT: str = ""
SUFFIX_TEXT: str = "Files"

def select_folder():
    ext_list = []
    path = askdirectory(title='Select your folder')

    assert os.path.isdir(path), "Invalid path"

    # construct path object
    d = pathlib.Path(path)

    # search through folder to find files
    for file in d.iterdir():
        if file.is_file():
            ext = file.suffix

            ext_list.append(ext)
            print(ext)
            # create new folder for each file type
            new_folder = d / (PREFIX_TEXT + " ." + ext[1:] + " " + SUFFIX_TEXT)
            if not new_folder.is_dir():
                new_folder.mkdir()
            # move files to new folder
            file.replace(new_folder / file.name)
            # text to show transfer complete
    print(f'File Types{set(ext_list)}')
    status = ttk.Label(text=f"Transfer Complete with {len(ext_list)} Files Transferred created")
    status.pack()

def hello_world() -> str:
    return "Hello world"

def return_10() -> int:
    return 10

