import tkinter as tk
from tkinter import messagebox
import time
import random

# List of sample sentences for typing test
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed is measured in words per minute.",
    "Python is a versatile programming language.",
    "Practice makes perfect when learning to code.",
    "Artificial intelligence is transforming the world."
]

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        # Initialize variables
        self.start_time = None
        self.selected_sentence = random.choice(SENTENCES)

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Title label
        self.title_label = tk.Label(self.root, text="Typing Speed Test", font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=20)

        # Sentence to type
        self.sentence_label = tk.Label(self.root, text=self.selected_sentence, wraplength=600, font=("Helvetica", 14))
        self.sentence_label.pack(pady=10)

        # Entry box for user input
        self.input_entry = tk.Entry(self.root, font=("Helvetica", 14), width=80)
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<FocusIn>", self.start_timer)

        # Submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.calculate_speed, font=("Helvetica", 12))
        self.submit_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_test, font=("Helvetica", 12))
        self.reset_button.pack(pady=5)

    def start_timer(self, event):
        # Start the timer when user focuses on the entry box
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self):
        # Calculate typing speed in WPM
        end_time = time.time()
        typed_text = self.input_entry.get().strip()
        elapsed_time = end_time - self.start_time if self.start_time else 0

        if not typed_text:
            messagebox.showwarning("Empty Input", "Please type the sentence before submitting.")
            return

        # Count words typed
        word_count = len(typed_text.split())
        wpm = round((word_count / elapsed_time) * 60) if elapsed_time > 0 else 0

        # Compare with original sentence
        if typed_text == self.selected_sentence:
            self.result_label.config(text=f"✅ Correct! Your typing speed is {wpm} WPM.")
        else:
            self.result_label.config(text=f"⚠️ Text mismatch. Your typing speed is {wpm} WPM.")

    def reset_test(self):
        # Reset the test for another round
        self.start_time = None
        self.selected_sentence = random.choice(SENTENCES)
        self.sentence_label.config(text=self.selected_sentence)
        self.input_entry.delete(0, tk.END)
        self.result_label.config(text="")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
