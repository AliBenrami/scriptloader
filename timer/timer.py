import tkinter as tk
from tkinter import colorchooser, messagebox


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")
        self.time_left = 0
        self.running = False
        self.textcolor = "white"  # Default text color


        self.label = tk.Label(root, text="Enter time (hh:mm:ss):", font=("Arial", 12))
        self.label.pack(pady=10)


        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10)


        self.start_button = tk.Button(root, text="Start", command=self.start_timer, font=("Arial", 12))
        self.start_button.pack(pady=10)


        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, font=("Arial", 12))
        self.stop_button.pack(pady=10)
        self.stop_button.config(state=tk.DISABLED)


        self.color_button = tk.Button(root, text="Change Text Color", command=self.change_textcolor, font=("Arial", 12))
        self.color_button.pack(pady=10)


        self.timer_frame = tk.Frame(root, bg="black")
        self.timer_frame.pack(pady=20)
       
        self.timer_display = tk.Label(self.timer_frame, text="", font=("Arial", 36), bg="black", fg=self.textcolor)
        self.timer_display.pack(padx=20, pady=10)


    def start_timer(self):
        if not self.running:
            time_str = self.entry.get()
            try:
                hours, minutes, seconds = map(int, time_str.split(':'))
                total_seconds = hours * 3600 + minutes * 60 + seconds
                self.time_left = total_seconds
                self.running = True
                self.update_display()
                self.start_button.config(state=tk.DISABLED)
                self.stop_button.config(state=tk.NORMAL)
                self.entry.config(state=tk.DISABLED)
                self.count_down()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid time in hh:mm:ss format.")


    def count_down(self):
        if self.time_left > 0 and self.running:
            self.time_left -= 1
            self.update_display()
            self.root.after(1000, self.count_down)
        elif self.running:
            self.label.config(text="Time's up!", font=("Arial", 18))
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.entry.config(state=tk.NORMAL)


    def update_display(self):
        hours = self.time_left // 3600
        minutes = (self.time_left % 3600) // 60
        seconds = self.time_left % 60
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.timer_display.config(text=time_str)


    def stop_timer(self):
        self.running = False
        self.label.config(text="Timer stopped", font=("Arial", 12))
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.entry.config(state=tk.NORMAL)


    def change_textcolor(self):
        newcolor = colorchooser.askcolor()[1]
        if newcolor:
            self.textcolor = newcolor
            self.timer_display.config(fg=self.textcolor)


if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.geometry("400x450")  # Set a custom window size
    root.mainloop()



