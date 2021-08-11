from tkinter import *

def save_info():
    first_name_info = firstname.get()
    last_name_info = lastname.get()
    age_info = age.get()

    print(first_name_info,last_name_info,age_info)

    file = open("user.txt","w")

    file.write("Your First name :" + first_name_info)
    file.write("\n")
    file.write("Your last name :" + last_name_info)
    file.write("\n")
    file.write("Your age :" + str(age_info))

    file.close()

app = Tk()

app.geometry("600x600")

app.title("pythtn form GUI")


heading = Label(text="pythtn form GUI",bg="yellow",fg="black",font="10",width="500",height="3")

heading.pack()

firstname_text = Label(text="firstname :")
lastname_text = Label(text="lastname :")
age_text = Label(text="Age :")

firstname_text.place(x=15, y=70)
lastname_text.place(x=15 , y=140)
age_text.place(x=15, y=210)

firstname = StringVar()
lastname = StringVar()
age = IntVar()

first_name_entry = Entry(textvariable=firstname,width="30")
last_name_entry = Entry(textvariable=lastname,width="30")
age_entry = Entry(textvariable=age,width="30")

first_name_entry.place(x=15, y=100)
last_name_entry.place(x=15, y=180)
age_entry.place(x=15, y=240)

button = Button(app, text="Submit", command=save_info, width="30",bg="grey",height="2")

button.place(x=15,y=290)
mainloop()