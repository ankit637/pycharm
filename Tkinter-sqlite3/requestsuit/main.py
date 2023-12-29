import sqlite3
from tkinter import *
from PIL import ImageTk,Image



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

        # ankitshukla123@gmail.com
        # ankit123

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

    import tkinter as tk
    from tkinter import filedialog
    import requests
    from tkinter import messagebox
    import json
    import subprocess
    import os

    import tkinter as tk
    from tkinter import filedialog

    class Notepad(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)

            # Set the title for the notepad
            self.title("Notepad")

            # Create a text widget
            self.text = tk.Text(self, wrap="word")
            self.text.pack(side="top", fill="both", expand=True)

            # Create a menu bar
            self.menu = tk.Menu(self)
            self.config(menu=self.menu)

            # Create a file menu
            file_menu = tk.Menu(self.menu)
            self.menu.add_cascade(label="File", menu=file_menu)
            file_menu.add_command(label="New", command=self.new_file)
            file_menu.add_command(label="Open", command=self.open_file)
            file_menu.add_command(label="Save", command=self.save_file)
            file_menu.add_separator()
            file_menu.add_command(label="Exit", command=self.quit)

            # Create an edit menu
            edit_menu = tk.Menu(self.menu)
            self.menu.add_cascade(label="Edit", menu=edit_menu)
            edit_menu.add_command(label="Cut", command=self.cut)
            edit_menu.add_command(label="Copy", command=self.copy)
            edit_menu.add_command(label="Paste", command=self.paste)

        def new_file(self):
            self.text.delete("1.0", "end")
            self.title("Notepad")

        def open_file(self):
            file = filedialog.askopenfile(parent=self, mode="rb", title="Open a file")
            if file:
                contents = file.read()
                self.text.delete("1.0", "end")
                self.text.insert("1.0", contents)
                file.close()
                self.title(file.name + " - Notepad")

        def save_file(self):
            file = filedialog.asksaveasfile(mode="w", defaultextension=".txt",
                                            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
            if file:
                contents = self.text.get("1.0", "end")
                file.write(contents)
                file.close()
                self.title(file.name + " - Notepad")

        def cut(self):
            self.text.event_generate("<<Cut>>")

        def copy(self):
            self.text.event_generate("<<Copy>>")

        def paste(self):
            self.text.event_generate("<<Paste>>")

    # -----------------------------------------------------------------------------------------------------------------------
    # start domain functionality
    def handle_domain():
        domain_input = domain.get()
        url = domain_input
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            result_box.insert(END, f'HTTP error occurred - {http_err}\n')
        except Exception as err:
            result_box.insert(END, f'Other error occurred - {err}\n')
        else:
            result_box.insert(END, 'Success!\n')

            # Write request headers to 'request.header.txt'
            request_headers = dict(response.request.headers)
            with open('../request.header.txt', 'w') as file:
                json.dump(request_headers, file, indent=4)  # Save headers as JSON with indentation

            messagebox.showinfo('Success', 'Request headers saved successfully')

            # Write response headers to 'response.header.txt'
            response_headers = dict(response.headers)
            with open('../response_header.txt', 'w') as file:
                json.dump(response_headers, file, indent=4)  # Save headers as JSON with indentation

            messagebox.showinfo('Success', 'Response headers saved successfully')

            soup = BeautifulSoup(response.text, 'html.parser')
            links = [a['href'] for a in soup.find_all('a', href=True)]

            with open('../urls.txt', 'w') as urls_file:
                for link in links:
                    urls_file.write(link + '\n')

            messagebox.showinfo('Success', 'Web Page URLs saved successfully')

            # Write response headers to 'response.header.txt'
            session_cookies = dict(response.cookies)
            with open('../cookies.txt', 'w') as file:
                json.dump(session_cookies, file, indent=4)

            messagebox.showinfo('Success', 'Session Cookies saved successfully')

            with open('../html.txt', 'wb') as file:
                file.write(response.content)

            messagebox.showinfo('Success', 'HTML Content saved successfully')

    #-----------------------------------------------------------------------------------------------------------------------
    # open request header file
    def open_request_headers():
        # Open the file in the Notepad GUI
        notepad = Notepad()
        with open('../request.header.txt', 'r') as file:
            contents = file.read()
            notepad.text.insert("1.0", contents)
        notepad.title("Request Headers - Notepad")
        notepad.mainloop()

    # -----------------------------------------------------------------------------------------------------------------------
    # open response header file
    def open_response_headers():
        # Open the file in the Notepad GUI
        notepad = Notepad()
        with open('../response_header.txt', 'r') as file:
            contents = file.read()
            notepad.text.insert("1.0", contents)
        notepad.title("Request Headers - Notepad")
        notepad.mainloop()

    # -----------------------------------------------------------------------------------------------------------------------
    def open_urls():
        # Open the file in the Notepad GUI
        notepad = Notepad()
        with open('../urls.txt', 'r') as file:
            contents = file.read()
            notepad.text.insert("1.0", contents)
        notepad.title("Web Page URLs - Notepad")
        notepad.mainloop()

    # -----------------------------------------------------------------------------------------------------------------------
    def cookies():
        # Open the file in the Notepad GUI
        notepad = Notepad()
        with open('../cookies.txt', 'r') as file:
            contents = file.read()
            notepad.text.insert("1.0", contents)
        notepad.title("Session Cookies - Notepad")
        notepad.mainloop()

    # -----------------------------------------------------------------------------------------------------------------------
    def html():
        # Open the file in the Notepad GUI
        notepad = Notepad()
        with open('../html.txt', 'r', encoding='utf-8') as file:  # Specify the encoding
            contents = file.read()
            notepad.text.insert("1.0", contents)
        notepad.title("HTML Content - Notepad")
        notepad.mainloop()

    # -----------------------------------------------------------------------------------------------------------------------
    # domain button & function
    domain_btn = Button(dashboard_frame, text='Start Here', bg='white', fg='black', width=10, height=1, command=handle_domain) #
    domain_btn.config(font=('verdana', 15))
    domain_btn.pack(pady=(10, 20))

    # Add a label for 'Result' text
    result_label = Label(dashboard_frame, text='Output Area', font=('Arial', 14),padx=10, pady=10 ) #bg='#0096DC',fg='white'
    result_label.pack()

    # Add a text box to display the result
    result_box = Text(dashboard_frame, height=1, width=10)
    result_box.pack(pady=15)
    result_box.config(font=('Arial', 18))
# -----------------------------------------------------------------------------------------------------------------------
    # domain button & function
    request_btn = Button(dashboard_frame, text='Request Headers', bg='white', fg='black', width=15, height=1, command=open_request_headers) #
    request_btn.config(font=('verdana', 15))
    request_btn.pack(pady=(10, 20))

    # domain button & function
    response_btn = Button(dashboard_frame, text='Response Headers', bg='white', fg='black', width=15, height=1, command=open_response_headers) #
    response_btn.config(font=('verdana', 15))
    response_btn.pack(pady=(10, 20))

    # domain button & function
    url_btn = Button(dashboard_frame, text='Response URLs', bg='white', fg='black', width=15, height=1, command=open_urls) #
    url_btn.config(font=('verdana', 15))
    url_btn.pack(pady=(10, 20))

    # cookies button & function
    cookies_btn = Button(dashboard_frame, text='Session Cookies', bg='white', fg='black', width=15, height=1, command=cookies) #
    cookies_btn.config(font=('verdana', 15))
    cookies_btn.pack(pady=(10, 20))

    # cookies button & function
    html_btn = Button(dashboard_frame, text='HTML Content', bg='white', fg='black', width=15, height=1,command=html)  #
    html_btn.config(font=('verdana', 15))
    html_btn.pack(pady=(10, 20))
#---------------------------------------------------------------------
#handle login function button
import hashlib
def handle_login():
    email = email_input.get()
    password = pass_input.get()

    k, j, d = 0, 0, 0
    user = None

    if len(email) >= 6 and len(password) >= 6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@") == 1):
                if (email[-4] == ".") ^ (email[-3] == "."):
                    for i in email:
                        if i == i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1

                    if k == 0 and j == 0 and d == 0:
                        conn = sqlite3.connect('login_credentials.db')
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
    # Function to create a lock window
    def lock_window(window_to_lock):
        lock = Toplevel(window_to_lock)
        lock.attributes('-topmost', True)  # Ensure the lock window is on top
        lock.transient(window_to_lock)  # Set the lock window as transient for the main window
        lock.grab_set()  # Grab all events for the lock window

        # Customize the lock window appearance or add a message
        lock_label = Label(lock, text="Processing...", font=('Arial', 12))
        lock_label.pack(padx=20, pady=20)

        return lock

    # Function to handle adding user to the database
    import sqlite3

    def create_users_table():
        conn = sqlite3.connect('login_credentials.db')
        cursor = conn.cursor()

        # SQL command to create the users table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                email TEXT UNIQUE,
                password TEXT
            )
        ''')

        conn.commit()
        conn.close()

    def add_user():
        create_users_table()  # Ensure the 'users' table exists

        new_email = new_email_input.get()
        new_password = new_pass_input.get()

        # Lock the create_account_window
        lock = lock_window(create_account_window)

        k, j, d = 0, 0, 0

        if len(new_email) and len(new_password) >= 6:
            if new_email[0].isalpha():
                if ("@" in new_email) and (new_email.count("@") == 1):
                    if (new_email[-4] == ".") ^ (new_email[-3] == "."):
                        for i in new_email:
                            if i == i.isspace():
                                k = 1
                            elif i.isalpha():
                                if i == i.upper():
                                    j = 1
                            elif i.isdigit():
                                continue
                            elif i == "_" or i == "." or i == "@":
                                continue
                            else:
                                d = 1

                        if k == 1 or j == 1 or d == 1:
                            messagebox.showinfo('Wrong Input', 'Enter the Correct Email')
                        else:
                            # Insert new user into the database
                            conn = sqlite3.connect('login_credentials.db')
                            cursor = conn.cursor()
                            cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)",
                                           (new_email, new_password))
                            conn.commit()
                            conn.close()
                            messagebox.showinfo('Success', 'Account Created Successfully')
                            create_account_window.destroy()
                            lock.destroy()
                    else:
                        messagebox.showinfo('Wrong Input', 'Enter the Correct Email')
                else:
                    messagebox.showinfo('Wrong Input', 'Enter the Correct Email')
            else:
                messagebox.showinfo('Wrong Input', 'Enter the Correct Email')
        else:
            messagebox.showinfo('Wrong Input', 'Enter the Correct Email')
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

root.title('Login Into RequestSuit') # Title for top-right corner

#root.iconbitmap('app.ico') # Icon for top-right corner & size=17*17 pxels

root.minsize(500,500) #control main size = minimum

# root.mixsize(400,400) #control main size = maximum

root.geometry('900x750') #control main size = particularly

root.configure(background='#0096DC') #control main window colour code of flipkart & 'blue'

# Create a frame for the login screen
login_frame = Frame(root, bg='#0096DC')
#---------------------------------------------------------------------
#add image

# img = Image.open('test.png') #open & add image into in main window
# resized_img =  img.resize((100,100))
# img = ImageTk.PhotoImage(resized_img)
#
# img_label = Label(root,image=img)
# img_label.pack(pady=(10,10))

#---------------------------------------------------------------------
# add text
text_label = Label(root,text='RequestSuit',fg='white',bg='#0096DC') # text = text name + fg='' = text colour + bg='' = backgound
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
