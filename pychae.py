import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My first GUI")
root.geometry("500x200")
label = tk.Label(root, text="Hello world")
label.pack()
def say_hello():
    print("Hello!")
button = tk.Button(root, text="Click me", command=say_hello)
button.pack()

entry = tk.Entry(root)
entry.pack()

def get_input():
    user_input = entry.get()
    print("You typed:", user_input)
inputButton = tk.Button(root, text="Submit", command=get_input)
inputButton.pack()

# Checkbox
ismarried = tk.IntVar()
checkButton = tk.Checkbutton(root, text="Are you married?", variable=ismarried)
checkButton.pack()

# Radio Buttons
gender = tk.StringVar()
# root = tk.Tk()
radio1 = tk.Radiobutton(root, text="Male", variable=gender, value="male")
radio2 = tk.Radiobutton(root, text="Female", variable=gender, value="female")
# radio1.pack(side="right")
# radio2.pack(side="left")
# radio1.place(x=50, y=50)
# radio2.place(x=100, y=50)
# radio1.grid(row=0, column=0)

# messagebox.showinfo("Message", "This is a message")
# messagebox.showinfo("Warning", "This is a warning")
# messagebox.showerror("Error", "This is a error")

# styled text
label1 = tk.Label(root, text="Hello GUI", fg="red", bg="black",
                  font=("Arial", 32, "bold"))
label1.pack()

root.mainloop()