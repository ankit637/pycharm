import sqlite3
from tkinter import *
from PIL import ImageTk,Image
from tkinter  import messagebox

#---------------------------------------------------------------------
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import re
import json

#---------------------------------------------------------------------
# Function to switch to the dashboard upon successful login
def open_dashboard(root_ref):
    import requests
    from requests.exceptions import HTTPError
    from bs4 import BeautifulSoup
    import re
    import json
    # Hide or destroy login elements
    for widget in root_ref.winfo_children():
        widget.destroy()

    # Create a new frame for the dashboard
    dashboard_frame = Frame(root_ref, bg='#0096DC')
    dashboard_frame.pack(fill='both', expand=True)

    # Add widgets and functionality for the dashboard
    welcome_label = Label(dashboard_frame, text='RequestSuit Dashboard!', font=('Arial', 20), padx=20, pady=20)
    welcome_label.pack()

    # Add a text label for the domain URL
    text_label = Label(dashboard_frame, text='Enter The Domain URL', fg='white', bg='#0096DC')
    text_label.pack()
    text_label.config(font=('verdana', 20))

    # Add domain entry box to the dashboard_frame
    domain = Entry(dashboard_frame, width=80)
    domain.pack(ipady=8, pady=(15, 15))

    # -----------------------------------------------------------------------------------------------------------------------
    # start domain functionality
    def handle_domain():
        domain_input = domain.get()
        url = domain_input
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            print('Success!')
            print(response.text)





    # -----------------------------------------------------------------------------------------------------------------------
    # domain button & function
    domain_btn = Button(dashboard_frame, text='Start Here', bg='white', fg='black', width=10, height=1, command=handle_domain) #
    domain_btn.config(font=('verdana', 15))
    domain_btn.pack(pady=(10, 20))


#---------------------------------------------------------------------
#handle login function button
def handle_login():
    email = email_input.get()
    password = pass_input.get()

    conn = sqlite3.connect('../requestsuit/login_credentials.db')
    cursor = conn.cursor()


    # Search for the entered credentials in the database
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        messagebox.showinfo('Success', 'Login Successful')
        open_dashboard(root)
    else:
        messagebox.showerror('Error', 'Invalid Credentials')

#---------------------------------------------------------------------

from tkinter import Toplevel

# Function to create a new account
def create_account():
    # Function to handle adding user to the database
    def add_user():
        new_email = new_email_input.get()
        new_password = new_pass_input.get()

        conn = sqlite3.connect('../requestsuit/login_credentials.db')
        cursor = conn.cursor()

        # Insert new user into the database
        cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (new_email, new_password))

        conn.commit()
        conn.close()

        messagebox.showinfo('Success', 'Account Created Successfully')

        # Close the create account window and go back to the main window
        create_account_window.destroy()

    # Create a new window for creating an account
    create_account_window = Toplevel(root)
    create_account_window.title('Create Account')

    new_email_label = Label(create_account_window, text='Enter New Email', fg='white', bg='#0096DC')
    new_email_label.pack(pady=(20, 5))
    new_email_label.config(font=('verdana', 12))

    new_email_input = Entry(create_account_window, width=50)
    new_email_input.pack(ipady=4, pady=(1, 15))

    new_pass_label = Label(create_account_window, text='Enter New Password', fg='white', bg='#0096DC')
    new_pass_label.pack(pady=(20, 5))
    new_pass_label.config(font=('verdana', 12))

    new_pass_input = Entry(create_account_window, width=50)
    new_pass_input.pack(ipady=4, pady=(1, 15))

    create_btn = Button(create_account_window, text='Create Account', bg='white', fg='black', width=15, height=1, command=add_user)
    create_btn.config(font=('verdana', 15))
    create_btn.pack(pady=(10, 20))


#---------------------------------------------------------------------
#configuration

root = Tk() #root is variable who stores screen main window # Tk() is built in keywords

root.title('Login form') # Title for top-right corner

root.iconbitmap('img.ico') # Icon for top-right corner & size=17*17 pxels

root.minsize(500,500) #control main size = minimum

# root.mixsize(400,400) #control main size = maximum

root.geometry('900x700') #control main size = particularly

root.configure(background='#0096DC') #control main window colour code of flipkart & 'blue'

# Create a frame for the login screen
login_frame = Frame(root, bg='#0096DC')
#---------------------------------------------------------------------
#add image

img = Image.open('../img_1.png') #open & add image into in main window
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
# Adding a 'Create Account' button to the main window
create_account_btn = Button(root, text='Create Account', bg='white', fg='black', width=15, height=1, command=create_account)
create_account_btn.config(font=('verdana', 15))
create_account_btn.pack(pady=(10, 20))


#---------------------------------------------------------------------

#---------------------------------------------------------------------

root.mainloop() # never exit loop & mainloop()  holds the root's main window

# from PIL import Image
#
# img = Image.open('img.png')
# img.save('img.ico')
