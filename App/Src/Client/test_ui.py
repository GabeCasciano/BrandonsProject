from tkinter import * 
from socket import *
from threading import *

HOST = ""
PORT = 12345

class demo_window:
    class worker(Thread):
        def __init__(self, conn: socket):
            pass
    
    def __init__(self, tk: Tk, conn: socket):
        tk.title("Demo window")
        self.tk = tk

        self.user1_name_var = StringVar()
        self.user2_name_var = StringVar()
        self.user1_name = Label(tk, textvariable=self.user1_name_var, fg = "red")
        self.user2_name = Label(tk, textvariable=self.user2_name_var, fg = "red")
        self.user1_name_var.set("Gabe")
        self.user2_name_var.set("Brandon")

        self.user1_name.grid(row=0, column=0)
        self.user2_name.grid(row=1, column=0)

if __name__ == "__main__":
    root = Tk()
    root.geometry("200x200")
    dem_win = demo_window(root, socket())
    while 1:
        root.update()
        root.update_idletasks()
