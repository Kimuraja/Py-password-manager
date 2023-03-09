from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

inp_web = Entry(width=35)
inp_web.grid(row=1, column=1, columnspan=2)

# ----------USER----------#
user_txt = Label(text="Email/Username:")
user_txt.grid(column=0, row=2)

inp_user = Entry(width=35)
inp_user.grid(row=2, column=1, columnspan=2)

# ----------Password----------#
psw_txt = Label(text="Password:")
psw_txt.grid(column=0, row=3)

inp_psw = Entry(width=21)
inp_psw.grid(row=3, column=1)

psw_button = Button(text="Generate Password")
psw_button.grid(row=3, column=2)

# ----------Add Button----------#
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

mainloop()