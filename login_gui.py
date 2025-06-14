import tkinter as tk

def login():
    usr = username_entry.get()
    pwd = password_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    dob = dob_entry.get()
    print(f"Username:{usr}, Password:{pwd}, name:{name},email:{email}, dob:{dob}")

window = tk.Tk()
window.title("Login from")
window.geometry("500x300")

#  username
username_lable = tk.Label(window, text="username:")
username_lable.pack()
username_entry = tk.Entry(window)
username_entry.pack()

# name
name_label = tk.Label(window, text= "name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Email
email_label = tk.Label(window, text="email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

# Dob
dob_label = tk.Label(window, text="dob:")
dob_label.pack()
dob_entry = tk.Entry(window)
dob_entry.pack()


tk.Label(window, text="Password:").pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

tk.Button(window, text="Login", command=login).pack()

window.mainloop()
