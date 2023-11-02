import tkinter as tk
import random


# Function to generate a specified number of random numbers and update the label
def generate_random_numbers():
    min_value = int(min_entry.get())
    max_value = int(max_entry.get())
    num_to_generate = int(num_entry.get())
   
    if min_value < max_value:
        random_numbers = [random.randint(min_value, max_value) for _ in range(num_to_generate)]
        result_label.config(text=f"Random Numbers: {', '.join(map(str, random_numbers))}")
    else:
        result_label.config(text="Invalid Input")


# Create the main window
root = tk.Tk()
root.title("Random Number Generator")


# Create and place labels and entry fields
min_label = tk.Label(root, text="Min Value:")
min_label.pack()
min_entry = tk.Entry(root)
min_entry.pack()


max_label = tk.Label(root, text="Max Value:")
max_label.pack()
max_entry = tk.Entry(root)
max_entry.pack()


num_label = tk.Label(root, text="Number of Random Numbers:")
num_label.pack()
num_entry = tk.Entry(root)
num_entry.pack()


result_label = tk.Label(root, text="Random Numbers:")
result_label.pack()


# Create and place the "Generate" button
generate_button = tk.Button(root, text="Generate", command=generate_random_numbers)
generate_button.pack()


# Run the Tkinter main loop
root.mainloop()





