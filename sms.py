from tkinter import*
import time
import ttkthemes
from tkinter import ttk
import pymysql
from tkinter import messagebox,filedialog
import pandas as pd

#<------------functionality part-------------->

##Connect database 
def connect_database():
    #connect function 
    def connect():
        global mycursor,con
        try:
            con = pymysql.connect(host= hostEntry.get(), user=usernameEntry.get(), password=passwordEntry.get()) #host='localhost',user='root',password='enter your password'
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Invalid Details',parent=connectWindow)
            return
        
        try:
            #create database query
            query = 'create database studentmanagementsystem'
            mycursor.execute(query)
            #use database
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            #create student table 
            query = 'create table student(id int not null primary key, name varchar(30), mobile varchar(10), email varchar(30), address varchar(100), gender varchar(20), dob varchar(20), date varchar(50), time varchar(50))'
            mycursor.execute(query)
        except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            
        messagebox.showinfo('Success', 'Database Connection is successfull!', parent = connectWindow)
        connectWindow.destroy()
        
        #activate button state
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
            
    #create a top level display
    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title("Database Connection")
    connectWindow.resizable(0,0)
    
    #Hostname Label
    hostnameLabel = Label(connectWindow,text='Host Name:', font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)
    
    #Hostname Entry
    hostEntry = Entry(connectWindow, font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=20,pady=20)
    
    #Username Label
    usernameLabel = Label(connectWindow,text='User Name:', font=('arial',20,'bold'))
    usernameLabel.grid(row=1,column=0,padx=20)
    
    #UserName Entry
    usernameEntry = Entry(connectWindow, font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1,padx=20,pady=20)
    
    #Password Label
    passwordLabel = Label(connectWindow,text='Password:', font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)
    
    #Password Entry
    passwordEntry = Entry(connectWindow, font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=20,pady=20)
    
    #Connect Buttton
    connectButton = ttk.Button(connectWindow,text='CONNECT', command=connect)
    connectButton.grid(row=3,columnspan=2)
    
##clock function
def clock():
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'  Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)

##slider functon  
count = 0
text = ''

def slider():
    global text,count
    text += s[count] #s 
    sliderLabel.config(text = text)
    count += 1
    sliderLabel.after(500,slider)
    
    if count == len(s):
        count = 0
        text = ''

# <---------------------Buttons functionality-------------------->
# global elements
global currenttime, date

#Top window function
def toplevel_data(title,button_text,command):
    global idEntry,phoneEntry,nameEntry,emailEntry,addressEntry,genderEntry,dobEntry,screen
    # Top level window
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(0, 0)

    # Entry fields for search student
    # Idlabel
    idLabel = Label(screen, text='Id',font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=20, pady=20, sticky=W)
    # Entry Field
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=15)

    # Name label
    nameLabel = Label(screen, text='Name',font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=20, sticky=W)
    # Entry Field
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=15)

    # Phone label
    phoneLabel = Label(screen, text='Phone',font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=20, pady=20, sticky=W)
    # Entry Field
    phoneEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, padx=10, pady=15)

    # Email label
    emailLabel = Label(screen, text='Email',font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=20, pady=20, sticky=W)
    # Entry Field
    emailEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=10, pady=15)

    # Address label
    addressLabel = Label(screen, text='Address',font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=20, pady=20, sticky=W)
    # Entry Field
    addressEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, padx=10, pady=15)

    # Gender label
    genderLabel = Label(screen, text='Gender',font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=20, pady=20, sticky=W)
    # Entry Field
    genderEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, padx=10, pady=15)

    # DOB label
    dobLabel = Label(screen, text='D.O.B',font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=20, pady=20, sticky=W)
    # Entry Field
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=10, pady=15)

    # Screen Button
    screen_button = ttk.Button(screen, text=button_text, command=command)
    screen_button.grid(row=7, columnspan=2, pady=10)
    
    # grab the item index
    if title == 'Update Student':
        indexing = studentTable.focus()

        content = studentTable.item(indexing)
        list_data = content['values']

        # Insert the data into the Entry field
        idEntry.insert(0, list_data[0])
        nameEntry.insert(0, list_data[1])
        phoneEntry.insert(0, list_data[2])
        emailEntry.insert(0, list_data[3])
        addressEntry.insert(0, list_data[4])
        genderEntry.insert(0, list_data[5])
        dobEntry.insert(0, list_data[6])
                
#exit button
def iexit():
    result = messagebox.askyesno('Confirm','Do you want to exit?')
    if result :
        root.destroy()
    else:
        pass

#Export data function
def export_data():
    url = filedialog.asksaveasfilename(defaultextension = '.csv')
    indexing = studentTable.get_children()
    newlist = []
    for index in indexing:
        content = studentTable.item(index)
        datalist = content['values']
        newlist.append(datalist)
    
    table =pd.DataFrame(newlist, columns = ['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data is saved successfully')
        

#Update student Button Functionality
def update_data():
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    query = 'update student set name =%s,mobile =%s,email =%s,address =%s, gender =%s, dob=%s, date =%s,time =%s where id = %s'
    mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date, currenttime, idEntry.get()))
    
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully', parent = screen)
    screen.destroy()

    #show update in the Tree view
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END, values = data)

#Show student Button Functionality
def show_student():
    query  = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END, values=data)

#Delete button Functionality
def delete_student():
        indexing = studentTable.focus()
        content  =studentTable.item(indexing)
        content_id = content['values'][0]
        query  = 'delete from student where id=%s'
        mycursor.execute(query,content_id)
        con.commit()
        messagebox.showinfo('Deleted',f'Id {content_id} is deleted successfully')
    
    #Display the updated data
        query = 'select * from student '
        mycursor.execute(query)
        fetched_data  = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', END, values=data)
        

# Functionality of Search Student Button

def search_data():
    query = 'select * from student where id =%s or name =%s or mobile=%s or email=%s or address=%s or gender=%s or dob = %s'
    mycursor.execute(query,(idEntry.get(), nameEntry.get(), phoneEntry.get() , emailEntry.get(), addressEntry.get(), genderEntry.get(), dobEntry.get()))
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)
        
# Functionality of add student Button
#function add_data 
def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Error','All Feilds are required',parent=screen)

    else:
        try:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime))
            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                emailEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            return


        query='select *from student'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('',END,values=data)


#<-------------------GUI Part----------------------->
root = ttkthemes.ThemedTk()

#get themes & apply
root.get_themes()
root.set_theme('radiance')

root.geometry('1174x680+0+0')#'1280x700+0+0'
root.resizable(0,0)
root.title('Student Management System')

#Datetime Label
datetimeLabel = Label(root, font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

#Slider Label 
s='Student Management System' #s[count] = S when count is 0
sliderLabel = Label(root,font=('arial',23,'italic bold'), width=50)
sliderLabel.place(x=200,y=0)
slider()

#Connect Button
connectButton = ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)

#<------------------------Left frame------------------------------>
leftFrame = Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

#Student Logo
logo_image = PhotoImage(file='students.png')
logo_label = Label(leftFrame, image = logo_image)
logo_label.grid(row=0,column=0)

# Add Student Button
addstudentButton = ttk.Button(leftFrame,text='Add Student',width=25, state=DISABLED, command=lambda :toplevel_data('Add Student', 'Add' , add_data))
addstudentButton.grid(row=1,column=0,pady=20)

# Search Button
searchstudentButton = ttk.Button(leftFrame,text='Search Student',width=25, state=DISABLED, command= lambda :toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)

#Delete Button
deletestudentButton = ttk.Button(leftFrame,text='Delete Student',width=25, state=DISABLED, command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

#update Student Button
updatestudentButton = ttk.Button(leftFrame,text='Update Student',width=25, state=DISABLED, command= lambda :toplevel_data('Update Student','Update', update_data))
updatestudentButton.grid(row=4,column=0,pady=20)

#Show Student Button
showstudentButton = ttk.Button(leftFrame,text='Show Student',width=25, state=DISABLED, command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

#Export Student Button
exportstudentButton = ttk.Button(leftFrame,text='Export Data',width=25, state=DISABLED, command=export_data)
exportstudentButton.grid(row=6,column=0,pady=20)

#Exit Button
exitButton = ttk.Button(leftFrame,text='Exit',width=25, command=iexit)
exitButton.grid(row=7,column=0,pady=20)

#<-----------------------Right frame---------------------->
rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

#Scroll bar
scrollBarX = Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame,orient=VERTICAL)

#preview table
studentTable = ttk.Treeview(rightFrame,columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B','Added Date', 'Added Time'), xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

#configure the X&Y views
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

studentTable.pack(fill=BOTH,expand=1)

#Add values to the table
studentTable.heading('Id', text = 'Id')
studentTable.heading('Name', text = 'Name')
studentTable.heading('Mobile No', text = 'Mobile No')
studentTable.heading('Email', text = 'Email')
studentTable.heading('Address', text = 'Address')
studentTable.heading('Gender', text = 'Gender')
studentTable.heading('D.O.B', text = 'D.O.B')
studentTable.heading('Added Date', text = 'Added Date')
studentTable.heading('Added Time', text = 'Added Time')

#Student Table Column Methods
studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Mobile No',width=200,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Address',width=200,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)
studentTable.column('Added Date',width=200,anchor=CENTER)
studentTable.column('Added Time',width=200,anchor=CENTER)

#Style the TreeView
style = ttk.Style()

style.configure('Treeview', rowheight= 40, font=('arial',12,'bold'), foreground='red4', background ='white', fieldbackground='white')
style.configure('Treeview.Heading', font= ('arial',14,'bold'),foreground = 'Red')

studentTable.config(show='headings') #removes the first empty column

root.mainloop()