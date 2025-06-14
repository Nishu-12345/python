# a = "hello python"
# b = "  samester"

# print(a+ b)
# Example (Hello, World):
import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=50)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=2)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=LEFT)
tk.mainloop()