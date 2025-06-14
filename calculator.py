import tkinter as tk

def calculate(operator):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result_label.config(text="Error: Divide by 0")
                return
        
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create window
window = tk.Tk()
window.title("Cute Full Calculator 💗")

# Input fields
entry1 = tk.Entry(window)
entry1.pack(pady=5)

entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Buttons for each operation
btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="+", width=5, command=lambda: calculate('+')).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="-", width=5, command=lambda: calculate('-')).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="*", width=5, command=lambda: calculate('*')).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="/", width=5, command=lambda: calculate('/')).grid(row=0, column=3, padx=5)

# Result display
result_label = tk.Label(window, text="Result will show here 😊", font=("Arial", 20))
result_label.pack(pady=10)

# Start GUI
window.mainloop()
