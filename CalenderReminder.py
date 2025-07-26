import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkcalendar import Calendar
import json
import os

REMINDER_FILE = "reminders.json"

def load_reminders():
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r") as f:
            return json.load(f)
    return {}

def save_reminders(reminders):
    with open(REMINDER_FILE, "w") as f:
        json.dump(reminders, f, indent=4)

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monthly Calendar with Reminders")
        self.root.geometry("600x500")
        self.root.configure(bg="#f5f5f5")

        self.reminders = load_reminders()

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 10), padding=6)
        style.configure("TLabel", background="#f5f5f5", font=("Segoe UI", 10))

        self.cal = Calendar(self.root, selectmode='day', date_pattern='yyyy-mm-dd')
        self.cal.pack(pady=20)

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_btn = ttk.Button(self.button_frame, text="Add Reminder", command=self.add_reminder)
        self.add_btn.grid(row=0, column=0, padx=10)

        self.view_btn = ttk.Button(self.button_frame, text="View Reminders", command=self.view_reminders)
        self.view_btn.grid(row=0, column=1, padx=10)

        self.clear_btn = ttk.Button(self.button_frame, text="Delete Reminders", command=self.delete_reminders)
        self.clear_btn.grid(row=0, column=2, padx=10)

        self.status = ttk.Label(self.root, text="Select a date to manage reminders")
        self.status.pack(pady=10)

    def add_reminder(self):
        date = self.cal.get_date()
        reminder = simpledialog.askstring("Add Reminder", f"Enter reminder for {date}:")
        if reminder:
            self.reminders.setdefault(date, []).append(reminder)
            save_reminders(self.reminders)
            messagebox.showinfo("Saved", "Reminder added successfully!")

    def view_reminders(self):
        date = self.cal.get_date()
        reminders = self.reminders.get(date, [])
        if reminders:
            reminder_text = "\n".join(f"{i+1}. {rem}" for i, rem in enumerate(reminders))
        else:
            reminder_text = "No reminders for this date."

        messagebox.showinfo(f"Reminders for {date}", reminder_text)

    def delete_reminders(self):
        date = self.cal.get_date()
        if date in self.reminders:
            if messagebox.askyesno("Confirm Delete", f"Delete all reminders for {date}?"):
                del self.reminders[date]
                save_reminders(self.reminders)
                messagebox.showinfo("Deleted", "Reminders deleted.")
        else:
            messagebox.showinfo("No Reminders", "No reminders to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
