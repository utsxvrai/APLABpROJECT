#Bus Booking Sysytem
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


# Create a database or connect to one
conn = sqlite3.connect('bus_booking.db')

# Create cursor
cur = conn.cursor()

# Create table - bus
cur.execute('CREATE TABLE IF NOT EXISTS bus (b_id VARCHAR(5) NOT NULL PRIMARY KEY,b_type VARCHAR(10),capacity INT,fair INT,op_id VARCHAR(5) NOT NULL,route_id VARCHAR(5) NOT NULL,FOREIGN KEY (op_id) REFERENCES operator(opr_id),FOREIGN KEY (route_id) REFERENCES route(r_id))')

# Create table - operator
cur.execute("CREATE TABLE IF NOT EXISTS operator(opr_id VARCHAR(5) PRIMARY KEY,name VARCHAR(20),address VARCHAR(50),phone CHAR(10),email VARCHAR(30))")

# Create table - running buses
cur.execute("CREATE TABLE IF NOT EXISTS runningBuses(b_id VARCHAR(5),run_date DATE,seat_avail INT,FOREIGN KEY (b_id) REFERENCES bus(b_id))")

# Create table - route
cur.execute("CREATE TABLE IF NOT EXISTS route(r_id VARCHAR(5) NOT NULL PRIMARY KEY,s_name VARCHAR(20),s_id VARCHAR(5),d_name VARCHAR(20),d_id VARCHAR(5))")

# Create table - booking history
cur.execute("CREATE TABLE IF NOT EXISTS bookingHistory(name VARCHAR(20),gender CHAR(1),no_of_seat INT,phone CHAR(10),age INT,booking_ref VARCHAR(10) NOT NULL PRIMARY KEY,booking_date DATE,travel_date DATE,bid VARCHAR(5),FOREIGN KEY (bid) REFERENCES bus(b_id))")


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
            self.bookingPage()

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

                cur.execute("Select r_id from route where s_name=? and d_name=?", (source, dest))
                busList = cur.fetchall()

                if len(busList) == 0:
                    messagebox.showerror('Error', 'No bus found!')
                else:
                    for i in busList:
                        for j in i:
                            route_id = str(j)
                    
                    cur.execute("Select b_id from runningBuses where r_id=?", (route_id))
                    busCheck = cur.fetchall()
                    
                    if len(busCheck) == 0:
                        messagebox.showerror('Error', 'No bus found!')

                    else:
                        busIdList = []
                        for i in busCheck:
                            for j in i:
                                busIdList.append(j)

                        newBusIdList = []
                        for i in range(len(busIdList)):
                            cur.execute("Select b_id from runningBuses where run_date=? and b_id=?",(date, busIdList[i])) 
                            busD = cur.fetchall()
                            if len(busCheck) != 0:
                                newBusIdList.append(busD)
                            else:
                                pass

                        bh = []
                        for i in newBusIdList:
                            for j in i:
                                bh.append(j[0])

                        if len(bh) == 0:
                            messagebox.showerror('Error', 'No bus found!')

                        else :
                            Label(root,text='select bus ',font='Arial 10 bold').grid(row=6,column=3)
                            Label(root, text='operator ', font='Arial 10 bold').grid(row=6, column=4)
                            Label(root, text='b_type ', font='Arial 10 bold').grid(row=6, column=5)
                            Label(root, text='Available Capacity ', font='Arial 10 bold').grid(row=6, column=6)
                            Label(root, text='fare ', font='Arial 10 bold').grid(row=6, column=7)
                            r=7
                            busNo=IntVar()
                            selectBus = IntVar()
                            sNo=1
                            for i in b:
                                busNo=i
                                cur.execute('select op_id from bus where b_id=?',(i))
                                res_opr_id=cur.fetchall()
                                for j in res_opr_id:
                                    opr_id=j[0]

                                cur.execute('select name from operator where opr_id=?',(opr_id))
                                res_opr_name=cur.fetchall()
                                for j in res_opr_name:
                                    opr_name=j[0]

                                cur.execute('select b_type from bus where b_id=?',(i))
                                res_b_type=cur.fetchall()
                                for j in res_b_type:
                                    b_type=j[0]

                                cur.execute('select seat_avail from runningBuses where run_date=? and b_id=?',(jd,i))
                                res_seat_avail=cur.fetchall()
                                for j in res_seat_avail:
                                    seat_avail=j[0]

                                cur.execute('select fair from bus where b_id=?',(i))
                                res_fare=cur.fetchall()
                                for j in res_fare:
                                    fare=j[0]

                                def show_button():
                                        Button(root, text='PROCEED', bg='green', fg='black', font='Arial 12 bold',command=proceed).grid(row=10, column=9, padx=30)
                                var=Radiobutton(root,value=busNo,variable=selectBus,command=show_button)
                                var.grid(row=r,column=3)
                                Label(root, text=opr_name, font='Arial 10 bold').grid(row=r, column=4)
                                Label(root, text=b_type, font='Arial 10 bold').grid(row=r, column=5)
                                Label(root, text=seat_avail, font='Arial 10 bold').grid(row=r, column=6)
                                Label(root, text=fare, font='Arial 10 bold').grid(row=r, column=7)

                                r+=1
                                sNo+=1

                            def proceed():
                                f_b_id = selectBus.get()
                                Label(root,text="\n\n\n").grid(row=10,columnspan=12)
                                Label(root,text='Fill passenger details to book the bus', bg='light green', fg='dark green', font='Arial 18 bold').grid(row=11,columnspan=12)
                                Label(root, text="\n\n\n").grid(row=12,columnspan=12)

                                Label(root,text='name',font='Arial 10 bold').grid(row=13,column=3)
                                pname = Entry(root, font='Arial 12 bold', fg='black')
                                pname.grid(row=13,column=4)

                                gender = StringVar()
                                gender.set("Select Gender")
                                opt = ["M", "F", "T"]
                                g_menu = OptionMenu(root, gender, *opt)
                                g_menu.grid(row=13, column=6)

                                Label(root, text='no of seats', font='Arial 10 bold').grid(row=13, column=7)
                                pseat=Entry(root, font='Arial 12 bold', fg='black')
                                pseat.grid(row=13,column=8)

                                Label(root, text='mobile', font='Arial 10 bold').grid(row=14, column=3)
                                pmobile = Entry(root, font='Arial 12 bold', fg='black')
                                pmobile.grid(row=14, column=4)

                                Label(root, text='age', font='Arial 10 bold').grid(row=14, column=5)
                                page = Entry(root, font='Arial 12 bold', fg='black')
                                page.grid(row=14, column=6)

                                def book_seat():
                                    name=pname.get()
                                    gen=gender.get()
                                    seats=pseat.get()
                                    seats=int(seats)
                                    age=page.get()
                                    age=int(age)
                                    mobile=pmobile.get()
                                    bid=selectBus.get()
                                    if len(mobile)==10:
                                        if len(name)>0 and len(name)<20:
                                            if age>0 and age<150:
                                                if seats>0 and seats<60:
                                                        #print(name, gen, age, mobile, seats, bid)
                                                    booking_ref=1
                                                    cur.execute('select booking_ref from bookingHistory')
                                                    res_ref=cur.fetchall()
                                                    ref=[]
                                                    for i in res_ref:
                                                        ref.append(i[0])
                                                    booking_ref=len(ref)+1
                                                        #print(booking_ref)
                                                    cur_date=date.today()
                                                    cur.execute('insert into bookingHistory(name,gender,no_of_seat,phone,age,booking_ref,booking_date,travel_date,bid) values(?,?,?,?,?,?,?,?,?)',(name,gen,seats,mobile,age,booking_ref,cur_date,jd,bid))
                                                    con.commit()
                                                    cur.execute('select seat_avail from runningBuses where b_id=? and run_date=?',(bid,jd))
                                                    res_s=cur.fetchall()
                                                    s=res_s[0][0]
                                                    s=s-seats
                                                    cur.execute('update runningBuses set seat_avail=? where b_id=? and run_date=?',(s,bid,jd))
                                                    con.commit()
                                                    showinfo("succefull","booking successfull")

                                                else:
                                                    showerror("booking limit exceed","you can only book upto 5 seats")
                                            else:
                                                showerror("incorrect age","enter valid age")
                                        else:
                                            howerror("incorrect name","enter valid name")
                                    else:
                                        showerror("invalid mobile no","enter valid mobile no")


                                Button(root, text='BOOK SEAT', bg='green', fg='black', font='Arial 12 bold',
                                        command=book_seat).grid(row=16, column=9, padx=30)

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


    def bookingPage(self):
        root = Tk()
        root.title("BOOKING PAGE")
        root.state("zoomed")
        h, w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))
        bus = PhotoImage(file='Bus_for_project.png')
        home=PhotoImage(file='home.png')

        def check_booking_to_home():
            root.destroy()
            self.home_page()
        def check_tkt():
            mobile=mob.get()
            if len(mobile)==10 and mobile.isdigit():
                cur.execute('select * from booking_history where phone=?',[mobile])
                res_tkt=cur.fetchall()
                for i in res_tkt:
                    name=i[0]
                    gen=i[1]
                    seat=i[2]
                    phone=i[3]
                    age=i[4]
                    ref=i[5]
                    book_date=i[6]
                    travel_date=i[7]
                    b_i_d=i[8]
                cur.execute('select fair,route_id from bus where bus_id=?',[b_i_d])
                res_bus=cur.fetchall()
                fare=res_bus[0][0]
                route_id=res_bus[0][1]
                cur.execute('select s_name,e_name from route where r_id=?',[route_id])
                res_route=cur.fetchall()
                s_name=res_route[0][0]
                e_name=res_route[0][1]
                cur.execute('select booking_ref from booking_history where phone=?',[phone])
                res_ref=cur.fetchall()
                b_ref=res_ref[0][0]


                Label(text="YOUR TICKET", font='Arial 12 bold', bg='blue',fg='white').grid(row=6,columnspan=12 )
                Label(text="booking ref = "+b_ref,font='Arial 12 bold', fg='blue').grid(row=7,column=4)
                Label(text="name = " + name, font='Arial 12 bold', fg='blue').grid(row=7, column=5)
                Label(text="gender = " + gen, font='Arial 12 bold', fg='blue').grid(row=7, column=6)
                Label(text="no of seats = " + str(seat), font='Arial 12 bold', fg='blue').grid(row=7, column=7)
                Label(text="age = " + str(age), font='Arial 12 bold', fg='blue').grid(row=7, column=8)
                Label(text="booked on = " + book_date, font='Arial 12 bold', fg='blue').grid(row=8, column=4)
                Label(text="travel date = " + travel_date, font='Arial 12 bold', fg='blue').grid(row=8, column=5)
                Label(text="fare = " + str(fare), font='Arial 12 bold', fg='blue').grid(row=8, column=6)
                Label(text="total fare = " + str(fare*seat), font='Arial 12 bold', fg='blue').grid(row=8, column=7)




        Label(root, image=bus).grid(row=0, column=0, columnspan=12, padx=80)
        Label(root, text="Online Bus Booking System", font='Arial 30 bold', bg='LightCyan3', fg='red',relief=RAISED,padx=10,pady=10,bd=5).grid(row=2,
                                                                                                         column=0,
                                                                                                         columnspan=12,
                                                                                                         pady=20)
        Label(root, text="Check Your Booking", font='Arial 22 bold', bg='LightGreen').grid(row=3,
                                                                                                            column=0,
                                                                                                            pady=20,
                                                                                                            columnspan=12,
                                                                                                            padx=600)

        Label(root, text="Enter your mobile no.", font='Arial 12 bold', fg='black').grid(row=4, column=5)
        mob=Entry(root, font='Arial 12 bold')
        mob.grid(row=4, column=6)

        Button(root, text='Check Booking', font='Arial 12',command=check_tkt).grid(row=4, column=7)
        Button(root, image=home,command=check_booking_to_home).grid(row=5, column=7,pady=20)
        root.mainloop()

    def db_add_page(self):
        # Implement the add bus details page here
        pass



obj = BusBookingSystem()
obj.coverPage()