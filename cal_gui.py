import tkinter as t

def cal():
    try:
        result = eval(entry.get())
        label.config(text="Result:" + str(result))
    except:
        label.config(text="Invalid input")

window = t.Tk()
window.title("Calculator")
window.geometry("300x200")

entry = t.Entry(window)
entry.pack()
button = t.Button(window, text="Calculate", command=cal)
button.pack()

label = t.Label(window, text="Please enter an experession:")
label.pack()

window.mainloop()