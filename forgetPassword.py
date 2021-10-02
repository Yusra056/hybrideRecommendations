from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import os
import smtplib

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

         #back buttton
        back_btn = Button(frame_login, command= self.goBack_btnFunction, cursor='hand2', text='<', bd=0, bg= '#61331c', fg= '#eacf8e', activebackground='#61331c', font=('times new roman',30, 'bold')).place(x=10, y=5, width=40, height=40)


        #reset password here label
        login_label = Label(frame_login, text='Forget Password', font=('Impact',35, 'bold'), bg= '#eacf8e', fg= '#61331c')
        login_label.place(x=40, y= 60)

        #statement
        statement_label = Label(frame_login, text='Please enter the Email address linked \n with this application', font=('times new roman',15, 'bold'), bg= '#eacf8e', fg= '#61331c')
        statement_label.place(x=40, y= 130)

        #label and textfield to enter email address
        email_label = Label(frame_login, text='Email Address', font=('Goudy old style', 15, 'bold'), bg= '#eacf8e', fg= '#61331c').place(x= 65, y=195)
        self.email_textfield = Entry(frame_login, font=('times new roman',15), bg='lightgrey')
        self.email_textfield.place(x= 65, y=230, width= 250, height= 35)

        #send email button
        self.reset_btn = Button(self.root, command = self.sentEmail, cursor='hand2', text='Sent email', bd=0, bg= '#61331c', fg= '#eacf8e', activebackground='#61331c', font=('times new roman',20))
        self.reset_btn.place(x=170, y=320, width=180, height=40)

    def sentEmail(self):
        if self.email_textfield.get() == "":
            messagebox.showerror("Error", "Please enter the required email address", parent = self.root)
        else:
            try:
                conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
                cursor = conn.cursor()
                cursor.execute("select user_password from user where user_email=%s", (self.email_textfield.get()))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please recheck your entered email address", parent = self.root)
                else:
                    messagebox.showinfo("Email Send", "We have send you the email to your email address. please check the email. If you can not find it in your inbox please check the spam tab. Thank you")
       
                    with smtplib.SMTP('smtp.gmail.com',  587) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()

                        smtp.login('whatShouldIReadNextBook','obfohnlrecpeovpc')

                        subject = 'Help for your account password'
                        body = f'We have mailed you your account password that you had entered when you registered your account. You should change your password after login. Your password is {row} , happy reading.'

                        msg = f'Subject: {subject}\n\n{body}'

                        smtp.sendmail('whatShouldIReadNextBook', 'joysjiya45@gmail.com', msg)
                        print('Sent email successfully')
       
                    conn.commit()
                    conn.close()
                    #root.destroy()
                    #os.system('python forntPage.py')
            except Exception as excpt:
                messagebox.showerror("Error", f"Error due to: {str(excpt)}", parent = self.root)
    
    def goBack_btnFunction(self):
        root.destroy()
        os.system('python login.py')


root = Tk()
obj = forgetPassword(root)
root.mainloop()