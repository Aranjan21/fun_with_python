#!/usr/bin/env python3
import psycopg2
from tkinter import *
import tkinter as tk
''' This code defines the the connection to postgres db running in local
    installed with brew utility. We will use tkinter to submit data
    in the backend pg server '''

#Initialise the tkinter object

root = Tk()

#Define the function to store data in db
def get_data(name,age,address,phnum):
    connection = psycopg2.connect(dbname='postgres', user='testuser')
    cursor = connection.cursor()
    query = ('''insert into students (name,age,address,number) values (%s,%s,%s,%s);''')
    cursor.execute(query,(name,age,address,phnum))
    print('Data inserted for student: ')
    connection.commit()
    connection.close()

# Create canvass using tkinter
canvas = Canvas(root,height=480,width=900)
canvas.pack()

#Layout the frame on top of the canvas
frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)

# Add labels grid layout system
label = Label(frame,text="Add your Data")
label.grid(row=0,column=1)

# Create label for name of students
label = Label(frame,text="Name of Student")
label.grid(row=1,column=0)

entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

# Create label for age of student
label = Label(frame,text="Age of Student")
label.grid(row=2,column=0)

entry_age = Entry(frame)
entry_age.grid(row=2,column=1)

#Create label for Address of Student

label = Label(frame,text="Address")
label.grid(row=3,column=0)

entry_address = Entry(frame)
entry_address.grid(row=3,column=1)

#Create label for phone number
label = Label(frame,text="Phone Number")
label.grid(row=4,column=0)

entry_phnum = Entry(frame)
entry_phnum.grid(row=4,column=1)

#Create submit button
button = Button(frame,text="Submit",command=lambda:get_data(entry_name.get(),entry_age.get(),entry_address.get(),entry_phnum.get()))
button.grid(row=5,column=1)


# This function will create table students in pg server along with schemas

def create_table():
    connection = psycopg2.connect(dbname='postgres',user='testuser')
    cursor = connection.cursor()
    query = 'create table students(ID serial ,name text,address text,age int ,number int);'
    cursor.execute(query)
    print("Table Created")
    connection.commit()
    connection.close()

def insert_data():
    connection = psycopg2.connect(dbname='postgres', user='testuser')
    cursor = connection.cursor()
    print('Enter five studenst details here: ')
    for i in range(5):
        name = input('Enter name of student{}: '.format(i))
        age = input('Enter his/her age: ')
        address = input('Enter address: ')
        number = input('Enter tele-phone Number: ')
        query = ('''insert into students (name,age,address,number) values (%s,%s,%s,%s);''')
        cursor.execute(query,(name,age,address,number))
        print('Data inserted for student{} .'.format(i))
    connection.commit()
    connection.close()


root.mainloop()
#insert_data()
#create_table()
