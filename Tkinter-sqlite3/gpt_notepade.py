import os
from tkinter import Tk, Text, Scrollbar, Menu, messagebox, filedialog

def open_text_file():
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open Text File",
                                           filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_area.delete(1.0, 'end')
            text_area.insert('end', content)

def save_as_text_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if file_path:
        with open(file_path, 'w') as file:
            content = text_area.get(1.0, 'end-1c')
            file.write(content)
        messagebox.showinfo('Information', 'File saved successfully.')

root = Tk()
root.title('Simple Notepad')

text_area = Text(root, wrap='word')
text_area.pack(expand='yes', fill='both')

scroll = Scrollbar(text_area)
text_area.configure(yscrollcommand=scroll.set)
scroll.config(command=text_area.yview)
scroll.pack(side='right', fill='y')

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_text_file)
file_menu.add_command(label='Save As...', command=save_as_text_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)
menu_bar.add_cascade(label='File', menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()
