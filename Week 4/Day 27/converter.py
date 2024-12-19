import tkinter as tk

window = tk.Tk()
window.minsize(width=100, height=70)
window.config(padx=20, pady=20)
window.title("Mile to Km Converter")

def convertToKm(miles):
    try:
        miles = float(miles.strip())
        km = miles * 1.6
        label_result.config(text=km)
    except ValueError: pass
    

input = tk.Entry(width=10)
input.grid(row=0, column=1)

label_miles = tk.Label(text="Miles")
label_miles.grid(row=0, column=2)

label_equal = tk.Label(text="is equal to")
label_equal.grid(row=1, column=0)

label_result = tk.Label(text=0)
label_result.grid(row=1, column=1)

label_km = tk.Label(text="Km")
label_km.grid(row=1, column=2)

button_calc = tk.Button(text="Calculate", command=lambda: convertToKm(input.get()))
button_calc.grid(row=2, column=1)

window.mainloop()