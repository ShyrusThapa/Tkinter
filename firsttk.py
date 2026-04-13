from tkinter import *
sc= Tk()
sc.title("Shyrus")
sc.geometry("500x500")
#Labeling
Label(sc,text="Registration Form",font="white,ariel,bold,20",bg="black").pack(fill="both")

#Details
Label(sc,text="Name",font="white").place(x=30,y=40)
Label(sc,text="Age",font="white").place(x=30,y=80)
Label(sc,text="Phone",font="white").place(x=30,y=120)
Label(sc,text="Email",font="white").place(x=30,y=160)

#Entry box 
name_entry=Entry(sc,font=10,bd=3)
name_entry.place(x=100,y=40)

age_entry=Entry(sc,font="white",bd=3)
age_entry.place(x=100,y=80)

phone_entry=Entry(sc,font="white",bd=3)
phone_entry.place(x=100,y=120)

email_entry=Entry(sc,font="white",bd=3)
email_entry.place(x=100,y=160)

mainloop()