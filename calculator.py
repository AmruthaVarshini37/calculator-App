import tkinter as tk

def on_click(event):
    button_text = event.widget["text"]

    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row_values in buttons:
    row_frame = tk.Frame(root)
    row_frame.pack(expand=True, fill="both")
    for value in row_values:
        btn = tk.Button(row_frame, text=value, font=("Arial", 18), relief=tk.RAISED, bd=5)
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

root.mainloop()
