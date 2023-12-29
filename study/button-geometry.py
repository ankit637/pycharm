import tkinter as tk

def requestsuit_dashboard(root_ref):
    # Functionality for the 'Requestsuit' button goes here
    pass  # Placeholder for the functionality

def subsuit_dashboard():
    # Functionality for the 'SubSuit' button goes here
    pass  # Placeholder for the functionality

window = tk.Tk()
window.title('Dashboard')

dashboard_frame = tk.Frame(window, bg='#0096DC', width=300, height=200)
dashboard_frame.pack(fill='both', expand=True)

dashboard_label = tk.Label(dashboard_frame, text='Main Dashboard!', font=('Arial', 20), padx=50, pady=20)
dashboard_label.pack()

request_button = tk.Button(dashboard_frame, text='Requestsuit', bg='white', fg='black', width=15, height=1)
request_button.config(font=('verdana', 15))
request_button.place(x=100, y=100)

subdomain_button = tk.Button(dashboard_frame, text='SubSuit', bg='white', fg='black', width=15, height=1)
subdomain_button.config(font=('verdana', 15))
subdomain_button.place(x=310, y=100)
# ankitshukla123@gmail.com
window.mainloop()

