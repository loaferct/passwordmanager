from tkinter import *
from tkinter import messagebox
import random
from random import shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)] 
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title = website, message = f'These are the details entered: \nEmail: {email} \npassword: {password} \nIs it ok to save?')

    if is_ok:
        if len(website) == 0 or len(password) ==  0 :
            messagebox.showinfo(title = 'warining', message = 'Empty fields')

        else:    
            with open("data.file",'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

    



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager App")
window.config(padx = 50, pady = 20)
#window.minsize(width = 300, height = 300)

canvas = Canvas(width = 200, height = 200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(column = 1, row = 0)


website_label = Label(text = 'Website: ')
website_label.grid(column = 0, row = 1)

website_entry = Entry(width = 35)
website_entry.grid(column = 1, row = 1, columnspan = 2)
website_entry.focus()

email_label = Label(text = 'Email/Username: ')
email_label.grid(column = 0, row = 2)

email_entry = Entry(width = 35)
email_entry.insert(0,"sauravkatwalkatwal@gmail.com")
email_entry.grid(column = 1, row = 2, columnspan = 2)

password_label = Label(text = 'Password: ')
password_label.grid(column = 0 ,row = 3)

password_entry = Entry(width = 21)
password_entry.grid(column = 1, row = 3)

generate_password_button = Button(text = 'Generate Password', command = generate_password)
generate_password_button.grid(column = 2, row = 3)

add_button = Button(text = 'Add', width = 36, command = save)
add_button.grid(column = 1, row = 4, columnspan = 2)








window.mainloop()