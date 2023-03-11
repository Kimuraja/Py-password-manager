from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '?', '-', '_', '=', '{', '}', '[', ']']

    let = [choice(letters) for _ in range(randint(8, 10))]
    sym = [choice(symbols) for _ in range(randint(2, 4))]
    num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = let + sym + num
    shuffle(password_list)

    password = "".join(password_list)
    inp_psw.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def data_save():
    web = inp_web.get()
    email = inp_user.get()
    password = inp_psw.get()
    new_data = {web: {
        "email": email,
        "password": password,
        }
    }

    if not web or not email or not password:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)

        finally:
            inp_psw.delete(0, END)
            inp_web.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# ----------WEBSITE----------#
web_txt = Label(text="Website:")
web_txt.grid(column=0, row=1)

inp_web = Entry(width=38)
inp_web.grid(row=1, column=1, columnspan=2)
inp_web.focus()

# ----------USER----------#
user_txt = Label(text="Email/Username:")
user_txt.grid(column=0, row=2)

inp_user = Entry(width=38)
inp_user.grid(row=2, column=1, columnspan=2)
inp_user.insert(END, "your.email@gmail.com")

# ----------Password----------#
psw_txt = Label(text="Password:")
psw_txt.grid(column=0, row=3)

inp_psw = Entry(width=21)
inp_psw.grid(row=3, column=1)

psw_button = Button(text="Generate Password", command=generate_password)
psw_button.grid(row=3, column=2)

# ----------Add Button----------#
add_button = Button(text="Add", width=36, command=data_save)
add_button.grid(row=4, column=1, columnspan=2)


mainloop()
