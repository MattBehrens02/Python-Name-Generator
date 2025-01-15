import string
import random
import tkinter as tk

VOWELS = "aeiou"
CONSTONANTS = "".join(i for i in string.ascii_lowercase if i not in VOWELS)

def Create_Name():
    key =input_box.get().lower()

    result = []

    for char in key:
        if char == 'c': result.append(random.choice(CONSTONANTS))
        elif char == 'v': result.append(random.choice(VOWELS))
        else: result.append(char) # just in case somebody can't follow instructions

    generated_name = ''.join(result).capitalize()

    output_label.config(text=generated_name)
    
root = tk.Tk()
root.title("Random Name Generator")
root.geometry("800x600")

input_label = tk.Label(root, text="Enter in a key for a name using [c]onsonant or [v]owels")
input_label.pack(pady=5)

input_box = tk.Entry(root, width=30)
input_box.pack(pady=5)

output_label = tk.Label(root, text="Output will appear here", fg="gray")
output_label.pack(pady=20)
    
submit_button = tk.Button(root, text="commenceth name generation", command=Create_Name)
submit_button.pack(pady=10)

root.mainloop()