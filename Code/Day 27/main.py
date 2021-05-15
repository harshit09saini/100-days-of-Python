# Introduction to Tkinter
# Miles to Km

import tkinter as tk

window = tk.Tk()
window.title("Miles to Km Converter")
window.minsize()
window.config(padx=10, pady=10)

miles_input = tk.Entry()
miles_input.grid(row=0, column=1)

miles_label = tk.Label(text="Miles", font=("Times New Roman", 15, "normal"))
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)

is_equal_to_label = tk.Label(
    text="is equal to", font=("Times New Roman", 15, "normal"))
is_equal_to_label.grid(row=1, column=0)
is_equal_to_label.config(padx=20, pady=20)
km_value = tk.Label(text="0", font=("Times New Roman", 15, "normal"))


def miles_to_km():
    miles = int(miles_input.get())
    km = miles * 1.609
    km_value.config(text=km,  font=("Times New Roman", 20, "bold"))
    km_value.grid(row=1, column=1)


km_label = tk.Label(text="km", font=("Times New Roman", 15, "normal"))
km_label.grid(row=1, column=2)

calculate_button = tk.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)
calculate_button.config(padx=10, pady=10)

window.mainloop()
