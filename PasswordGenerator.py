import string
import random
import tkinter as tk
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, length, complexity):
        self.length = length
        self.complexity = complexity
    
    charset_basic = list(string.ascii_letters)
    charset_complex = list(string.ascii_letters + string.digits)
    chartset_all = list(string.ascii_letters + string.digits + string.punctuation)

    def generate_password(self):
        password = ''
        if self.complexity == 1:
            for i in range(self.length):
                password += random.choice(self.charset_basic)
        elif self.complexity == 2:
            for i in range(self.length):
                password += random.choice(self.charset_complex)
        elif self.complexity == 3:
            for i in range(self.length):
                password += random.choice(self.chartset_all)
        return password

def on_generate_button_click():
    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()
        generator = PasswordGenerator(length, complexity)
        password = generator.generate_password()
        result_label.config(text=password)
        # Enable the copy button after generating the password
        copy_button.config(state=tk.NORMAL)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

def on_copy_button_click():
    password = result_label.cget("text")
    if password:
        app.clipboard_clear()
        app.clipboard_append(password)
        messagebox.showinfo("Info", "Password copied to clipboard.")

app = tk.Tk()
app.title("Password Generator")

# Length Entry
tk.Label(app, text="Desired password length:").grid(row=0, column=0)
length_entry = tk.Entry(app)
length_entry.grid(row=0, column=1)

# Complexity Buttons
complexity_var = tk.IntVar(value=1)  # Set default value
tk.Label(app, text="Password Complexity:").grid(row=1, column=0)
radiobuttons_frame = tk.Frame(app)
tk.Radiobutton(radiobuttons_frame, text="Only Letters", variable=complexity_var, value=1).pack(side=tk.LEFT)
tk.Radiobutton(radiobuttons_frame, text="Letters & Numbers", variable=complexity_var, value=2).pack(side=tk.LEFT)
tk.Radiobutton(radiobuttons_frame, text="All Characters", variable=complexity_var, value=3).pack(side=tk.LEFT)
radiobuttons_frame.grid(row=1, column=1)

# Creating Button
generate_button = tk.Button(app, text="Generate", command=on_generate_button_click)
generate_button.grid(row=2, column=0, columnspan=2)

# Result Label
result_label = tk.Label(app, text="", font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=2)

# Creating the copy button
copy_button = tk.Button(app, text="Copy to Clipboard", command=on_copy_button_click, state=tk.DISABLED)
copy_button.grid(row=4, column=0, columnspan=2)

app.mainloop()
