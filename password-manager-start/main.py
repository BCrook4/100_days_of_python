from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Looks like you left a field empty")

    else:
        try:
            with open("data.json", "r") as file:
                # reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating old data
            data.update(new_data)

            with open("data.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)

        finally:
            website_field.delete(0, END)
            password_field.delete(0, END)
            # username_field.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website_to_find = website_field.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found")

    else:
        if website_to_find in data:
            password = data[website_to_find]['password']
            username = data[website_to_find]['username']
            messagebox.showinfo(title=website_to_find, message=f"Email/Username: {username}\n\nPassword: {password}")
        else:
            messagebox.showinfo(title=website_to_find, message=f"No details for {website_to_find} exist.")

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

website_field = Entry(width=28)
website_field.grid(column=1, row=1)
website_field.focus()

website_search_button = Button(text="Search", width=14, command=find_password)
website_search_button.grid(column=2, row=1, sticky="W")

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