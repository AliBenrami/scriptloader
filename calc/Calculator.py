import tkinter as tk


# Create a function to update the display
def update_display(value):
    current_text = display.get()
    if current_text == "0":
        display.set(value)
    else:
        display.set(current_text + value)


# Create a function to clear the display
def clear_display():
    display.set("0")


# Create a function to evaluate the expression
def evaluate():
    try:
        expression = display.get().replace("%", "/100")
        result = eval(expression)
        display.set(str(result))
    except:
        display.set("Error")


# Create the main window
root = tk.Tk()
root.title("Calculator")


# Create a variable to store the display value
display = tk.StringVar()
display.set("0")


# Create the display entry widget
display_entry = tk.Entry(root, textvariable=display, font=("Helvetica", 20), justify="right")
display_entry.grid(row=0, column=0, columnspan=4)


# Create the calculator buttons
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "(", "+",
    ")", "%", "C", "="
]


row = 1
col = 0


for button_text in button_texts:
    if button_text == "=":
        tk.Button(root, text=button_text, command=evaluate, font=("Helvetica", 20)).grid(row=row, column=col)
    elif button_text == "C":
        tk.Button(root, text=button_text, command=clear_display, font=("Helvetica", 20)).grid(row=row, column=col)
    else:
        tk.Button(root, text=button_text, command=lambda value=button_text: update_display(value), font=("Helvetica", 20)).grid(row=row, column=col)


    col += 1
    if col > 3:
        col = 0
        row += 1


# Start the main loop
root.mainloop()
