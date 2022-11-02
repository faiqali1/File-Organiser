from tkinter import Tk, ttk
from src.file_organiser.utils import select_folder


label = ""
root = Tk()
root.title('select your folder')
root.resizable(True, True)
root.geometry('400x200')
open_button = ttk.Button(root, text='Select Folder', command=select_folder)
open_button.pack(expand=True)
multiple_label = ttk.Label(root, text=label)
root.mainloop()
