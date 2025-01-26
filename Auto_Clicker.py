import time
import pyautogui
import tkinter as tk
from threading import Thread, Event

class AutoClicker:
    def __init__(self):
        self.is_running = False
        self.stop_event = Event()

    def start_clicking(self):
        # Get the values from the form
        num_clicks = clicks_entry.get()
        delay = delay_entry.get()

        # Convert the values to integers
        num_clicks = int(num_clicks)
        delay = float(delay)

        # Click the mouse the specified number of times
        for i in range(num_clicks):
            if self.stop_event.is_set():
                break
            pyautogui.click()
            time.sleep(delay)

        self.is_running = False

    def start_auto_clicker(self):
        if not self.is_running:
            self.is_running = True
            self.stop_event.clear()
            auto_click_thread = Thread(target=self.start_clicking)
            auto_click_thread.start()

    def stop_auto_clicker(self):
        if self.is_running:
            self.stop_event.set()

# Create a window
window = tk.Tk()
window.title("Auto Clicker")

# Create an instance of AutoClicker
auto_clicker = AutoClicker()

# Create form fields for the number of clicks and the delay
clicks_label = tk.Label(text="Number of clicks:")
clicks_entry = tk.Entry()
delay_label = tk.Label(text="Delay between clicks (seconds):")
delay_entry = tk.Entry()

# Create buttons to start and stop the autoclicker
start_button = tk.Button(text="Start", command=auto_clicker.start_auto_clicker)
stop_button = tk.Button(text="Stop", command=auto_clicker.stop_auto_clicker)

# Add the form fields and buttons to the window
clicks_label.pack()
clicks_entry.pack()
delay_label.pack()
delay_entry.pack()
start_button.pack()
stop_button.pack()

# Run the tkinter event loop
window.mainloop()
