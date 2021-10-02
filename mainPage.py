import abc
import io
from typing import List
from results import create_contentBase_recommendations
from tkinter import *
import PyPDF2
from tkPDFViewer import tkPDFViewer as pdf 
import tkinter as tk
from tkinter import ttk
from io import BytesIO
from PIL import ImageTk, Image
from tkinter import messagebox
from numpy import double, float16, insert, log
import pymysql
import os
import pandas as pd
#import csv
from results import create_contentBase_recommendations
#from subprocess import call
import login
#import login_username_textfield
#import global_variables

root = Tk()

user_id = StringVar()
user_name = StringVar()
user_email = StringVar()
user_contactNo = StringVar()
user_password = StringVar()
user_username = StringVar()
user_prefered_genre = StringVar()
login_user_id = StringVar()
recommend_prefered_genre = StringVar()

book_id= IntVar()
book_Name = StringVar()
author_Name = StringVar()
book_Pages = StringVar()
book_Genre= StringVar()
book_Description = StringVar()
book_Rating = DoubleVar()
book_pdf_link = StringVar()
rating_point = 0
#user_Name = StringVar()


class profile_page:
    def __init__(self, root):
        self.root = root
        self.root.title("Happy Reading")    
        self.root.geometry("980x651+180+10")
        self.root.resizable(False, False)
        #self.root.iconify()
        #self.user_name = login.user_name
        #print(login_username_textfield)
        #login id = new login()

        #user id textfield
        self.login_user_id_textfield= Entry(self.root, font=('times new roman',11), textvariable=login_user_id)
        self.login_user_id_textfield.place(x= 30, y=150, width= 90, height= 20)
        #self.login_user_id_textfield.place_forget()
        
        #print(str(login.login_username_textfield.get()))

        #set the username of the logged in user
        login_user_id.set(str('2'))

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
        self.myBooks_button = Button(self.root, command= self.show_my_book_shelf, text='My Shelf', bd=0, bg= '#d0c1aa', cursor= 'hand2' ,fg= '#61331c', activebackground='#d0c1aa', font=('times new roman',15)).place(x=107, y=20, width=80, height=35)

        #My search button
        self.search_button = Button(self.root, command= self.search_function, text='Search', bd=0, bg= '#d0c1aa', cursor= 'hand2' ,fg= '#61331c', activebackground='#d0c1aa', font=('times new roman',15)).place(x=190, y=20, width=80, height=35)

        #My recomendations button
        self.search_button = Button(self.root, command= self.show_recomendations, text='Recommendations', bd=0, bg= '#d0c1aa', cursor= 'hand2' ,fg= '#61331c', activebackground='#d0c1aa', font=('times new roman',15)).place(x=280, y=20, width=145, height=35)

        #Find friends  button
        self.search_button = Button(self.root, command= self.search_function, text='Friends', bd=0, bg= '#d0c1aa', cursor= 'hand2' ,fg= '#61331c', activebackground='#d0c1aa', font=('times new roman',15)).place(x=430, y=20, width=80, height=35)


        #My logout button
        self.logout_button = Button(self.root, command= self.signOut, text='Sign Out', bd=0, bg= '#d0c1aa', cursor= 'hand2' ,fg= '#61331c', activebackground='#d0c1aa', font=('times new roman',15)).place(x=880, y=20, width=80, height=35)

        #frame for my profile
        self.frame_profile = Frame(self.root, bg='#eacf8e')

        # frame for My Shelf and pdf viewer
        self.frame_my_shelf = Frame(self.root, bg='#eacf8e')
        self.book_reviews = Frame(self.root, bg='#eacf8e')

        # frame for search book
        self.frame_search = Frame(self.root, bg='#eacf8e')

        # frame for search book
        self.frame_recommendations = Frame(self.root, bg='#eacf8e')


        #label and textfield for contactNo
        self.contactNo_label = Label(self.frame_profile, text='Contact No', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c')
        self.contactNo_textfield = Entry(self.frame_profile, font=('times new roman',15), bg='lightgrey', textvariable=user_contactNo)

        #label and textfield for email
        self.email_label = Label(self.frame_profile, text='Email', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c')
        self.email_textfield = Entry(self.frame_profile, font=('times new roman',15), bg='lightgrey', textvariable= user_email)
        
        #label and textfield for password
        self.password_label = Label(self.frame_profile, text='Password', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c')
        self.password_textfield = Entry(self.frame_profile, font=('times new roman',15), bg='lightgrey', textvariable= user_password)

        #label and textfield for prefered genre
        self.prefered_genre_label = Label(self.frame_profile, text='Perfered Genre', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c')
        self.prefered_genre_textfield = Entry(self.frame_profile,font=('times new roman',15), bg='lightgrey', textvariable=user_prefered_genre)
        

    def profile_shown(self):

        #login.login_function()

        #disapper other frames
        self.frame_search.place_forget()
        self.frame_my_shelf.place_forget()
        self.frame_recommendations.place_forget()

        #frame for my profile placement
        self.frame_profile.place(x=340, y=180, width=485, height= 370,)

        #register here label
        profile_label = Label(self.frame_profile, text='My Profile', font=('Impact',35, 'bold'), bg= '#eacf8e', fg= '#61331c')
        profile_label.place(x=20, y= 5)


        #print(login.login_username_textfield)

        #label and textfeild name
        name_label = Label(self.frame_profile, text='Name', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 30, y=70)
        self.name_textfield = Entry(self.frame_profile, font=('times new roman',15), bg='lightgrey', textvariable= user_name )
        self.name_textfield.place(x= 30, y=100, width= 190, height= 35)

        #label and textfield for email
        self.email_label.place(x= 30, y=140)
        self.email_textfield.place(x= 30, y=170, width= 190, height= 35)

        #label and textfield for password
        self.password_label.place(x= 30, y=210)
        self.password_textfield.place(x= 30, y=240, width= 190, height= 35)

        #label and textfeild username
        self.username_label = Label(self.frame_profile, text='Username', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 265, y=70)
        self.username_textfield = Entry(self.frame_profile, font=('times new roman',15), bg='lightgrey', textvariable=user_username)
        self.username_textfield.place(x= 265, y=100, width= 190, height= 35)

        #label and textfield for contactNo
        self.contactNo_label.place(x= 265, y=140)
        self.contactNo_textfield.place(x= 265, y=170, width= 190, height= 35)

        #label and textfield for user prefered password
        self.prefered_genre_label.place(x= 265, y=210)
        self.prefered_genre_textfield.place(x= 265, y=240, width= 190, height= 35)

        #Update button
        self.register_btn = Button(self.frame_profile, command= self.setPassword, cursor='hand2', text='Update', bd=0, bg= '#61331c', fg= '#eacf8e', activebackground='#61331c', font=('times new roman',20))
        self.register_btn.place(x=150, y=310, width=180, height=40)

        try:
                conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
                cursor = conn.cursor()
                cursor.execute("select * from user where user_id=%s", (self.login_user_id_textfield.get()))
                row = cursor.fetchall()
                if row != None:
                    for tup in row:
                        #user_id.set(login.login_username_textfield.get())
                        user_name.set(str(tup[1]))
                        user_username.set(str(tup[2]))
                        user_email.set(str(tup[3]))
                        user_contactNo.set(str(tup[4]))
                        user_password.set(str(tup[5]))
                        user_prefered_genre.set(str(tup[6]))
                            
                    conn.commit()
                    conn.close()
                    #root.destroy()
                    #os.system('python forntPage.py')
        except Exception as excpt:
            messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)


    def setPassword(self):
        try:
            conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
            cursor = conn.cursor()
            cursor.execute("UPDATE user SET user_email=%s, user_contactNo=%s, user_password=%s, prefered_genre=%s WHERE user_id=%s", 
            (self.email_textfield.get(), self.contactNo_textfield.get(), self.password_textfield.get(),self.prefered_genre_textfield.get(),login_user_id.get()))
            row = cursor.fetchall()
            if row == None:
                messagebox.showerror("Error", "Invalid username", parent = self.root)
            else:
                messagebox.showinfo("Data Updated", f"{self.username_textfield.get()} , Your data has been updated", parent = self.root)
        
                conn.commit()
                conn.close()
                #root.destroy()
                #os.system('python login.py')
        except Exception as excpt:
            messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)

    
    def show_my_book_shelf(self):
        
        #disapper other frames
        self.frame_profile.place_forget()
        self.frame_search.place_forget()
        self.frame_recommendations.place_forget()

        # frame for my search  placement
        self.frame_my_shelf.place(x=340, y=120, width=550, height= 470,)

        #My shelf label
        self.my_shelf_label = Label(self.frame_my_shelf, text='My Shelf', font=('Impact',35, 'bold'), bg= '#eacf8e', fg= '#61331c')
        self.my_shelf_label.place(x=20, y= 5)

        #label 
        my_shelf_second_label = Label(self.frame_my_shelf , text='The Books Added To My Shelf Are', font=('Goudy old style', 17, 'bold'), bg= '#eacf8e', fg= '#61331c')
        my_shelf_second_label.place(x= 25, y=80)
        

        #frame for the display table
        self.my_shelf_display_frame = Frame(self.frame_my_shelf, bg='#eacf8e')
        self.my_shelf_display_frame.place(x= 25,y = 130, width= 500, height=320)

        #treeview row select row
        #self.tree_row_frame = Frame(self.my_shelf_display_frame, bg = '#eacf8e', highlightbackground="#61331c", highlightthickness=5)

        #treeview
        self.tree = ttk.Treeview(self.my_shelf_display_frame)
        

        #Treeview for the books added into the table
        try:
            conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
            cursor = conn.cursor()
            #cursor.execute("select * from book_in_shelf")
            cursor.execute("select * from books, book_in_shelf where books.book_id = book_in_shelf.book_id")
        

            self.tree.place(width=500, height=320)
            #tree['show'] = ['headings']

            self.shelf_sytle = ttk.Style(self.my_shelf_display_frame)
            self.shelf_sytle.theme_use("clam")
            self.shelf_sytle.configure(".", foreground= '#61331c', font=('times new roman', 12))
            self.shelf_sytle.configure("Treeview.Heading", foreground= '#61331c', font= ('Goudy old style', 15, "bold"))
            self.shelf_sytle.configure("Treeview", rowheight= 135)

            #tree columns are 
            self.tree["columns"] = (#"book_cover", 
            "book_title", "book_author", "user_rating", "user_feedback")

            #designing the columns
            self.tree.column("#0", width=130, stretch='NO')
            self.tree.column("book_title", width=130, anchor=tk.CENTER)
            self.tree.column("book_author", width=130, anchor=tk.CENTER)
            self.tree.column("user_rating", width=150, anchor=tk.CENTER)
            self.tree.column("user_feedback", width=135, anchor=tk.CENTER)

            #heading of the columns
            self.tree.heading("#0", text= "Book Cover", anchor=tk.CENTER)
            self.tree.heading("book_title", text= "Book Title", anchor=tk.CENTER)
            self.tree.heading("book_author", text= "Book Author", anchor=tk.CENTER)
            self.tree.heading("user_rating", text= "No. Of Pages", anchor=tk.CENTER)
            self.tree.heading("user_feedback", text= "Boo Genre", anchor=tk.CENTER)

            i = 0
            self.tree.imglist = []
            for tup in cursor:
                a = tup[1]
                b = tup[2]
                c = tup[3]
                d = tup[5]
                global _img
                _img = Image.open(io.BytesIO(tup[7]))
                _img.thumbnail((100,130))
                _img = ImageTk.PhotoImage(_img)
                
                l2 = tk.Label(self.my_shelf_display_frame,image=_img)
                #l2.place(x= 12, y= 15)
                #print(l2)
                self.tree.insert(parent="", index="end", iid=i, 
                image=_img, 
                values=(a, b, c, d) )
                self.tree.imglist.append(_img)
                i += 1
            
            #horizontal scrollbar for the diplay table
            horizontal_scroll_bar = ttk.Scrollbar(self.my_shelf_display_frame, orient="horizontal")
            horizontal_scroll_bar.configure(command=self.tree.xview)
            self.tree.configure(xscrollcommand=horizontal_scroll_bar.set)
            horizontal_scroll_bar.pack(fill=X, side=BOTTOM)
            

            #vertical scrollbar for display table
            vertical_scroll_bar = ttk.Scrollbar(self.my_shelf_display_frame, orient="vertical")
            vertical_scroll_bar.configure(command=self.tree.yview)
            self.tree.configure(yscrollcommand=vertical_scroll_bar.set)
            vertical_scroll_bar.pack(fill=Y, side=RIGHT)
            
            conn.commit()
            conn.close()
        except Exception as excpt:
            messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)
    
        #treeview binding
        def tree_row_clicked(e):
            global tree_row_frame
            tree_row_frame = Frame(self.my_shelf_display_frame, bg = '#eacf8e', highlightbackground="#61331c", highlightthickness=5)
            tree_row_frame.place(x= 100,y = 60, width= 350, height=220)

            #back buttton
            close_btn = Button(tree_row_frame, command= self.exit_selected_row_frame, cursor='hand2', text='x', bd= 0, bg= '#eacf8e', fg= '#61331c', activebackground= '#eacf8e', font=('Goudy old style',20))
            close_btn.place(x=310, y=7, width=20, height=20)


            #book title
            global book_title
            book_title = Entry(tree_row_frame,  bg= '#eacf8e', bd=0, fg= '#61331c', font=('times new roman',11), justify= 'center')
            book_title.place(x= 15, y= 160, height = 25, width= 100)

            #open the book button
            open_book_btn = Button(tree_row_frame, command= self.open_book, cursor='hand2', text='Want To Read', bd= 0, fg= '#eacf8e', bg= '#61331c', activebackground= '#eacf8e', font=('times new roman',13))
            open_book_btn.place(x=150, y=40, width=145, height=30)

            #remove the book from my shelf button
            remove_book_btn = Button(tree_row_frame, command= self.remove_book, cursor='hand2', text='Remove From Shelf', bd= 0, fg= '#eacf8e', bg= '#61331c', activebackground= '#eacf8e', font=('times new roman',13))
            remove_book_btn.place(x=150, y=90, width=145, height=30)

            #review the book button
            review_book_btn = Button(tree_row_frame, command= self.reviews_of_book, cursor='hand2', text='Reviews', bd= 0, fg= '#eacf8e', bg= '#61331c', activebackground= '#eacf8e', font=('times new roman',13))
            review_book_btn.place(x=150, y=140, width=145, height=30)

            #treeview row selected
            selected = self.tree.focus()
            value = self.tree.item(selected, 'values')
            global author
            author = value[1]
            #print(author)
            picture = self.tree.item(selected, 'image')
            book_title.insert(INSERT, value[0])
            #print(book_title.get())

            #book cover
            book_cover = Label(tree_row_frame, image=picture)
            book_cover.place(x= 20, y= 20, height = 132, width= 90)

        #tree binding
        self.tree.bind("<Double-1>", tree_row_clicked)
    
    def open_book(self):
        try:
            conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE book_name=%s",(book_title.get()))
            row = cursor.fetchall()
            for tup in row:
                os.startfile(str(tup[6]))
            

            conn.commit()
            conn.close()
            
        except Exception as excpt:
            messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)

    def reviews_of_book(self):
        # disapper other frames
        #self.frame_my_shelf.place_forget()

        # frame for my search  placement
        self.book_reviews.place(x=340, y=90, width=550, height= 540)

        #back buttton
        self.close_btn = Button(self.book_reviews, command= self.exit_book_views_frame, cursor='hand2', text='x', bd= 0, bg= '#eacf8e', fg= '#61331c', activebackground= '#eacf8e', font=('Goudy old style',20))
        self.close_btn.place(x=520, y=7, width=20, height=20)

        #Pdf book title label
        self.reviews_of_book_title = Label(self.book_reviews, text= book_title.get(), font=('Impact',30, 'bold'), bg= '#eacf8e', fg= '#61331c')
        self.reviews_of_book_title.place(x=20, y= 5)

        # #pdf book link
        # self.book_pdf_link = Entry(self.book_reviews, textvariable=book_pdf_link)
        # self.book_pdf_link.place(x= 230, y=55, width=270)
        # self.book_pdf_link.place_forget()

        #Pdf book author label 
        self.reviews_book_author = Label(self.book_reviews, text=str(author), font=('Goudy old style', 13, 'bold'), bg= '#eacf8e', fg= '#61331c')
        self.reviews_book_author.place(x= 30, y=55)

        #side border for the review fields
        self.book_reviews_border_frame = Frame(self.book_reviews, bg='#61331c')
        self.book_reviews_border_frame.place(x=30, y=90, width=490, height= 180)

        #Pdf book display frame
        self.book_reviews_display_frame = Frame(self.book_reviews, bg='#eacf8e')
        self.book_reviews_display_frame.place(x=35, y=90, width=490, height= 180)

        #label and textfeild name
        self.user_name_label = Label(self.book_reviews_display_frame , text=self.username_textfield.get(), font=('Goudy old style', 20, 'bold'), bg= '#eacf8e', fg= '#61331c')
        self.user_name_label.place(x= 15, y=3)

        #rating textfield
        
        self.rating_textfield = Label(self.book_reviews_display_frame, text=rating_point, justify='center', font=('times new roman',15), bg='#eacf8e')
        self.rating_textfield.place(x= 370, y= 65, width= 30)
        self.rating_star_label = Label(self.book_reviews_display_frame , text='Star', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c')
        self.rating_star_label.place(x= 405, y=63)

        #label
        self.add_a_review_label = Label(self.book_reviews_display_frame , text='Add A Public Feedback', font=('Goudy old style', 13, 'bold'), bg= '#eacf8e', fg= '#61331c')
        self.add_a_review_label.place(x= 30, y=45)
        
        self.feedback_textfield = Text(self.book_reviews_display_frame, font=('times new roman',15), bg='#eacf8e')
        self.feedback_textfield.place(x= 30, y=85, width= 280, height= 80)

        #add and subtract buttons
        self.plus_one_btn = Button(self.book_reviews_display_frame, command= self.plus_one_point, cursor='hand2', text='+',justify='center', bd= 0, fg= '#eacf8e', bg= '#61331c', activebackground= '#eacf8e', font=('times new roman',12,'bold'))
        self.plus_one_btn.place(x=335, y=65, width=25, height=25)
        self.minus_one_btn = Button(self.book_reviews_display_frame, command= self.minus_one_point, cursor='hand2', text='-',justify='center', bd= 0, fg= '#eacf8e', bg= '#61331c', activebackground= '#eacf8e', font=('times new roman',12,'bold'))
        self.minus_one_btn.place(x=448, y=65, width=25, height=25)

        #submit button
        self.submit_btn = Button(self.book_reviews_display_frame  , command= self.submit_review, cursor='hand2', text='Submit', bd= 0, fg= '#eacf8e', bg= '#61331c', activebackground= '#eacf8e', font=('times new roman',15,'bold'))
        self.submit_btn.place(x=370, y=140, width=80, height=30)

        #show all feedbacks of the selected book

        #Users' feedback
        self.all_user_feedback = Label(self.book_reviews, text= 'User Feedback', font=('Impact',23, 'bold'), bg= '#eacf8e', fg= '#61331c')
        self.all_user_feedback.place(x=40, y= 280)
        

        #frame for the display feedback
        self.user_feedback_display_frame = Frame(self.book_reviews, bg='#eacf8e')
        self.user_feedback_display_frame.place(x= 45,y = 330, width= 470, height=180)

        #treeview for user feedback
        self.feedback_tree = ttk.Treeview(self.user_feedback_display_frame)
        
        #Treeview for the books added into the table
        try:
            conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
            cursor = conn.cursor()
            #cursor.execute("select * from book_in_shelf")
            cursor.execute("SELECT * FROM books, book_review, user WHERE book_review.book_id = books.book_id AND book_review.user_id = user.user_id AND books.book_name=%s",(book_title.get()))
            print(book_title.get())
            #cursor.execute("SELECT user.user_username from user,book_review WHERE book_review.user_id = user.user_id")
            #row1 = cursor.fetchone()
            #row = cursor.fetchall()
            #AND books.book_name=%s", (book_title.get())
            

            self.feedback_tree.place(width=458, height=180)
            self.feedback_tree['show'] = ['headings']

            self.feedback_tree_sytle = ttk.Style(self.user_feedback_display_frame)
            self.feedback_tree_sytle.theme_use("clam")
            self.feedback_tree_sytle.configure(".", foreground= '#61331c', font=('times new roman', 12))
            self.feedback_tree_sytle.configure("Treeview.Heading", foreground= '#61331c', font= ('Goudy old style', 15, "bold"))
            self.feedback_tree_sytle.configure("Treeview", rowheight= 30)

            #tree columns are 
            self.feedback_tree["columns"] = ("username", "user_rating", "user_feedback")

            #designing the columns
            self.feedback_tree.column("username", width=10, anchor=tk.CENTER)
            self.feedback_tree.column("user_rating", width=10, anchor=tk.CENTER)
            self.feedback_tree.column("user_feedback", width=250, anchor=tk.W)

            #heading of the columns
            self.feedback_tree.heading("username", text= "User", anchor=tk.CENTER)
            self.feedback_tree.heading("user_rating", text= "Rating", anchor=tk.CENTER)
            self.feedback_tree.heading("user_feedback", text= "Feedback", anchor=tk.CENTER)

            _i = 0
            #self.tree.imglist = []
            for tup in cursor:
                # a = tup[1]
                # b = tup[2]
                # c = tup[3]
                # d = tup[5]
                # g = tup[10]
                h = tup[11]
                i = tup[12]
                # j = tup[13]
                # k = tup[14]
                l = tup[15]
                print(str(h)) # feedback
                print(str(i)) # user_rating
                print(str(l)) # user_username
                
                self.feedback_tree.insert(parent="", index="end", iid=_i, values=(l, i, h) )
                _i += 1
            
            #vertical scrollbar for display table
            vertical_scroll_bar = ttk.Scrollbar(self.user_feedback_display_frame, orient="vertical")
            vertical_scroll_bar.configure(command=self.feedback_tree.yview)
            self.feedback_tree.configure(yscrollcommand=vertical_scroll_bar.set)
            vertical_scroll_bar.pack(fill=Y, side=RIGHT)
            
            conn.commit()
            conn.close()
        except Exception as excpt:
            messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)
    
    def open_book(self):
        try:
            conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books WHERE book_name=%s",(book_title.get()))
            row = cursor.fetchall()
            for tup in row:
                os.startfile(str(tup[6]))
            

            conn.commit()
            conn.close()
            
        except Exception as excpt:
            messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)


    def submit_review(self):
        try:
            global rating_point
            MsgBox = messagebox.askquestion ('Confirmation',f'Are you sure you want to submit "{self.rating_textfield.cget("text")}" this rating',icon = 'warning')
            if MsgBox == 'yes':
                conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
                cursor = conn.cursor()
                cursor.execute("SELECT book_id FROM books WHERE book_name=%s",(book_title.get()))
                row = cursor.fetchone()
                print(row)
                print(login_user_id.get())
                print(self.rating_textfield.cget("text"))
                #rating = (self.rating_textfield.cget("text"))
                print(self.feedback_textfield.get("1.0",END))
                cursor.execute("insert into book_review (book_id, user_id, book_review_feedback, book_review_rating) values (%s, %s, %s, %s)",
                (
                    row,
                    #login_user_id.get(),
                    "8",
                    self.feedback_textfield.get("1.0",END),
                    self.rating_textfield.cget("text")
                ))
                messagebox.showinfo("Submitted Successfully", f'{self.username_textfield.get()}, thank you for your review.', parent = self.root)
                self.feedback_textfield.delete(0, END)
                rating_point = 0
            else:
                #do nothing
                pass
            conn.commit()
            conn.close()
            
        except Exception as excpt:
            messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)
   

    def plus_one_point(self):
        global rating_point
        if(rating_point > 4):
            rating_point = 5
            self.rating_textfield.config(text=rating_point)
        else:
            rating_point +=1
            self.rating_textfield.config(text=rating_point)
            

    def minus_one_point(self):
        global rating_point
        if(rating_point < 1):
            rating_point = 0
            self.rating_textfield.config(text=rating_point)
        else:    
            rating_point -=1
            self.rating_textfield.config(text=rating_point) 
            

    def exit_selected_row_frame(self):
        tree_row_frame.place_forget()
        book_title.delete(0, END)

    def exit_book_views_frame(self):
        global rating_point
        self.book_reviews.place_forget()
        self.shelf_sytle.configure("Treeview", rowheight= 135)
        self.reviews_of_book_title.config(text="")
        self.reviews_book_author.config(text="")
        rating_point = 0


    def remove_book(self):
        MsgBox = messagebox.askquestion ('Remove Book',f'Are you sure you want to remove "{book_title.get()}" from your shelf?',icon = 'warning')
        if MsgBox == 'yes':
            _x = self.tree.selection()[0]
            print(book_title.get())
            try:
                conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
                cursor = conn.cursor()
                print(cursor.execute("SELECT book_id FROM books WHERE book_name=%s",(book_title.get())))
                row = cursor.fetchone()
                print(row)
                cursor.execute("DELETE FROM book_in_shelf WHERE book_id=%s", (row))
                self.tree.delete(_x)
                messagebox.showinfo("Removed", f'"{book_title.get()}", has been removed from your shelf', parent = self.root)
                tree_row_frame.place_forget()

                conn.commit()
                conn.close()
                
            except Exception as excpt:
                messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)

        else:
            #Do nothing
            pass
        



    def search_function(self):
        #search list
        self.search_book_list = Listbox(self.frame_search, bg = '#61331c')
        self.search_book_list.pack()

        #disapper other frames
        self.frame_profile.place_forget()
        self.frame_my_shelf.place_forget()
        self.frame_recommendations.place_forget()
        self.search_book_list.pack_forget()

        # frame for my search  placement
        self.frame_search.place(x=340, y=120, width=550, height= 470,)

        #Search books label
        searchBook_label = Label(self.frame_search , text='Search Books', font=('Impact',35, 'bold'), bg= '#eacf8e', fg= '#61331c')
        searchBook_label.place(x=20, y= 5)

        #label and textfeild name
        name_label = Label(self.frame_search , text='Enter Book Name', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 30, y=70)
        self.bookName_textfield = Entry(self.frame_search , font=('times new roman',15), bg='#eacf8e')
        self.bookName_textfield.place(x= 30, y=100, width= 390, height= 35)

        self.search_book_label = Label(self.frame_search , text='', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 30, y=140)
        
        #search button
        self.search_btn = Button(self.frame_search , command= self.serach_btn_function, cursor='hand2', text='Search', bd=0, bg= '#eacf8e', fg= '#61331c', activebackground='#61331c', font=('times new roman',18))
        self.search_btn.place(x=420, y=100, width=100, height=35)

  
        #method create content-base recommendations
    def serach_btn_function(self):
        
        #self.book_list = Listbox(self.frame_search,font=('times new roman',15),  bg='#eacf8e').place( x= 30, y= 150, height = 120, width= 350)
        #create_contentBase_recommendations(self.bookName_textfield.get())
        if self.bookName_textfield.get() == "" :
            messagebox.showerror("Error", "Please enter book name", parent = self.root)
        else:
            try:
                conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
                cursor = conn.cursor()
                cursor.execute("select * from books where book_name=%s", (self.bookName_textfield.get()))
                row = cursor.fetchall()
                if not row:
                    messagebox.showerror("Error", f'"{str(self.bookName_textfield.get())}"?, No such book is present in the system', parent = self.root)
                #row = cursor.fetchall()
                else:
                #else:
                    #search result listbox
                    self.search_book_list.place( x= 30, y= 150, height = 310, width= 490)
                    

                    #book id textfield
                    self.book_id_textfield= Entry(self.search_book_list, font=('times new roman',11), bg='lightgrey', textvariable = book_id)
                    self.book_id_textfield.place(x= 10, y=10, width= 40, height= 20)
                    self.book_id_textfield.place_forget()

                    #searched book image
                    
                    #label and textfeild book title
                    self.book_name_label = Label(self.search_book_list, text='Book Title', font=('Goudy old style', 12, 'bold'), bg= '#61331c', fg= '#eacf8e').place(x= 185, y=30)
                    self.book_name_textfield = Entry(self.search_book_list,  font=('times new roman',11), bg='lightgrey', textvariable= book_Name)
                    self.book_name_textfield.place(x= 185, y=55, width= 130, height= 25)
                    

                    #label and textfeild book author name
                    book_author_name_label = Label(self.search_book_list, text='Author Name', font=('Goudy old style', 12, 'bold'), bg= '#61331c', fg= '#eacf8e').place(x= 335, y=30)
                    self.book_author_name_textfield = Entry(self.search_book_list, font=('times new roman',11), bg='lightgrey', textvariable=author_Name)
                    self.book_author_name_textfield.place(x= 335, y=55, width= 130, height= 25)
                    

                    #label and textfeild book pages
                    book_pages_label = Label(self.search_book_list, text='No. of Pages', font=('Goudy old style', 12, 'bold'), bg= '#61331c', fg= '#eacf8e').place(x= 185, y=90)
                    self.book_pages_no_textfield = Entry(self.search_book_list, font=('times new roman',11), bg='lightgrey', textvariable=book_Pages)
                    self.book_pages_no_textfield.place(x= 185, y=120, width= 130, height= 25)
                    

                    #label and textfeild book genre
                    book_genre_label = Label(self.search_book_list, text='Book Genre', font=('Goudy old style', 12, 'bold'), bg= '#61331c', fg= '#eacf8e').place(x= 335, y=90)
                    self.book_genre_textfield = Entry(self.search_book_list, font=('times new roman',11), bg='lightgrey', textvariable=book_Genre)
                    self.book_genre_textfield.place(x= 335, y=120, width= 130, height= 25)

                    #scroll bar for search frame
                    #self.scroll_bar = Scrollbar(self.book_description_textfield, orient=VERTICAL)
                    

                    #label and textfeild book description
                    book_description_label = Label(self.search_book_list, text='Book Description', font=('Goudy old style', 12, 'bold'), bg= '#61331c', fg= '#eacf8e').place(x= 185, y=155)
                    self.book_description_textfield = Text(self.search_book_list, font=('times new roman',11), bg='lightgrey',height=4, width=50)
                    #, yscrollcommand= self.scroll_bar.set)
                    self.book_description_textfield.place(x= 185, y=180, width= 280, height= 90)

                    #scroll bar for search frame
                    #self.scroll_bar.config(command=self.book_description_textfield.yview)
                    #self.scroll_bar.pack(side=RIGHT, fill=Y)

                    #label and rating mention
                    self.book_rating_label = Label(self.search_book_list, text='Rating: ', font=('Goudy old style', 12, 'bold'), bg= '#61331c', fg= '#eacf8e').place(x= 50, y=215)
                    self.book_rating_entry = Entry(self.search_book_list, font=('times new roman',11), bg='lightgrey', textvariable=book_Rating)
                    self.book_rating_entry.place(x= 110, y=220, width= 40, height= 20)
                    #self.book_rating_entry.config(state='disabled')


                    #button for add the book in my shelf
                    self.book_add = Button(self.search_book_list, command=self.add_book_to_myShelf , cursor='hand2', text='Add To Myshelf', bd=0, bg= '#eacf8e', fg= '#61331c', activebackground='#61331c', font=('times new roman',12)).place(x= 40, y=260, width=120, height=30)
                    
                    #print(row)
                    #book_Name.set("Hello")
                    for tup in row:
                        global img
                        img = Image.open(io.BytesIO(tup[7]))
                        img.thumbnail((120,182))
                        img = ImageTk.PhotoImage(img)

                        l2 = tk.Label(self.search_book_list,image=img)
                        l2.place(x= 25, y= 30, height = 182, width= 120)
                        #print(l2)

                        book_id.set(str(tup[0]))
                        book_Name.set(str(tup[1]))
                        author_Name.set(str(tup[2]))
                        book_Pages.set(str(tup[3]))
                        self.book_description_textfield.insert(INSERT, str(tup[4]))
                        book_Genre.set(str(tup[5]))
                        #it = str(tup[6])
                        #img = Image.open(io.BytesIO(tup[6]))
                        #collecting image and displaying 
                        
                        #l2.grid(row=2,column=2)
                        #search_book_image = ImageTk.PhotoImage(img)
                        #search_book_image = Label(self.search_book_list, image = search_book_image)
                        #self.search_book_image.ph
                        #search_book_image.place(x= 25, y= 30, height = 182, width= 130)

                        #self.search_book_image.config(state='disabled')
                        self.book_name_textfield.config(state='disabled')
                        self.book_author_name_textfield.config(state='disabled')
                        self.book_pages_no_textfield.config(state='disabled')
                        self.book_genre_textfield.config(state='disabled')
                        self.book_description_textfield.config(state='disabled')
                        self.book_id_textfield.config(state='disabled')
                        

                    #cursor.execute("select rating_no from book_rating where rating_of_bookID=%s", (self.book_id_textfield.get()))
                    #row1 = cursor.fetchone()
                    #if row1 != None:
                     #   for coln in row1:
                      #      book_Rating.set(double(coln[2]))
                       #     self.book_rating_entry.config(state='disable')

                #else:
                 #   messagebox.showerror("Error", "No such book is present in the system", parent = self.root)
                      
                    conn.commit()
                    conn.close()
                    #root.destroy()
                    #os.system('python forntPage.py')
            except Exception as excpt:
                messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)

    def get_book_image(self, id):
        pass 


    def add_book_to_myShelf(self):
    #    pass
        try:
            conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
            cursor = conn.cursor()
            cursor.execute("select book_id from book_in_shelf where book_id=%s", self.book_id_textfield.get())
            row = cursor.fetchone()
            if row != None:
                messagebox.showinfo("Duplication", "This book is already present in your shelf", parent = self.root)
            else:
                cursor.execute("insert into book_in_shelf (user_id, book_id) values (%s,%s)", 
                (
                    self.login_user_id_textfield.get(),
                    self.book_id_textfield.get()
                ))
                
                messagebox.showinfo("Book Added",f"{self.book_name_textfield.get()} , has been added to your shelf", parent = self.root)
            
                conn.commit()
                conn.close()
                #root.destroy()
                #os.system('python login.py')
        except Exception as excpt:
            messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)

    def show_recomendations(self):
        
       #disapper other frames
        self.frame_profile.place_forget()
        self.frame_my_shelf.place_forget()
        self.frame_search.place_forget()
        
        # frame for recommendations  placement
        self.frame_recommendations.place(x=340, y=120, width=550, height= 470,)

        #Search books label
        recommendations_label = Label(self.frame_recommendations, text='Recommendations', font=('Impact',35, 'bold'), bg= '#eacf8e', fg= '#61331c')
        recommendations_label.place(x=20, y= 5)

        try:
            conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
            cursor = conn.cursor()
            cursor1 = conn.cursor()
            cursor.execute("select prefered_genre from user where user_id=%s",(login_user_id.get()))
            row = cursor.fetchone()
            #print(row)
            if row is not None:
                    #print(row)

                #label 
                self.prefered_genre_label = Label(self.frame_recommendations, text='Your May Like To Read', font=('Goudy old style', 18, 'bold'), bg= '#eacf8e', fg= '#61331c')
                self.prefered_genre_label.place(x= 22, y=75)

                #frame for the display recommendation for prefered genre
                self.recommendation_for_prefered_genre_tree_frame = Frame(self.frame_recommendations, bg='#eacf8e')
                self.recommendation_for_prefered_genre_tree_frame.place(x= 30,y=120, width= 490, height=170)

                #treeview for recommendations for user prefered genre
                self.recommendation_for_prefered_genre_tree = ttk.Treeview(self.recommendation_for_prefered_genre_tree_frame)
                self.recommendation_for_prefered_genre_tree.place(width=478, height=170)
                #self.recommendation_for_prefered_genre_tree['show'] = ['headings']

                self.recommendation_for_prefered_genre_tree_sytle = ttk.Style(self.recommendation_for_prefered_genre_tree_frame)
                self.recommendation_for_prefered_genre_tree_sytle .theme_use("clam")
                self.recommendation_for_prefered_genre_tree_sytle .configure(".", foreground= '#61331c', font=('times new roman', 12))
                self.recommendation_for_prefered_genre_tree_sytle .configure("Treeview.Heading", foreground= '#61331c', font= ('Goudy old style', 15, "bold"))
                self.recommendation_for_prefered_genre_tree_sytle .configure("Treeview", rowheight= 65)

                #tree columns are 
                self.recommendation_for_prefered_genre_tree["columns"] = ("book_title", "book_author_name", "book_pages")

                #designing the columns
                
                self.recommendation_for_prefered_genre_tree.column("#0", width=40, anchor=tk.CENTER)
                self.recommendation_for_prefered_genre_tree.column("book_title", width=55, anchor=tk.CENTER)
                self.recommendation_for_prefered_genre_tree.column("book_author_name", width=60, anchor=tk.CENTER)
                self.recommendation_for_prefered_genre_tree.column("book_pages", width=20, anchor=tk.CENTER)

                #heading of the columns
                
                self.recommendation_for_prefered_genre_tree.heading("#0", text= "Book Cover", anchor=tk.CENTER)
                self.recommendation_for_prefered_genre_tree.heading("book_title", text= "Book Title", anchor=tk.CENTER)
                self.recommendation_for_prefered_genre_tree.heading("book_author_name", text= "Author Name", anchor=tk.CENTER)
                self.recommendation_for_prefered_genre_tree.heading("book_pages", text= "Pages", anchor=tk.CENTER)

                
                cursor1.execute("SELECT * FROM books WHERE book_genre=%s",(row) )
                #(recommend_prefered_genre_textfield.get()))
                #print (recommend_prefered_genre_textfield.get())
                
                _i = 0
                self.recommendation_for_prefered_genre_tree.imglist = []
                for tup in cursor1:
                    a = tup[1]
                    b = tup[2]
                    c = tup[3]
                    d = tup[5]
                    global _Img
                    _Img = Image.open(io.BytesIO(tup[7]))
                    _Img.thumbnail((50,70))
                    _Img = ImageTk.PhotoImage(_Img)
                    
                    l2 = tk.Label(self.recommendation_for_prefered_genre_tree_frame,image=_Img)
                    # print(str(a)) 
                    # print(str(b)) 
                    # print(str(c)) 
                    # #print(str(d))
                    
                    self.recommendation_for_prefered_genre_tree.insert(parent="", index="end", iid=_i, 
                    image= _Img, values=(a, b, c) )
                    self.recommendation_for_prefered_genre_tree.imglist.append(_Img)
                    _i += 1
            
                #vertical scrollbar for display table
                vertical_scroll_bar = ttk.Scrollbar(self.recommendation_for_prefered_genre_tree_frame, orient="vertical")
                vertical_scroll_bar.configure(command=self.recommendation_for_prefered_genre_tree.yview)
                self.recommendation_for_prefered_genre_tree.configure(yscrollcommand=vertical_scroll_bar.set)
                vertical_scroll_bar.pack(fill=Y, side=RIGHT)



                #print(create_contentBase_recommendations(self.recommend_prefered_genre_textfield.get()))

            else:
                messagebox.showinfo("Prefered Genre?", "Please select prefered genre in your profile, thank you", parent = self.root)


            conn.commit()
            conn.close()
                #root.destroy()
                #os.system('python login.py')
        except Exception as excpt:
            messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)




    def signOut(self):
        MsgBox = messagebox.askquestion ('Sign Out','Are you sure you want to sign out?',icon = 'warning')
        if MsgBox == 'yes':
            root.destroy()
            os.system('python login.py')
        else:
            #Do nothing
            pass
            


obj = profile_page(root)
root.mainloop()