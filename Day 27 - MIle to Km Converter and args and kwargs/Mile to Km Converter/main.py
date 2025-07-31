from tkinter import *

def miles_to_km():
    miles = float(mile_input.get())
    km = miles * 1.609
    km_rounded = round(km, 2)
    km_result_label.config(text=f"{km_rounded}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

mile_input = Entry(width=7)
mile_input.grid(column=1,row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2,row=0)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

equals_label = Label(text="=")
equals_label.grid(column=0,row=1)

convert_button = Button(text="Convert", command=miles_to_km)
convert_button.grid(column=1,row=2)

window.mainloop()