from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import os

class forgetPassword:
    def __init__(self, root):
        self.root = root
        self.root.title("Password?")    
        self.root.geometry("500x420+340+80")
        self.root.resizable(False, False)
        self.root.configure(bg='#61331c')


        # frame for login
        frame_login = Frame(self.root, bg='#eacf8e')
        frame_login.place(x=60, y=30, width=380, height=335,)

        #reset password here label
        login_label = Label(frame_login, text='Reset Password', font=('Impact',35, 'bold'), bg= '#eacf8e', fg= '#61331c')
        login_label.place(x=40, y= 40)

        #label and textfeild password
        newPassword_label = Label(frame_login, text='Password', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 65, y=120)
        self.newPassword_textfield = Entry(frame_login, font=('times new roman',15), bg='lightgrey')
        self.newPassword_textfield.place(x= 65, y=150, width= 250, height= 35)

        #label and textfield for confirm password
        confirmpassword_label = Label(frame_login, text='Confirm Password', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 65, y=185)
        self.confirmpassword_textfield = Entry(frame_login, font=('times new roman',15), bg='lightgrey', show='*')
        self.confirmpassword_textfield.place(x= 65, y=215, width= 250, height= 35)

        #sign up button
        self.reset_btn = Button(self.root, command = self.setPassword, cursor='hand2', text='Login', bd=0, bg= '#61331c', fg= '#eacf8e', activebackground='#61331c', font=('times new roman',20))
        self.reset_btn.place(x=170, y=320, width=180, height=40)

    def setPassword(self):
        pass
root = Tk()
obj = forgetPassword(root)
root.mainloop()