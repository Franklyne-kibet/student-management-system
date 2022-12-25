from tkinter import*
from tkinter import messagebox
from PIL import ImageTk 


#login function
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()== 'Enter Your User Name' and passwordEntry.get() == 'Set your password':
        messagebox.showinfo('Success','Welcome') 
        window.destroy()
        import sms 
    else:
        messagebox.showerror('Error','Please enter correct username and password')

#Window Display
window = Tk()
window.geometry('1280x700+0+0')
window.title("Login System of Student Management System") 
window.resizable(False,False)

#Import the background image
backgroundImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

#<---------------Add login Frame--------------->
loginFrame = Frame(window,bg='White')
loginFrame.place(x=400,y=150)

##Login Image
loginImage = PhotoImage(file = 'logo.png')
logoLabel = Label(loginFrame,image = loginImage)
logoLabel.grid(row=0,column=0, columnspan=2,pady=10)

##username Logo
usernameImage = PhotoImage(file = 'user.png')
usernameLabel  = Label(loginFrame,image = usernameImage, text = 'Username',compound=LEFT, font=('times new roman',20,'bold'),bg='White')
usernameLabel.grid(row=1,column=0,padx=10,pady=10)

##username Entry Field
usernameEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,padx=10,pady=10)

##password logo
passwordImage = PhotoImage(file = 'password.png')
passwordLabel  = Label(loginFrame,image = passwordImage, text = 'Password',compound=LEFT, font=('times new roman',20,'bold'),bg='White')
passwordLabel.grid(row=2,column=0,padx=10,pady=10)

##Password Entry Field
passwordEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,padx=10,pady=10)

##Button
loginButton = Button(loginFrame,text = 'Login',font=('times new roman',14,'bold'),width=15,fg='White',bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='White', cursor='hand2', command=login) #login function
loginButton.grid(row=3,column=1,pady=10)

window = mainloop()