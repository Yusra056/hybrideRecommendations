from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import os

class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")    
        self.root.geometry("800x530+240+30")
        self.root.resizable(False, False)

        # background Image
        self.bg = PhotoImage(file='C:\\Users\\IA\\Pictures\\background2.png')
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # frame for login
        frame_login = Frame(self.root, bg='#eacf8e')
        frame_login.place(x=20, y=70, width=380, height=335,)

        #login here label
        login_label = Label(frame_login, text='Login Here', font=('Impact',35, 'bold'), bg= '#eacf8e', fg= '#61331c')
        login_label.place(x=60, y= 40)

        #label and textfeild username
        username_label = Label(frame_login, text='Username', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 65, y=120)
        self.username_textfield = Entry(frame_login, font=('times new roman',15), bg='lightgrey')
        self.username_textfield.place(x= 65, y=150, width= 250, height= 35)

        #label and textfield for password
        password_label = Label(frame_login, text='Password', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 65, y=185)
        self.password_textfield = Entry(frame_login, font=('times new roman',15), bg='lightgrey', show='*')
        self.password_textfield.place(x= 65, y=215, width= 250, height= 35)

        #sign up button
        signup_btn = Button(frame_login, command = self.registerNow_btnFunction, text='Register Now', cursor='hand2',bd=0, bg= '#eacf8e', fg= '#61331c', activebackground='#eacf8e', font=('times new roman',11,'underline')).place(x=65, y=265)

        #forget password button
        forget_btn = Button(frame_login, command = self.forgetPassword_function, text='Forget Password?', cursor='hand2', bd=0, bg= '#eacf8e', fg= '#61331c', activebackground='#eacf8e', font=('times new roman',11)).place(x=205, y=265)
        

        #login button
        login_btn = Button(self.root, command = self.login_function, cursor='hand2', text='Login', bd=0, bg= '#61331c', fg= '#eacf8e', activebackground='#61331c', font=('times new roman',20)).place(x=115, y=393, width=180, height=40)

    def login_function(self):
        if self.username_textfield.get() == "" or self.password_textfield.get() == "":
            messagebox.showerror("Error", "All fields are required to login", parent = self.root)
        else:
            try:
                conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
                cursor = conn.cursor()
                cursor.execute("select * from user where user_username=%s and user_password=%s", (self.username_textfield.get(), self.password_textfield.get()))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid username or password", parent = self.root)
                else:
                    messagebox.showinfo("Welcome", f"Welcome {self.username_textfield.get()} , happy reading.", parent = self.root)
        
                    conn.commit()
                    conn.close()
                    root.destroy()
                    os.system('python forntPage.py')
            except Exception as excpt:
                messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)

    def forgetPassword_function(self, root):
        messagebox.showinfo("Password?", f"Welcome {self.username_textfield.get()} , Reset your password.", parent = self.root)
        os.system('forgetPassword.py')

    def registerNow_btnFunction(self):
        root.destroy()
        os.system('python forntPage.py')

root = Tk()
obj = login(root)
root.mainloop()