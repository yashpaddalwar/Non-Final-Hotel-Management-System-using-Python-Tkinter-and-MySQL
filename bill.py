from tkinter import *;
from PIL import Image, ImageTk;    #pip install pillow
from tkinter import ttk;
import mysql.connector
import random
from tkinter import messagebox


class GenerateBill:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("400x550+600+220")


        #    """""""""""""""""""""""Variables""""""""""""""""""""""""

        self.var_contact = StringVar()
        self.var_roomavailable = StringVar()

        #    """""""""""""""""""""""Title""""""""""""""""""""""""

        lbl_title = Label(self.root,text="Bill",font=("times new roman",10,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=400,height=40)

        #    """""""""""""""""""""""Logo""""""""""""""""""""""""

        imglogo = Image.open(r"D:\Python MiniProject\images\hoteldeluxelogo.jpg")
        imglogo = imglogo.resize((50,40))
        self.photoimglogo = ImageTk.PhotoImage(imglogo)

        lblimg = Label(self.root,image=self.photoimglogo,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=50,height=40)


        #    """""""""""""""""""""""Button Frame""""""""""""""""""""""""

        btn_frame = Frame(self.root,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=40,width=400,height=60)

        # Cust_Contact
        lbl_contact = Label(btn_frame,text="Customer Contact",fg="black",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_contact.grid(row=0,column=0,sticky=W)

        entry_contact = ttk.Entry(btn_frame,textvariable=self.var_contact,width=20,font=("times new roman",10,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)


        #    """""""""""""""""""""""Bill Button""""""""""""""""""""""""
        buttonBill = Button(btn_frame,text="Generate Bill",command=self.Fetch_Details_customer,font=("times new roman",10,"bold"),bg="black",fg="white",width=10,cursor="hand2")
        buttonBill.grid(row=0,column=2,sticky=W)

        # Cust_Room
        lbl_Room = Label(btn_frame,text="Room No",fg="black",font=("times new roman",10,"bold"),padx=2,pady=6)
        lbl_Room.grid(row=1,column=0,sticky=W)

        entry_Room = ttk.Entry(btn_frame,textvariable=self.var_roomavailable,width=20,font=("times new roman",10,"bold"))
        entry_Room.grid(row=1,column=1,sticky=W)


        #    """""""""""""""""""""""Bill Button""""""""""""""""""""""""
        buttonBillroom = Button(btn_frame,text="Generate Bill",command=self.Fetch_Details_room,font=("times new roman",10,"bold"),bg="black",fg="white",width=10,cursor="hand2")
        buttonBillroom.grid(row=1,column=2,sticky=W)

        #    """""""""""""""""""""""Bill Frame""""""""""""""""""""""""

        printbill_frame = Frame(self.root,bd=0,relief=RIDGE)
        printbill_frame.place(x=0,y=490,width=400,height=30)

        #    """""""""""""""""""""""Bill Button""""""""""""""""""""""""
        buttonBillroom = Button(printbill_frame,text="Print Bill",font=("times new roman",10,"bold"),bg="black",fg="white",width=10,cursor="hand2")
        buttonBillroom.grid(row=1,column=2,sticky=W)

        
    def Fetch_Details_customer(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Fill the Contact Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error","The Number is not found!",parent=self.root)
            else:
                conn.commit()
                conn.close()


                #    """""""""""""""""""""""Bill Frame""""""""""""""""""""""""

                bill_frame = Frame(self.root,bd=0,relief=RIDGE)
                bill_frame.place(x=0,y=102,width=400,height=150)
                

                lblName = Label(bill_frame,text="Name:",font=("times new roman",12,"bold"))
                lblName.place(x=0,y=0)

                lbl = Label(bill_frame,text=row,font=("times new roman",12,"bold"))
                lbl.place(x=90,y=0)

                #    """""""""""""""""""""""Gender""""""""""""""""""""""""

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblGender = Label(bill_frame,text="Gender:",font=("times new roman",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2 = Label(bill_frame,text=row,font=("times new roman",12,"bold"))
                lbl2.place(x=90,y=30)

                #    """""""""""""""""""""""Email""""""""""""""""""""""""

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblEmail = Label(bill_frame,text="Email:",font=("times new roman",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl3 = Label(bill_frame,text=row,font=("times new roman",12,"bold"))
                lbl3.place(x=90,y=60)

                #    """""""""""""""""""""""Nationality""""""""""""""""""""""""

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblNationality = Label(bill_frame,text="Nationality:",font=("times new roman",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4 = Label(bill_frame,text=row,font=("times new roman",12,"bold"))
                lbl4.place(x=90,y=90)

                #    """""""""""""""""""""""Address""""""""""""""""""""""""

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblAddress = Label(bill_frame,text="Address:",font=("times new roman",12,"bold"))
                lblAddress.place(x=0,y=120)

                lbl5 = Label(bill_frame,text=row,font=("times new roman",12,"bold"))
                lbl5.place(x=90,y=120)

                


    def Fetch_Details_room(self):
        if self.var_roomavailable.get()=="":
            messagebox.showerror("Error","Fill the Room Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            query = ("select check_in from room where roomavailable=%s")
            value = (self.var_roomavailable.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error","The Room Number is not found!",parent=self.root)
            else:
                conn.commit()
                conn.close()


                #    """""""""""""""""""""""Check In""""""""""""""""""""""""

                bill_frame1 = Frame(self.root,bd=0,relief=RIDGE)
                bill_frame1.place(x=0,y=252,width=400,height=220)
                

                lblcheckin = Label(bill_frame1,text="Check-in:",font=("times new roman",12,"bold"))
                lblcheckin.place(x=0,y=0)

                lbl20 = Label(bill_frame1,text=row,font=("times new roman",12,"bold"))
                lbl20.place(x=90,y=0)


                #    """""""""""""""""""""""Check Out""""""""""""""""""""""""
                

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select check_out from room where roomavailable=%s")
                value = (self.var_roomavailable.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblcheckout = Label(bill_frame1,text="Check-Out:",font=("times new roman",12,"bold"))
                lblcheckout.place(x=0,y=30)

                lbl21 = Label(bill_frame1,text=row,font=("times new roman",12,"bold"))
                lbl21.place(x=90,y=30)


                #    """""""""""""""""""""""Room Type""""""""""""""""""""""""
                

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select roomtype from room where roomavailable=%s")
                value = (self.var_roomavailable.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblType = Label(bill_frame1,text="Room-Type:",font=("times new roman",12,"bold"))
                lblType.place(x=0,y=60)

                lbl22 = Label(bill_frame1,text=row,font=("times new roman",12,"bold"))
                lbl22.place(x=90,y=60)

                #    """""""""""""""""""""""Meal""""""""""""""""""""""""
                

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select meal from room where roomavailable=%s")
                value = (self.var_roomavailable.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblMeal = Label(bill_frame1,text="Meal:",font=("times new roman",12,"bold"))
                lblMeal.place(x=0,y=90)

                lbl23 = Label(bill_frame1,text=row,font=("times new roman",12,"bold"))
                lbl23.place(x=90,y=90)


                #    """""""""""""""""""""""Paid Tax""""""""""""""""""""""""
                

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select paidtax from room where roomavailable=%s")
                value = (self.var_roomavailable.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblpaidtax = Label(bill_frame1,text="Paid Tax:",font=("times new roman",12,"bold"))
                lblpaidtax.place(x=0,y=120)

                lbl6 = Label(bill_frame1,text=row,font=("times new roman",12,"bold"))
                lbl6.place(x=90,y=120)

            

                #    """""""""""""""""""""""Subtotal""""""""""""""""""""""""

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select subtotal from room where roomavailable=%s")
                value = (self.var_roomavailable.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblsubtotal = Label(bill_frame1,text="Sub-Total:",font=("times new roman",12,"bold"))
                lblsubtotal.place(x=0,y=150)

                lbl7 = Label(bill_frame1,text=row,font=("times new roman",12,"bold"))
                lbl7.place(x=90,y=150)

                #    """""""""""""""""""""""Total""""""""""""""""""""""""

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select total from room where roomavailable=%s")
                value = (self.var_roomavailable.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lbltotal = Label(bill_frame1,text="Total:",font=("times new roman",12,"bold"))
                lbltotal.place(x=0,y=180)

                lbl8 = Label(bill_frame1,text=row,font=("times new roman",12,"bold"))
                lbl8.place(x=90,y=180)





    



if __name__ == '__main__':
    root=Tk()
    object = GenerateBill(root)
    root.mainloop()
