import tkinter as tk
from tkinter import messagebox

def encode_message():
    message = input_text.get("1.0", tk.END).strip()
    shift = shift_value.get()
    if not message:
        messagebox.showerror("Error", "Please enter a message to encode.")
        return
    encoded = ''.join(
        chr(((ord(char) - 65 + shift) % 26 ) + 65) if char.isupper() else 
        chr(((ord(char) - 97 + shift) % 26)  + 97) if char.islower() else 
        char 
        for char in message
    )
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encoded)

def decode_message():
    message = input_text.get("1.0", tk.END).strip()
    shift = shift_value.get()
    if not message:
        messagebox.showerror("Error", "Please enter a message to decode.")
        return
    decoded = ''.join(
        chr(((ord(char) - 65 - shift) % 26) + 65) if char.isupper() else 
        chr(((ord(char) - 97 - shift) % 26) + 97) if char.islower() else 
        char 
        for char in message
    )
    output_text.delete("1.0", tk.END) 
    output_text.insert(tk.END, decoded)

def clear_screen():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    shift_value.set(3)      # Reset the shift value to default (3)

# Create the Main Window
root = tk.Tk()
root.title("Message Encoder and Decoder")

root.geometry("500x400")

# Input Text
tk.Label(root, text="Input Message:", font=("Arial", 12)).pack(pady=5)
input_text = tk.Text(root, height=5, width=50)
input_text.pack(pady=5)

# Shift Value
tk.Label(root, text="Shift Value: ", font=("Arial", 12)).pack(pady=5)
shift_value = tk.IntVar(value=3)
tk.Spinbox(root, from_=1, to=25, textvariable=shift_value, width=5).pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Encode", command=encode_message, width=10).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Decode", command=decode_message, width=10).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Clear Screen", command=clear_screen, width=10).grid(row=0, column=2, padx=5)

# Output Text
tk.Label(root, text="Output Message: ", font=("Arial", 12)).pack(pady=5)
output_text = tk.Text(root, height=5, width=50)
output_text.pack(pady=5)

# Run the main loop
root.mainloop()

