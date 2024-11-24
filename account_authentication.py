import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store user data
DATA_FILE = "users.json"

# Create JSON file if it dosen't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump({}, file)

def load_users():
    """Load users from the JSON file."""
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_users(users):
    """Save users to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

def sign_up():
    """Handle sign-up process."""
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    users = load_users()

    if not username or not password:
        messagebox.showerror("Error", "Username and Password cannot be empty !!!")
        return 

    if username in users:
        messagebox.showerror("Error", "Username already exists. Please log in")
    else:
        users[username] = password
        save_users(users)
        messagebox.showinfo("Success", "Sign-Up successful! Please log in.")
        clear_entries()

def log_in():
    """Handle Login Process"""
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    users = load_users()

    if not username or not password:
        messagebox.showerror("Error", "Username and Password cannot be empty.")
        return

    if username in users and users[username] == password:
        messagebox.showinfo("Success", f"Welcome {username}!")
    else:
        messagebox.showerror("Error", "Invalid credentials. Please try again.")

def clear_entries():
    """Clear input fields"""
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Arids :) Sign Up & Log In Page")
root.geometry("400x300")

# Labels and Entry Widgets
label_title = tk.Label(root, text="Sign Up / Log In", font=("Arial", 18))
label_title.pack(pady=10)

label_username = tk.Label(root, text="Username: ")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password: ")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Buttonss
button_signup = tk.Button(root, text ="Sign Up", command=sign_up, width=10)
button_signup.pack(pady=10)

button_login = tk.Button(root, text ="Log In", command=log_in, width=10)
button_login.pack(pady=10)


# Run the GUI Loop
root.mainloop()



































