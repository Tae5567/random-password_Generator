#Random Password Generator

from tkinter import *
import secrets
import string

#Initialize Window
 
root =Tk()
root.geometry("400x400") #size of the window by default
 
#title of our window
root.title("Random Password Generator")

###------------Random Password Generator------------------###
#Passwords generated should contain letters, numbers and special characters

printPassword = StringVar()

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

#set password length
#passLength = 12


#generate random password that meets constraints: contains:
#at least 8 characters, 1 number and 1 special character
def randomPassword():
    password = '' #initialize empty string
    for i in range(passLength.get()):
        password += ''.join(secrets.choice(alphabet))

    printPassword.set(password)



#get length of password
 
pass_head = Label(root, text = 'Password Length', font = 'arial 12 bold').pack(pady=10) #to generate label heading
 
passLength = IntVar() #integer variable to store the input of length of the password wanted
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = passLength , width = 24, font='arial 16').pack()


#Generate password button
Button(root, text = "Generate Password" , command = randomPassword, font="Arial 10", bg='lightpink', fg='black', activebackground="magenta", padx=5, pady=5 ).pack(pady= 20)


pass_label = Label(root, text = 'Your password is', font = 'arial 12 bold').pack(pady="30 10")
Entry(root , textvariable = printPassword, width = 24, font='arial 16').pack()

root.mainloop()
