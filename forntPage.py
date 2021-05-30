from results import create_contentBase_recommendations
from tkinter import *
#from PIL import ImageTk
from tkinter import messagebox
from numpy import insert
import pymysql
import os
import csv
import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel

root = Tk()

class profile_page:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")    
        self.root.geometry("980x651+180+10")
        self.root.resizable(False, False)
        

        

         # background Image
        self.bg = PhotoImage(file='C:\\Users\\IA\\Pictures\\profile_page.png')
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #create navigation bar
        frame_navigationBar = Frame(self.root, bg='#d0c1aa')
        frame_navigationBar.place(x=0, y=20, width=980, height= 35)

        #buttons on navigation bar
        #home button
        self.home_button = Button(self.root, command= self.profile_shown, text='Home', bd=0, bg= '#d0c1aa', cursor= 'hand2' ,fg= '#61331c', activebackground='#d0c1aa', font=('times new roman',15)).place(x=30, y=20, width=80, height=35)

        #My shelf button
        self.myBook_button = Button(self.root, command= self.jump_to_home, text='My Shelf', bd=0, bg= '#d0c1aa', cursor= 'hand2' ,fg= '#61331c', activebackground='#d0c1aa', font=('times new roman',15)).place(x=107, y=20, width=80, height=35)

        #My search button
        self.search_button = Button(self.root, command= self.search_function, text='Search', bd=0, bg= '#d0c1aa', cursor= 'hand2' ,fg= '#61331c', activebackground='#d0c1aa', font=('times new roman',15)).place(x=190, y=20, width=80, height=35)

        #My logout button
        self.logout_button = Button(self.root, command= self.signOut, text='Sign Out', bd=0, bg= '#d0c1aa', cursor= 'hand2' ,fg= '#61331c', activebackground='#d0c1aa', font=('times new roman',15)).place(x=880, y=20, width=80, height=35)

        
    def jump_to_home(self):
        pass

    def profile_shown(self):
       # frame for my profile
        frame_profile = Frame(self.root, bg='#eacf8e')
        frame_profile.place(x=340, y=180, width=485, height= 330,)

        #register here label
        profile_label = Label(frame_profile, text='My Profile', font=('Impact',35, 'bold'), bg= '#eacf8e', fg= '#61331c')
        profile_label.place(x=20, y= 5)

        #label and textfeild name
        name_label = Label(frame_profile, text='Name', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 30, y=70)
        self.name_textfield = Entry(frame_profile, font=('times new roman',15), bg='lightgrey')
        self.name_textfield.place(x= 30, y=100, width= 190, height= 35)

        #label and textfield for email
        email_label = Label(frame_profile, text='Email', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 30, y=140)
        self.email_textfield = Entry(frame_profile, font=('times new roman',15), bg='lightgrey')
        self.email_textfield.place(x= 30, y=170, width= 190, height= 35)

        #label and textfield for password
        password_label = Label(frame_profile, text='Password', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 30, y=210)
        self.password_textfield = Entry(frame_profile, font=('times new roman',15), bg='lightgrey')
        self.password_textfield.place(x= 30, y=240, width= 190, height= 35)

        #label and textfeild username
        username_label = Label(frame_profile, text='Username', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 265, y=70)
        self.username_textfield = Entry(frame_profile, font=('times new roman',15), bg='lightgrey')
        self.username_textfield.place(x= 265, y=100, width= 190, height= 35)

        #label and textfield for contactNo
        contactNo_label = Label(frame_profile, text='Contact No', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 265, y=140)
        self.contactNo_textfield = Entry(frame_profile, font=('times new roman',15), bg='lightgrey')
        self.contactNo_textfield.place(x= 265, y=170, width= 190, height= 35)

        #label and textfield for confirm password
        cnfrmpassword_label = Label(frame_profile, text='Perfered Genre', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 265, y=210)
        self.cnfrmpassword_textfield = Entry(frame_profile,font=('times new roman',15), bg='lightgrey', show='')
        self.cnfrmpassword_textfield.place(x= 265, y=240, width= 190, height= 35)

        #Update button
        register_btn = Button(self.root, command= self.jump_to_home, cursor='hand2', text='Update', bd=0, bg= '#61331c', fg= '#eacf8e', activebackground='#61331c', font=('times new roman',20)).place(x=500, y=490, width=180, height=40)

    def search_function(self):
        # frame for my search
        self.frame_search = Frame(self.root, bg='#eacf8e')
        self.frame_search.place(x=340, y=120, width=550, height= 450,)

        #register here label
        searchBook_label = Label(self.frame_search , text='Search Books', font=('Impact',35, 'bold'), bg= '#eacf8e', fg= '#61331c')
        searchBook_label.place(x=20, y= 5)

        #label and textfeild name
        name_label = Label(self.frame_search , text='Enter Book Name', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 30, y=70)
        self.bookName_textfield = Entry(self.frame_search , font=('times new roman',15), bg='#eacf8e')
        self.bookName_textfield.place(x= 30, y=100, width= 350, height= 35)

        self.search_book_label = Label(self.frame_search , text='', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 30, y=140)

        #search button
        self.search_btn = Button(self.frame_search , command= self.serach_btn_function, cursor='hand2', text='Search', bd=0, bg= '#eacf8e', fg= '#61331c', activebackground='#61331c', font=('times new roman',18))
        self.search_btn.place(x=380, y=100, width=100, height=35)

  
        #method create content-base recommendations
    def serach_btn_function(self):
        self.book_list = Listbox(self.frame_search,font=('times new roman',15),  bg='#eacf8e').place( x= 30, y= 150, height = 120, width= 350)
        create_contentBase_recommendations(self.bookName_textfield.get())

    def signOut(self):
        root.destroy()
        os.system('python login.py')

obj = profile_page(root)
root.mainloop()