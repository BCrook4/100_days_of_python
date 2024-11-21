from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password = password_letters + password_numbers + password_symbols
    shuffle(password)
    password = ''.join(password)

    password_field.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_field.get()
    username = username_field.get()
    password = password_field.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Looks like you left a field empty")

    else:
        is_okay = messagebox.askokcancel(title=website, message= f"These are the details entered: \nUsername: {username}"
                                                       f"\nPassword: {password} \nIs it ok to save?")


        if is_okay:
            website_field.delete(0, END)
            password_field.delete(0, END)
            # username_field.delete(0, END)

            with open("data.text", "a") as file:
                        file.write(f"{website} | {username} | {password}\n")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Website line
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_field = Entry(width= 49)
website_field.grid(column=1, row=1, columnspan=2, sticky="E")
website_field.focus()

# email/username
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_field = Entry(width=49)
username_field.grid(column=1, row=2, columnspan=2, sticky="E")
username_field.insert(0, "bentoncrook3@gmail.com")

# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_field = Entry(width=28)
password_field.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="W")

# add button
add_button = Button(text="Add", width= 41, command= save)
add_button.grid(column=1, row= 4, columnspan=2, sticky="E")






window.mainloop()