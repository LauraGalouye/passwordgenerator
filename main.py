import random
import string   
from tkinter import *

def generatepassword():
    print ("Welcome to the password generator")

    length = int(my_variable.get())
    include_lower = include_lower_var.get() == 1
    include_upper = include_upper_var.get() == 1
    include_number = include_number_var.get() == 1 
    include_special = include_special_var.get() == 1

    caracteres = ''
    
    if include_lower:
        caracteres += string.ascii_lowercase
    if include_upper:
        caracteres += string.ascii_uppercase
    if include_number:
        caracteres += string.digits
    if include_special:
        caracteres += string.punctuation

    if not caracteres:
        print('No characters selected')
        return None, 
    
    password = ''.join(random.choice(caracteres) for i in range(length))
    generated_password_label.config(text='Generated password: ' + password)
  



fenetre = Tk()
fenetre.geometry("500x500")
fenetre.title("Password Generator")
fenetre['bg'] = 'lightgray'
fenetre.resizable(width=False, height=False)



label = Label(fenetre, text="Enter the length of the password: ")
label.pack()

my_variable = StringVar()
entree = Entry(fenetre, textvariable=my_variable)
entree.pack()

options_frame = Frame(fenetre)
options_frame.pack(pady=10)

include_lower_var = IntVar()
include_lower_checkbox = Checkbutton(fenetre, text="Include lowercase letters", variable=include_lower_var)
include_lower_checkbox.pack()

include_upper_var = IntVar()
include_upper_checkbox = Checkbutton(fenetre, text="Include uppercase letters", variable=include_upper_var)
include_upper_checkbox.pack()

include_number_var = IntVar()
include_number_checkbox = Checkbutton(fenetre, text="Include numbers", variable=include_number_var)
include_number_checkbox.pack()

include_special_var = IntVar()
include_special_checkbox = Checkbutton(fenetre, text="Include special characters", variable=include_special_var)
include_special_checkbox.pack()

generate_button = Button(fenetre, text="Generate", command=generatepassword)
generate_button.pack()

generated_password_label = Label (fenetre, text="")
generated_password_label.pack()

fenetre.mainloop()