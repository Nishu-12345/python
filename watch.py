import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)  # update every 1000ms (1 second)

# Set up the window
root = tk.Tk()
root.title('Digital Watch')

# Configure the label
label = tk.Label(root, font=('calibri', 60, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

# Start the clock
time()

# Run the app
root.mainloop()
