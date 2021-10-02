import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import pymysql

my_w = tk.Tk()
my_w.geometry("980x651+180+10")  # Size of the window 
my_w.title('www.plus2net.com')
my_font1=('times', 18, 'bold')

l1 = tk.Label(my_w,text='books added with images',font=my_font1)  
l1.grid(row=1,column=1,columnspan=5)

l2 = tk.Label(my_w,  text='book Name', width=20 )  # added one Label 
l2.grid(row=2,column=1)

book_name = tk.Entry(my_w,width=20,bg='yellow') # added one Entry box
book_name.grid(row=2,column=2)

l3 = tk.Label(my_w,  text='book author Name', width=20 )  # added one Label 
l3.grid(row=2,column=3)

author_name = tk.Entry(my_w,width=20,bg='yellow') # added one Entry box
author_name.grid(row=2,column=4)

l4 = tk.Label(my_w,  text='book page no', width=20 )  # added one Label 
l4.grid(row=3,column=1)

book_page_no = tk.Entry(my_w,width=20,bg='yellow') # added one Entry box
book_page_no.grid(row=3,column=2)

l5 = tk.Label(my_w,  text='book Description', width=20 )  # added one Label 
l5.grid(row=3,column=3)

book_description = tk.Entry(my_w,width=20,bg='yellow') # added one Entry box
book_description.grid(row=3,column=4)

l6 = tk.Label(my_w,  text='book Genre', width=20 )  # added one Label 
l6.grid(row=4,column=1)

book_genre = tk.Entry(my_w,width=20,bg='yellow') # added one Entry box
book_genre.grid(row=4,column=2)

l7 = tk.Label(my_w,  text='book pdf link', width=20 )  # added one Label 
l7.grid(row=4,column=3)

book_pdf_link = tk.Entry(my_w,width=20,bg='yellow') # added one Entry box
book_pdf_link.grid(row=4,column=4)

b2 = tk.Button(my_w, text='Upload File', 
   command = lambda:upload_file())
b2.grid(row=5,column=1) 

my_font=('times', 12, 'bold')
b3 = tk.Button(my_w, text='Add data', font=my_font,
   command = lambda:add_data())
b3.grid(row=6,column=1,padx=20) 

global filename # Access this from both functions

def upload_file(): # Image upload and display
    global filename,img
    #w = 200, h = 200
    f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    b2 =tk.Button(my_w,image=img) # using Button 
    b2.grid(row=7,column=1,columnspan=2)#display uploaded photo
       
def add_data(): # Add data to MySQL table 
    global img , filename 
    fob=open(filename,'rb') # filename from upload_file()
    fob=fob.read()
    data=(book_name.get(), author_name.get(), book_page_no.get(),book_description.get(), book_genre.get() ,book_pdf_link.get(),fob) # tuple with data 
    conn = pymysql.connect(host = "localhost", user = "root", password="", database="fyp")
    cursor = conn.cursor()
    cursor.execute("insert into books(book_name, book_author_name, book_page_no, book_description, book_genre,book_pdf_link, book_image) values (%s,%s,%s,%s,%s,%s,%s)",data)
    conn.commit()
    conn.close()
    messagebox.showinfo("Message","the book is added to the database")
    
    #print("Row Added  = ") # displayed in console 
    #my_w.destroy() # close window after adding data
my_w.mainloop()  # Keep the window open
#http://localhost/phpmyadmin/tbl_get_field.php?db=fyp&table=books&where_clause=%60books%60.%60book_id%60+%3D+5&transform_key=book_image&sql_query=SELECT+%2A+FROM+%60books%60