import tkinter as tk
from tkinter import messagebox
import time
import random


class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x300")

        # Sample texts for the test
        self.samples = [
            "The quick brown fox jumps over the lazy dog.",
            "Practice makes perfect. Keep typing to improve your speed.",
            "Python is a versatile programming language loved by many developers.",
            "Consistency is the key to mastering any skill, including typing.",
            "Typing speed can greatly enhance your productivity and efficiency."
        ]
        self.sample = random.choice(self.samples)

        # UI Elements
        tk.Label(root, text="Typing Speed Test", font=("Helvetica", 20)).pack(pady=10)
        self.sample_label = tk.Label(root, text=self.sample, wraplength=700, font=("Helvetica", 14))
        self.sample_label.pack(pady=10)
        self.text_input = tk.Text(root, height=5, width=80, font=("Helvetica", 14))
        self.text_input.pack()
        self.text_input.bind("<KeyPress>", self.start_timer)
        self.text_input.bind("<KeyRelease>", self.check_typing)
        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=10)
        self.reset_btn = tk.Button(root, text="Reset", command=self.reset_test, state=tk.DISABLED)
        self.reset_btn.pack()

        # Timer and state
        self.start_time = None
        self.end_time = None
        self.completed = False

    def start_timer(self, event):
        if not self.start_time:
            self.start_time = time.time()  # Start timing on first key press

    def check_typing(self, event):
        if self.completed:
            return
        # Use "end-1c" to exclude the extra newline character added by Text widget
        typed = self.text_input.get("1.0", "end-1c").strip()
        sample = self.sample.strip()
        if typed == sample:
            self.end_time = time.time()
            self.calculate_wpm()
            self.completed = True
            self.reset_btn.config(state=tk.NORMAL)

    def calculate_wpm(self):
        duration = self.end_time - self.start_time
        minutes = duration / 60
        words = len(self.sample.split())
        wpm = round(words / minutes) if minutes > 0 else 0
        # Determine performance
        if wpm < 40:
            perf = "Below Average"
        elif wpm <= 100:
            perf = "Average"
        else:
            perf = "Above Average"
        self.result_label.config(text=f"Your speed: {wpm} WPM\nPerformance: {perf}")

    def reset_test(self):
        self.sample = random.choice(self.samples)
        self.sample_label.config(text=self.sample)
        self.text_input.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.end_time = None
        self.completed = False
        self.reset_btn.config(state=tk.DISABLED)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    TypingTestApp(root)
    root.mainloop()
