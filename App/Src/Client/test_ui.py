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
        self.user3_name_var = StringVar()
        self.user4_name_var = StringVar()
        self.user5_name_var = StringVar()
        self.user6_name_var = StringVar()
        self.user7_name_var = StringVar()
        self.user8_name_var = StringVar()
        self.user9_name_var = StringVar()
        self.user1_name = Label(tk, textvariable=self.user1_name_var, fg = "red")
        self.user2_name = Label(tk, textvariable=self.user2_name_var, fg = "red")
        self.user3_name = Label(tk, textvariable=self.user3_name_var, fg = "red")
        self.user4_name = Label(tk, textvariable=self.user4_name_var, fg = "red")
        self.user5_name = Label(tk, textvariable=self.user5_name_var, fg = "red")
        self.user6_name = Label(tk, textvariable=self.user6_name_var, fg = "red")
        self.user7_name = Label(tk, textvariable=self.user7_name_var, fg = "red")
        self.user8_name = Label(tk, textvariable=self.user8_name_var, fg = "red")
        self.user9_name = Label(tk, textvariable=self.user9_name_var, fg = "red")
        self.user1_name_var.set("Gabe")
        self.user2_name_var.set("Brandon")
        self.user3_name_var.set("Anas")
        self.user4_name_var.set("Hamza")
        self.user5_name_var.set("Hassan")
        self.user6_name_var.set("Gavin")
        self.user7_name_var.set("Vivian")
        self.user8_name_var.set("Aiden")
        self.user9_name_var.set("Derek")

        self.user1_name.grid(row=0, column=0)
        self.user2_name.grid(row=1, column=0)
        self.user3_name.grid(row=2, column=0)
        self.user4_name.grid(row=3, column=0)
        self.user5_name.grid(row=4, column=0)
        self.user6_name.grid(row=5, column=0)
        self.user7_name.grid(row=6, column=0)
        self.user8_name.grid(row=7, column=0)
        self.user9_name.grid(row=8, column=0)

if __name__ == "__main__":
    root = Tk()
    root.geometry("200x200")
    dem_win = demo_window(root, socket())
    while 1:
        root.update()
        root.update_idletasks()
