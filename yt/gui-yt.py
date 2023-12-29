from tkinter import *
from tkinter import messagebox
import psutil
import tkinter as tk
from pytube import YouTube

from pytube.exceptions import AgeRestrictedError

def download_video():
    input_url = url_input.get()

    def download(link):
        youtube_object = YouTube(link)
        try:
            youtube_object = youtube_object.streams.get_highest_resolution()
            youtube_object.download()
            messagebox.showinfo('Video Downloaded', 'Your Video is Downloaded successfully')
        except AgeRestrictedError as e:
            messagebox.showinfo('Age-Restricted', 'This video is age-restricted. Please log in to access.')
        except Exception as e:
            messagebox.showinfo('Error', f'An error has occurred: {e}')

    link = input_url
    download(link)

def get_network_speed():
    stats = psutil.net_io_counters()
    download_speed = stats.bytes_recv / 1024  # Download speed in KB
    upload_speed = stats.bytes_sent / 1024  # Upload speed in KB
    return download_speed, upload_speed

def update_speed_label():
    download_speed, upload_speed = get_network_speed()
    download_label.config(text=f"Download Speed: {download_speed:.2f} KB/s")
    upload_label.config(text=f"Upload Speed: {upload_speed:.2f} KB/s")
    root.after(1000, update_speed_label)  # Update speed label every second

root = Tk()
root.title('Download & Speed Checker')
root.minsize(500, 500)
root.geometry('900x750')
root.configure(background='#0096DC')

welcome_label = Label(root, text='YT Download Dashboard!', font=('Arial', 20), padx=20, pady=20)
welcome_label.pack()

download_label = Label(root, text='Download Speed: ', fg='white', bg='#0096DC')
download_label.pack(pady=(20, 5))
download_label.config(font=('verdana', 15))

upload_label = Label(root, text='Upload Speed: ',fg='white', bg='#0096DC')
upload_label.pack(pady=(20, 5))
upload_label.config(font=('verdana', 15))

url = Label(root, text='Enter the URL', fg='white', bg='#0096DC')
url.pack(pady=(20, 5))
url.config(font=('verdana', 18))

url_input = Entry(root, width=80)
url_input.pack(ipady=4, pady=(1, 15))

url_btn_download = Button(root, text='Download Video', bg='white', fg='black', width=15, height=1, command=download_video)
url_btn_download.config(font=('verdana', 15))
url_btn_download.pack(pady=(10, 10))

update_speed_label()  # Start the function to continuously update speed labels

root.mainloop()
