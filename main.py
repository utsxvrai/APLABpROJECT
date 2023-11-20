#Bus Booking Sysytem
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class BusBookingSystem:
    def homePage(self):
        
        root = Tk()
        root.title("Bus Booking System")
        root.state('zoomed')
        bus = PhotoImage(file="bus.png")
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry("%dx%d+0+0" % (w, h))
        root.configure(bg='cyan')

        Label(root, image=bus , bg='cyan').grid(row=0, column=1, columnspan=3, pady=20, padx=w // 3)  # Centered image
        Label(root, text="Online Bus Booking System", font='Arial 30 bold', bg='bisque', fg='orangered2', relief=RAISED,
              padx=10, pady=10, bd=5).grid(row=1, column=1, columnspan=3, pady=20, padx=w // 3)  # Centered text

        def home_to_journey_detail():
            root.destroy()
            self.journeyDetail()

        def home_to_check_booking():
            root.destroy()
            self.check_booking_page()

        def home_to_db_add_page():
            root.destroy()
            self.db_add_page()

        Button(root, text='Seat Booking', font='Arial 14 bold', bg='navy', fg='white',
               command=home_to_journey_detail).grid(row=7, column=1,pady=(80,0))
        Button(root, text='Check Booked Seat', font='Arial 14 bold', bg='navy', fg='white',
               command=home_to_check_booking).grid(row=7, column=2,pady=(80,0))
        Button(root, text='Add Bus Details', font='Arial 14 bold', bg='navy', fg='white',
               command=home_to_db_add_page).grid(row=7, column=3,pady=(80,0))

        Label(root, text='For Admin Only', fg='red', bg='cyan').grid(row=8, column=3)

        root.mainloop()

    def coverPage(self):
        root = Tk()
        root.title("COVER PAGE")
        root.state("zoomed")
        bus = PhotoImage(file='bus.png')
        

        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))
        root.configure(bg='cyan')  # Set the background color to white

        Label(root, image=bus, bg='cyan').pack()
        Label(root, text="Online Bus Booking System", font='Arial 30 bold', bg='white', fg='red', relief=RAISED,
            padx=10, pady=10, bd=5).pack()
        Label(root, text="\n\n\n\n\nName: Utsav Rai", font='Arial 16 bold', fg='blue', bg='cyan').pack()
        Label(root, text="Enr. No. : 221B425", font='Arial 16 bold', fg='blue', bg='cyan').pack()
        Label(root, text="Mobile : 8423829911\n\n\n\n", font='Arial 16 bold', fg='blue', bg='cyan').pack()
        Label(root, text="Submitted to: Dr. Mahesh Kumar", font='Arial 15 bold', bg='cyan', padx=10, pady=10, fg='red').pack()
        Label(root, text="Project Based Learning", font='Arial 15 bold', bg='cyan', fg='red').pack()

        def gotoHome(event):
            root.destroy()
            self.homePage()

        root.bind("<KeyPress>", gotoHome)
        root.mainloop()

    def journeyDetail(self):
        root = Tk()
        root.title("JOURNEY DETAIL")
        root.state("zoomed")

        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        bus = PhotoImage(file='bus.png')
        root.geometry('%dx%d+0+0' % (w, h))
        root.configure(bg='cyan')




        Label(root, image=bus, bg='cyan' ).grid(row=0, column=1, columnspan=3, pady=20, padx=w // 3)  # Centered image
        Label(root, text="Online Bus Booking System", font='Arial 30 bold', bg='bisque', fg='orangered2', relief=RAISED,padx=10, pady=10, bd=5).grid(row=1,     
            column=1, columnspan=3, pady=20, padx=w // 3)  # Centered text
        Label(root, text='Check Bus Availability!', bg='cyan', fg='navy', font='Arial 18 bold').grid(row=3, column=1,columnspan=12, pady=20)


        def home():
            root.destroy()
            self.homePage()

        # function to search buses
        def searchBus():
            
            dest = to_place.get()
            source = from_place.get()
            date = journey_date.get()


            if dest.isalpha() and source.isalpha() and date!='':
                dest = des.lower()
                source = source.lower()

                cur.execute("SELECT * FROM bus WHERE destination=? AND source=? AND date=?",(dest,source,date))


            else:
                messagebox.showerror('Error', 'Check the details entered!')


        input_frame = Frame(root, bg='white', relief='raised')
        input_frame.grid(row=4, column=3, columnspan=8, pady=10)

        # Create a ttk.Style to configure the frame
        style = ttk.Style()
        style.configure("RoundedFrame.TFrame", background='white', relief='raised', borderwidth=5)
        input_frame = ttk.Frame(root, style="RoundedFrame.TFrame")
        input_frame.grid(row=4, column=0, columnspan=8, pady=10)

        Label(input_frame, text='To :', fg='navy', font='Arial 12 bold').grid(row=0, column=0, padx=20, pady=10)
        to_place = Entry(input_frame, font='Arial 12 bold', fg='black')
        to_place.grid(row=0, column=1, padx=50 , pady=10)

        Label(input_frame, text='From :', fg='navy', font='Arial 12 bold').grid(row=0, column=2, padx=20 , pady=10)
        from_place = Entry(input_frame, font='Arial 12 bold', fg='black')
        from_place.grid(row=0, column=3, padx=50, pady=10)

        Label(input_frame, text='Date :', fg='navy', font='Arial 12 bold').grid(row=0, column=4, padx=20 , pady=10)
        journey_date = Entry(input_frame, font='Arial 12 bold', fg='black')
        journey_date.grid(row=0, column=5, padx=50, pady=10)

        Label(input_frame, text="date format YYYY-MM-DD" , fg='navy').grid(row=1, column=5, pady=(0,10))

        Button(input_frame, text='Search Buses', font='Arial 12 bold', bg='navy', fg='white').grid(row=0, column=6, padx=20, pady=10)

        life = PhotoImage(file='home.png')
        Button(input_frame, image=life, command=home).grid(row=0, column=7 , padx=20, pady=10)




        root.mainloop()


    def check_booking_page(self):
        # Implement the check booking page here
        pass

    def db_add_page(self):
        # Implement the add bus details page here
        pass



obj = BusBookingSystem()
obj.coverPage()