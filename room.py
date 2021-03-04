from tkinter import *;
from PIL import Image, ImageTk;    #pip install pillow
from tkinter import ttk;
import mysql.connector
import random
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        #    """""""""""""""""""""""Title""""""""""""""""""""""""

        lbl_title = Label(self.root,text="ROOM-BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #    """""""""""""""""""""""Logo""""""""""""""""""""""""

        img2 = Image.open(r"D:\Python MiniProject\images\hoteldeluxelogo.jpg")
        img2 = img2.resize((100,40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


         #    """""""""""""""""""""""labelFrame""""""""""""""""""""""""

        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Room-Booking Details: ",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


if __name__ == '__main__':
    root=Tk()
    object=Roombooking(root)
    root.mainloop()