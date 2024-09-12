import random
import string
import tkinter as tk
from tkinter import messagebox

def password_generator(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

def save_password(site_name, login, password):
    with open(r"D:\DOKUMENTY\BAZA.txt", "a") as file:
        file.write(f"{site_name} | {login} | {password}\n")

def generate_password():
    try:
        min_length = int(entry_length.get())
        has_number = var_numbers.get()
        has_special = var_special.get()
        site_name = entry_site.get()
        login = entry_login.get()

        pwd = password_generator(min_length, has_number, has_special)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, pwd)

        save_password(site_name, login, pwd)
        messagebox.showinfo("Sukces", "Hasło zostało wygenerowane i zapisane.")
    except ValueError:
        messagebox.showerror("Błąd", "Minimalna długość hasła musi być liczbą całkowitą.")



# ------------------------------------------------------------------------------------------------
# Tworzenie GUI
# ------------------------------------------------------------------------------------------------

def on_enter(event):
    button_generate.config(bg="darkred")


def on_leave(event):
    button_generate.config(bg="red")

root = tk.Tk()
root.title("Generator haseł")

# Ustawienie ikony programu
icon = tk.PhotoImage(file="icon.ico")
root.iconphoto(False, icon)

# Ustawienie rozmiaru okna
root.geometry("800x400")

# Konfiguracja grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1)

font_settings = ("Helvetica", 14)

tk.Label(root, text="Nazwa strony:", font=font_settings).grid(row=1, column=1, sticky="ew")
entry_site = tk.Entry(root, font=font_settings)
entry_site.grid(row=1, column=2, columnspan=2, sticky="ew")

tk.Label(root, text="Nazwa użytkownika:", font=font_settings).grid(row=2, column=1, sticky="ew")
entry_login = tk.Entry(root, font=font_settings)
entry_login.grid(row=2, column=2, columnspan=2, sticky="ew")

tk.Label(root, text="Minimalna długość hasła:", font=font_settings).grid(row=3, column=1, sticky="ew")
entry_length = tk.Entry(root, font=font_settings)
entry_length.grid(row=3, column=2, columnspan=2, sticky="ew")

var_numbers = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Zawiera liczby", variable=var_numbers, font=font_settings).grid(row=4, column=1, columnspan=3, sticky="ew")

var_special = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Zawiera znaki specjalne", variable=var_special, font=font_settings).grid(row=5, column=1, columnspan=3, sticky="ew")

button_generate = tk.Button(root, text="Generuj hasło", command=generate_password, font=font_settings, bg="red", fg="white")
button_generate.grid(row=6, column=1, columnspan=3, sticky="ew")

button_generate.bind("<Enter>", on_enter)
button_generate.bind("<Leave>", on_leave)

tk.Label(root, text="Wygenerowane hasło:", font=font_settings).grid(row=7, column=1, sticky="ew")
entry_password = tk.Entry(root, font=font_settings)
entry_password.grid(row=7, column=2, columnspan=2, sticky="ew")

root.mainloop()
