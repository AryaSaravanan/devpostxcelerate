
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\scien\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1150x55")
window.configure(bg = "#EBFF9E")


canvas1 = Canvas(
    window,
    bg = "#EBFF9E",
    height = 55,
    width = 1150,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas1.place(x = 0, y = 0)
canvas1.create_text(
    292.0,
    0.0,
    anchor="nw",
    text="PIL App",
    fill="#000000",
    font=("Inter SemiBold", 48 * -1)
)
window.resizable(False, False)
window.mainloop()