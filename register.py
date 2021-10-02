import os
from tkinter import *
#from PIL import ImageTk
from tkinter import messagebox
import pymysql
class register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Page")    
        self.root.geometry("850x566+240+30")
        self.root.resizable(False, False)
        
        # background Image
        self.bg = PhotoImage(file='C:\\Users\\IA\\Pictures\\signup_background.png')
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #back buttton
        back_btn = Button(self.root, command= self.goBack_btnFunction, cursor='hand2', text='Go Back', bd=0, bg= '#61331c', fg= '#eacf8e', activebackground='#61331c', font=('times new roman',14, 'bold')).place(x=10, y=20, width=80, height=30)


        # frame for register
        frame_register = Frame(self.root, bg='#eacf8e')
        frame_register.place(x=20, y=130, width=485, height= 320,)

        #register here label
        login_label = Label(frame_register, text='Register Here', font=('Impact',35, 'bold'), bg= '#eacf8e', fg= '#61331c')
        login_label.place(x=20, y= 5)

        #label and textfeild name
        name_label = Label(frame_register, text='Name', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 30, y=70)
        self.name_textfield = Entry(frame_register, font=('times new roman',15), bg='lightgrey')
        self.name_textfield.place(x= 30, y=100, width= 190, height= 35)

        #label and textfield for email
        email_label = Label(frame_register, text='Email', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 30, y=140)
        self.email_textfield = Entry(frame_register, font=('times new roman',15), bg='lightgrey')
        self.email_textfield.place(x= 30, y=170, width= 190, height= 35)

        #label and textfield for password
        password_label = Label(frame_register, text='Password', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 30, y=210)
        self.password_textfield = Entry(frame_register, font=('times new roman',15), bg='lightgrey', show='*')
        self.password_textfield.place(x= 30, y=240, width= 190, height= 35)

        #label and textfeild username
        username_label = Label(frame_register, text='Username', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 265, y=70)
        self.username_textfield = Entry(frame_register, font=('times new roman',15), bg='lightgrey')
        self.username_textfield.place(x= 265, y=100, width= 190, height= 35)

        #label and textfield for contactNo
        contactNo_label = Label(frame_register, text='Contact No', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 265, y=140)
        self.contactNo_textfield = Entry(frame_register, font=('times new roman',15), bg='lightgrey')
        self.contactNo_textfield.place(x= 265, y=170, width= 190, height= 35)

        #label and textfield for confirm password
        cnfrmpassword_label = Label(frame_register, text='Confirm Password', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 265, y=210)
        self.cnfrmpassword_textfield = Entry(frame_register, font=('times new roman',15), bg='lightgrey', show='')
        self.cnfrmpassword_textfield.place(x= 265, y=240, width= 190, height= 35)

        #register button
        register_btn = Button(self.root, command= self.register_data, cursor='hand2', text='Signup', bd=0, bg= '#61331c', fg= '#eacf8e', activebackground='#61331c', font=('times new roman',20)).place(x=170, y=430, width=180, height=40)

    def register_data(self):

        if self.name_textfield.get().isalpha() == False:
            messagebox.showerror("Error", "Name most be of alphabets only", parent = self.root)
        elif self.contactNo_textfield.get().isdigit() == False:
            messagebox.showerror("Error", "Contact Number must be of numbers only", parent = self.root)
        elif self.name_textfield.get() == '' or self.username_textfield.get() == '' or self.email_textfield.get() == '' or self.contactNo_textfield.get() == '' or self.password_textfield.get() == '' or self.cnfrmpassword_textfield.get() == '':
            messagebox.showerror("Error", "All fields are required to signup", parent = self.root)
        elif self.password_textfield.get() != self.cnfrmpassword_textfield.get():
            messagebox.showerror("Error", "Password's and Confirm Password's entries do not match", parent = self.root)
        else:
            try:
                conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
                cursor = conn.cursor()
                cursor.execute("select * from user where user_username=%s", self.username_textfield.get())
                row = cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exists with the current username. Pleae try another", parent = self.root)
                
                else:
                    cursor.execute("insert into user (user_name, user_username, user_email, user_contactNo, user_password) values (%s,%s,%s,%s,%s)", 
                    (
                        self.name_textfield.get(),
                        self.username_textfield.get(),
                        self.email_textfield.get(),
                        self.contactNo_textfield.get(),
                        self.password_textfield.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Welcome", f"Thank you for joining {self.username_textfield.get()} , happy reading.", parent = self.root)
                    root.destroy()
                    os.system('python login.py')
            except Exception as excpt:
                messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)
        
    def goBack_btnFunction(self):
        root.destroy()
        os.system('python login.py')

    def username_passed(self):
        return self.username_textfield


root = Tk()
obj = register(root)
root.mainloop()