from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
from tkinter import ttk



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\scien\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("PIL App")


window.geometry("911x700")
window.configure(bg = "#FFFFFF")

mainframe = ttk.Frame(window)
mainframe.pack(fill='both', expand=1)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 2366,
    width = 911,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

scrollbar = ttk.Scrollbar(mainframe, orient="vertical", command=canvas.yview)
scrollableFrame = ttk.Frame(canvas)

scrollableFrame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

scrollwindow = canvas.create_window((0, 0), window=scrollableFrame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)




canvas.create_text(
    32.0,
    0.0,
    anchor="nw",
    text="What’s your name?",
    fill="#000000",
    font=("Inter", 36 * -1)
)



canvas.create_text(
    17.0,
    177.0,
    anchor="nw",
    text="What is your job description?",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    32.0,
    354.0,
    anchor="nw",
    text="Type in your full address here",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    33.0,
    708.0,
    anchor="nw",
    text="What is the crime that was committed?",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    32.0,
    885.0,
    anchor="nw",
    text="To which High Court are you filing this PIL?",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    32.0,
    1258.0,
    anchor="nw",
    text="How did you find about this crime?",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    33.0,
    1435.0,
    anchor="nw",
    text="What is the damage caused by the crime?",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    33.0,
    1821.0,
    anchor="nw",
    text="Have any representations been made on this topic before? ",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    32.0,
    1612.0,
    anchor="nw",
    text="How did you find out about this crime? What is the source of information? e.g. direct observation",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    32.0,
    1062.0,
    anchor="nw",
    text="Write brief facts about the matter on which this PIL is being filed",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    33.0,
    531.0,
    anchor="nw",
    text="Who/What business are you filing this PIL against?",
    fill="#000000",
    font=("Inter", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    455.0,
    113.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=42.0,
    y=81.0,
    width=826.0,
    height=55.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    456.0,
    290.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=43.0,
    y=258.0,
    width=826.0,
    height=62.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    456.0,
    467.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=43.0,
    y=435.0,
    width=826.0,
    height=62.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    455.0,
    644.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=42.0,
    y=612.0,
    width=826.0,
    height=62.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    456.0,
    821.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=43.0,
    y=789.0,
    width=826.0,
    height=62.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    455.0,
    998.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=42.0,
    y=966.0,
    width=826.0,
    height=62.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    455.0,
    1194.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=42.0,
    y=1162.0,
    width=826.0,
    height=62.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    456.0,
    1371.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=43.0,
    y=1339.0,
    width=826.0,
    height=62.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    455.0,
    1548.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=42.0,
    y=1516.0,
    width=826.0,
    height=62.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    455.0,
    1757.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=42.0,
    y=1725.0,
    width=826.0,
    height=62.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    455.0,
    1966.0,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=42.0,
    y=1934.0,
    width=826.0,
    height=62.0
)

mainframe.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


window.resizable(False, False)
window.mainloop()
