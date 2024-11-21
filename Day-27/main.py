from tkinter import *
# from playground import add

def button_clicked():
    # print("I got clicked")
    my_label.config(text= input.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100, y=0)
my_label.grid(column= 0, row=0)
my_label.config(padx=50,pady=50)

my_label["text"] = "New Text"
my_label.config(text="Newer Text")

# Button
button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column= 1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column= 2, row=0)


# Entry
input = Entry(window, width=20, validate="key")
# input.pack()
input.grid(column= 3, row=2)











window.mainloop()