from tkinter import *

def button_click():
    miles = float(input_miles.get())
    result_text.config(text= convert(miles))

def convert(miles):
    return miles*1.609344

# create window
window = Tk()
window.title("Mile to Km Conversion")
window.config(padx=50, pady=50)

# create label for miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# input entry box
input_miles = Entry(width=10)
input_miles.insert(END, string="0")
input_miles.grid(column=1, row=0)

# is equal label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=20, pady=10)

#TODO: have a text that gets updated with the calculation
result_text = Label(text= "0")
result_text.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=button_click)
calc_button.grid(column=1, row=2)





















window.mainloop()