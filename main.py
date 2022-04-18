import random
from tkinter import *
from tkinter import messagebox



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # using list comprehension
    letter_list=[random.choice(letters) for _ in range(random.randint(6,9))]
    numbers_list=[random.choice(numbers) for _ in range(random.randint(3,5))]
    symbols_list=[random.choice(symbols) for _ in range(random.randint(3,5))]

    password_list=letter_list+numbers_list+symbols_list
    random.shuffle(password_list)
    password=""

    for char in password_list:
        password+=char

    password_entry.insert(0,password)   # inserting the generated password


# ---------------------------- SAVE PASSWORD ------------------------------- #

#save button methood
def save():
    website_data = website_entry.get() #getting the website entry
    email_data = email_entry.get()    #getting the email entry
    password_data = password_entry.get()  #getting the password entry




    if len(website_data)== 0 or len(password_data)  == 0: #checking  empty entries
        # displaying warning message
        messagebox.showinfo(title='Warning', message="Don't leave any field empty")
    else:
        #displaying confirmation message
        msg_option = messagebox.askyesno(title="Notificaton", message=f" Website :{website_data}\n "
                                                                                  f"Email :{email_data} \n "
                                                                                  f"Password : {password_data}\n"
                                                                                  f"Do you want to proceed")
        if msg_option:

            with open("Data.txt" , "a") as data:# opening the file Data.txt inn append mode
                #saving the datas to the fie Data.txt
                data.write(f"{website_data} | {email_data} | {password_data} \n")
        password_entry.delete(0, END)
        website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('PASSWORD GENERATOR')
#window.minsize(width=400,height=400)
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
pass_image=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=pass_image)
canvas.grid(column=1,row=0)

#labels
website_label=Label(text="Website")
website_label.grid(column=0,row=1)
email_label=Label(text="Email/Username")
email_label.grid(column=0,row=2)
password_label=Label(text="Password")
password_label.grid(column=0,row=3)

#enteries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,'akhilr@gmail.com')      #inserting a defeault eemail entry
password_entry=Entry(width=25)
password_entry.grid(row=3,column=1)

#buttons
generate_button=Button(text="Generate password",command=password_generator)
generate_button.grid(row=3,column=2)
add_button=Button(text="ADD",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()