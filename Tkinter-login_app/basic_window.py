from tkinter import *
from PIL import ImageTk,Image
from tkinter  import messagebox
#---------------------------------------------------------------------
#handle login function button

def handle_login():
    email = email_input.get()
    password = pass_input.get()
    print(email,password)

    if email == 'ankitshukla231211@gmail.com' and password == '231001':
        messagebox.showinfo('Okay,Great!','Login Successful')
    else:
        messagebox.showerror('Error','Login Credentials')

#---------------------------------------------------------------------
#configuration

root = Tk() #root is variable who stores screen main window # Tk() is built in keywords

root.title('Login form') # Title for top-right corner

root.iconbitmap('img.ico') # Icon for top-right corner & size=17*17 pxels

root.minsize(400,400) #control main size = minimum

# root.mixsize(400,400) #control main size = maximum

root.geometry('700x500') #control main size = particularly

root.configure(background='#0096DC') #control main window colour code of flipkart & 'blue'

#---------------------------------------------------------------------
#add image

img = Image.open('img_1.png') #open & add image into in main window
resized_img =  img.resize((100,100))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root,image=img)
img_label.pack(pady=(10,10))

#---------------------------------------------------------------------
# add text
text_label = Label(root,text='Flipkart',fg='white',bg='#0096DC') # text = text name + fg='' = text colour + bg='' = backgound
text_label.pack() #text execute
text_label.config(font=('verdana',24)) # verdana = text style, 24 is a size of txt


#---------------------------------------------------------------------
#add email title of text box

email_label = Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

#add email box
email_input = Entry(root,width=50)
email_input.pack(ipady=4,pady=(1,15))
#---------------------------------------------------------------------
#add passwd title of text box

pass_label = Label(root,text='Enter Password',fg='white',bg='#0096DC')
pass_label.pack(pady=(20,5))
pass_label.config(font=('verdana',12))

#add email box
pass_input = Entry(root,width=50)
pass_input.pack(ipady=4,pady=(1,15))
#---------------------------------------------------------------------
#login button & function

login_btn = Button(root,text='Login Here',bg='white',fg='black',width=10,height=1,command=handle_login)
login_btn.config(font=('verdana',15))
login_btn.pack(pady=(10,20))

#---------------------------------------------------------------------

root.mainloop() # never exit loop & mainloop()  holds the root's main window

# from PIL import Image
#
# img = Image.open('img.png')
# img.save('img.ico')
