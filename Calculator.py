import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("260x360")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        self.expression = ""

        self.entry = tk.Entry(
            root, font=("Arial", 14), bd=3, relief="sunken",
            justify="right", bg="white"
        )
        self.entry.pack(fill="x", padx=10, pady=10, ipady=8)

        self.button_frame = tk.Frame(root, bg="#f5f5f5")
        self.button_frame.pack(padx=10)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"],
            ["="]
        ]

        for row in buttons:
            row_frame = tk.Frame(self.button_frame, bg="#f5f5f5")
            row_frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    row_frame, text=char, font=("Arial", 12), width=5, height=2,
                    bg="#e1e1e1", activebackground="#dcdcdc", bd=1,
                    command=lambda c=char: self.handle_input(c)
                )
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    def handle_input(self, char):
        if char == "C":
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
                self.expression = result
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.expression = ""
                self.entry.delete(0, tk.END)
            except:
                messagebox.showerror("Error", "Invalid input")
                self.expression = ""
                self.entry.delete(0, tk.END)
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
