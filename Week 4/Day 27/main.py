import tkinter as tk

window = tk.Tk()
window.title("Test")
window.minsize(width=600, height=480)
label = tk.Label(text="Hey :)", font=("Arial", 20, "bold"))
label.grid(row=0, column=0)

def label_text():
    label["text"] = f"Hello {input.get()}! c:"

button = tk.Button(text="Click me!", command=label_text)
button.grid(row=0, column=2)

button2 = tk.Button(text="Second button! c:")
button2.grid(row=1, column=1)

input = tk.Entry(width=10)
input.grid(row=2, column=3)


window.mainloop()