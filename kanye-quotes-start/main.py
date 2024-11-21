from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    response_json = response.json()
    quote = response_json["quote"]
    if len(quote) > 100:
        canvas.itemconfig(quote_text, text=quote, font= ("Arial", 18, "bold"))
    elif len(quote) > 75:
        canvas.itemconfig(quote_text, text=quote, font=("Arial", 20, "bold"))
    else:
        canvas.itemconfig(quote_text, text=quote, font=("Arial", 30, "bold"))
    #Write your code here.

test = ("I think I do myself a disservice by comparing myself to Steve Jobs and Walt Disney and human beings"
        " that we've seen before. It should be more like Willy Wonka...and welcome to my chocolate factory.")
test = "I am Warhol. I am the No. 1 most impactful artist of our generation. I am Shakespeare in the flesh."
print(len(test))

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bd=0)
kanye_button.grid(row=1, column=0)



window.mainloop()