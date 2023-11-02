import tkinter as tk
from tkinter.colorchooser import askcolor


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")


        self.pen_color = "black"
        self.pen_width = 2
        self.eraser_mode = False


        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(side="left", fill="y")


        self.change_color_button = tk.Button(self.options_frame, text="Change Color", command=self.change_color)
        self.change_color_button.pack()


        self.width_label = tk.Label(self.options_frame, text="Pen Width:")
        self.width_label.pack()
        self.pen_width_slider = tk.Scale(self.options_frame, from_=1, to=10, orient="horizontal", length=200, command=self.change_width)
        self.pen_width_slider.set(self.pen_width)
        self.pen_width_slider.pack()


        self.eraser_button = tk.Button(self.options_frame, text="Eraser", command=self.toggle_eraser)
        self.eraser_button.pack()


        self.reset_button = tk.Button(self.options_frame, text="Reset", command=self.reset)
        self.reset_button.pack()


        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)


        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)


    def start_drawing(self, event):
        self.last_x = event.x
        self.last_y = event.y


    def draw(self, event):
        x, y = event.x, event.y
        if not self.eraser_mode:
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.pen_color, width=self.pen_width, capstyle=tk.ROUND, smooth=tk.TRUE)
        else:
            self.canvas.create_rectangle(x - self.pen_width, y - self.pen_width, x + self.pen_width, y + self.pen_width, fill="white", outline="white")
        self.last_x = x
        self.last_y = y


    def change_color(self):
        color = askcolor(title="Choose Pen Color", color=self.pen_color)[1]
        if color:
            self.pen_color = color


    def change_width(self, value):
        self.pen_width = int(value)


    def toggle_eraser(self):
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.eraser_button.config(text="Pen")
        else:
            self.eraser_button.config(text="Eraser")


    def reset(self):
        self.canvas.delete("all")  # Clear the canvas
        self.pen_color = "black"
        self.pen_width = 2
        self.eraser_mode = False
        self.pen_width_slider.set(self.pen_width)


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()



