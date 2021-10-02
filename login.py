from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import os
import smtplib

#user_name = StringVar()

class login:
    #global login_username_textfield
    #global abc
    
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")    
        self.root.geometry("800x530+240+30")
        self.root.resizable(False, False)
        #global login_username_textfield\
        self.flag = 0

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
        global login_username_textfield
        username_label = Label(frame_login, text='Username', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 65, y=120)
        login_username_textfield = Entry(frame_login, font=('times new roman',15), bg='lightgrey')
        login_username_textfield.place(x= 65, y=150, width= 250, height= 35)
        

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
        if(self.flag == 0):
            abc = str(login_username_textfield.get())
            print(abc)
          
            if login_username_textfield.get() == "" or self.password_textfield.get() == "":
                messagebox.showerror("Error", "All fields are required to login", parent = self.root)
            else:
                try:
                    conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
                    cursor = conn.cursor()
                    cursor.execute("select * from user where user_username=%s and user_password=%s", (login_username_textfield.get(), self.password_textfield.get()))
                    row = cursor.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "Invalid username or password", parent = self.root)
                    else:
                        messagebox.showinfo("Welcome", f"Welcome {login_username_textfield.get()} , happy reading.", parent = self.root)
                        #print(str(self.login_username_textfield.get()))
                        self.flag +=1
                        
                        conn.commit()
                        conn.close()
                        #os.system('python mainPage.py')
                        #root.withdraw()
                        root.destroy()
                        #root.quit

                except Exception as excpt:
                    messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)
                    
        else:
            os.system('python mainPage.py')
            #self.root.quit()
            #self.root.withdraw()

    def user_name_pass():
        user_name = login_username_textfield.get()
        return user_name



    def forgetPassword_function(self):
        root.destroy()
        os.system('python forgetPassword.py')      
       

    def registerNow_btnFunction(self):
        root.destroy()
        os.system('python register.py')

root = Tk()
obj = login(root)
root.mainloop()