from tkinter import *
from tkinter import messagebox
import random
import pyperclip
#-------------------------------------------------GENERATE PASSWORD--------------------------------------------
def createpass():
    letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    number=['0','1','2','3','4','5','6','7','8','9']
    symbols=['!','@','#','$','%','^','&','*','(',')']
    password_letter=[random.choice(letter) for _ in range(random.randint(8,10))]
    password_number=[random.choice(number) for _ in range(random.randint(2,4))]
    password_symbol=[random.choice(symbols) for _ in range(random.randint(2,4))]
    password_list=password_letter+password_number+password_symbol
    random.shuffle(password_list)
    password="".join(password_list)
    pass_entry.insert(0,password)
    pyperclip.copy(password)

#---------------------------------------------------SAVE PASSWORD------------------------------------------------
def save():
    website=web_entry.get()
    password=pass_entry.get()
    email=email_entry.get()
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="ERROR",message=f"PLEASE DON'T LEAVE ANY FIELD EMPTY HERE")
    else:
        is_ok=messagebox.askokcancel(title=website ,message=f"These are the details entered\nEmail:{email}\nPassword:{password}\n is it OK TO SAVE")
        if is_ok:
            with open("passfile.txt","a") as passfile:
                passfile.write(f"{website} ---> {email} ---> {password}\n")
                web_entry.delete(0,END)
                pass_entry.delete(0,END)


#-----------------------------------------------------UI SETUP----------------------------------------------------
window=Tk()
window.title("WELCOME TO PASSWORD MANAGER")
window.config(bg="grey")
canvas=Canvas(height=200,width=500,bg="sky blue")
passimg = PhotoImage(file="pass.png")
canvas.create_image(150,100,image=passimg)
canvas.create_text(350, 100, text=f"WELCOME!\nto PASSWORD MANAGER", fill="black", font=('Helvetica 15 bold'))
canvas.grid(pady=(0,0),row=0,column=0,columnspan=3)
canvas.config(highlightthickness=0)
web=Label(text="Website",bg="grey")
web.grid(row=1,column=0)
email=Label(text="Email/Username",bg="grey")
email.grid(row=2,column=0)
password=Label(text="Password",bg="grey")
password.grid(row=3,column=0)




# ENTRIES
web_entry=Entry(width=67,bg="grey")
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()
email_entry=Entry(width=67,bg="grey")
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"PLEASE ENTER YOUR EMAIL HERE")
pass_entry=Entry(width=48,bg="grey")
pass_entry.grid(row=3,column=1)

#Button

generate_Button=Button(text="Create Password",bg="red",fg="white",width=14,command=createpass)
generate_Button.grid(row=3,column=2)
add_Button=Button(text="ADD THIS ENTRY IN YOUR FILE",bg="blue",fg="yellow",width=36,command=save)
add_Button.grid(row=4,column=1,columnspan=2,pady=(0,30))



window.mainloop()
