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

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    inp_psw.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = inp_web.get()
    email = inp_user.get()
    password = inp_psw.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            inp_web.delete(0, END)
            inp_psw.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = inp_web.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

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
web_txt.grid(row=1, column=0)

inp_web = Entry(width=21)
inp_web.grid(row=1, column=1)
inp_web.focus()

web_button = Button(text="Search", width=14)
web_button.grid(row=1, column=2)
# ----------USER----------#
user_txt = Label(text="Email/Username:")
user_txt.grid(row=2, column=0)

inp_user = Entry(width=39)
inp_user.grid(row=2, column=1, columnspan=2)
inp_user.insert(END, "your.email@gmail.com")

# ----------Password----------#
psw_txt = Label(text="Password:")
psw_txt.grid(row=3, column=0)

inp_psw = Entry(width=21)
inp_psw.grid(row=3, column=1)

psw_button = Button(text="Generate Password", command=generate_password)
psw_button.grid(row=3, column=2)

# ----------Add Button----------#
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


mainloop()
