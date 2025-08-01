from tkinter import *
from tkinter import messagebox
import csv
from random import randint,shuffle,choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
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

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = selected_email.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty. 😅")
    else:
        is_ok = messagebox.askokcancel(title=website, message= f"There are the details entered:\n\nEmail: {email}\nPassword: {password}\n\nIs that ok to save? 🤨")

        if is_ok:
            with open(file="data.csv", mode="a", newline="") as file:
                write = csv.writer(file)
                write.writerow([website,email,password])
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                messagebox.showinfo(title="Saved!", message="Your entry has been saved! 🎉")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30,pady=30, bg="white")

canvas = Canvas(height=200,width=300, bg="white", highlightthickness=0)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_png)
canvas.grid(column=1, row=0, columnspan=3)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35, highlightbackground="white")
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)

selected_email = StringVar()
selected_email.set("badshah.mustafa77@gmail.com")

email_menu = OptionMenu(window, selected_email,"badshah.mustafa77@gmail.com","mustafachillin@gmail.com","1948356@fcpsschools.net","avengermustafa7@gmail.com")
email_menu.config(bg="white", highlightbackground="white", width=31)
email_menu.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

password_entry = Entry(width=18, highlightbackground="white")
password_entry.grid(column=1, row=3, sticky="E")

password_button = Button(text="Generate Password", highlightbackground="white", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="add", width=33, highlightbackground="white", command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()