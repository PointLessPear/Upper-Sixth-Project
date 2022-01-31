import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import time
from datetime import date
from datetime import datetime

import sqlite3

from MainGUI import main
import ManagerMenu as MM
import ManagerBookingSettings as MBS

import ReceptionBookingSettings as RBS

class AddBookingGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title, AccessLevel):
        global CustIDVar, RoomOption, SpecialRequestsVar, CheckInDateVar, CheckOutDateVar, globalAccessLevel

        globalAccessLevel = AccessLevel

        CustIDVar = StringVar()
        SpecialRequestsVar = StringVar()
        CheckInDateVar = StringVar()
        CheckOutDateVar = StringVar()
        RoomOption = StringVar()

        #RoomID, RoomNum, CostPerNight, Sleeps, Availability

        if globalAccessLevel == 'Manager':
            self.CreateBackButtonManagerMenu(8)
        if globalAccessLevel == 'Reception':
            self. CreateBackButtonReceptionMenu(8)


        #Gathering room info from the rooms table in the DB and storing it in a list.
        with sqlite3.connect('Montalto Estate Hotel.db') as db:

            RoomNum, CostPerNight, Sleeps, Availabilty = [], [], [], []

            #Rooms = []
            c = db.cursor()
            sql = '''SELECT * FROM Rooms'''
            try:
                c.execute(sql)
                for i in range(15):
                    row = c.fetchone()

                    #print(row)

                    RoomNum.append(int(row[1]))
                    CostPerNight.append(str(row[2]))
                    Sleeps.append(int(row[3]))
                    Availabilty.append(str(row[4]))

            except:
                print('Error: Data not found')

        #Default option/Var for dropdown option menu

        DropDownOptions = [[RoomNum[0], CostPerNight[0], Sleeps[0], Availabilty[0]],
                           [RoomNum[1], CostPerNight[1], Sleeps[1], Availabilty[1]],
                           [RoomNum[2], CostPerNight[2], Sleeps[2], Availabilty[2]],
                           [RoomNum[3], CostPerNight[3], Sleeps[3], Availabilty[3]],
                           [RoomNum[4], CostPerNight[4], Sleeps[4], Availabilty[4]],
                           [RoomNum[5], CostPerNight[5], Sleeps[5], Availabilty[5]],
                           [RoomNum[6], CostPerNight[6], Sleeps[6], Availabilty[6]],
                           [RoomNum[7], CostPerNight[7], Sleeps[7], Availabilty[7]],
                           [RoomNum[8], CostPerNight[8], Sleeps[8], Availabilty[8]],
                           [RoomNum[9], CostPerNight[9], Sleeps[9], Availabilty[9]],
                           [RoomNum[10], CostPerNight[10], Sleeps[10], Availabilty[10]],
                           [RoomNum[11], CostPerNight[11], Sleeps[11], Availabilty[11]],
                           [RoomNum[12], CostPerNight[12], Sleeps[12], Availabilty[12]],
                           [RoomNum[13], CostPerNight[13], Sleeps[13], Availabilty[13]],
                           [RoomNum[14], CostPerNight[14], Sleeps[14], Availabilty[14]]]

        #print(DropDownOptions)
        RoomOption.set('Rooms')

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        # Intalises all Labels, Entries, OptionMenus and Buttons
        self.CustIDlbl = Label(self.master, text='Customer ID:', font=('Calibri', 12), bg=bgcolour).grid(column=0,row=2, pady=3)
        self.CustIDEntry = Entry(self.master, text='....', textvariable=CustIDVar, width=25).grid(column=1, row=2, pady=3)

        self.RoomNumlbl = Label(self.master, text='Room:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=3, pady=3)
        self.RoomNumOpt = OptionMenu(self.master, RoomOption, *DropDownOptions).grid(column=1, row=3, pady=3)

        self.SpecialRequestslbl = Label(self.master, text='Special Requests:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=4, pady=3)
        self.SpecialRequestsEntry = Entry(self.master, text='....', textvariable=SpecialRequestsVar, width=25).grid(column=1, row=4, pady=3)

        self.CheckInDatelbl = Label(self.master, text='CheckInDate:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=6, pady=3)
        self.CheckInDateEntry = Entry(self.master, text='....', textvariable=CheckInDateVar, width=25).grid(column=1, row=6, pady=3)

        self.CheckOutDatelbl = Label(self.master, text='Check Out Date:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=7, pady=3)
        self.CheckOutDateEntry = Entry(self.master, text='....', textvariable=CheckOutDateVar, width=25).grid(column=1, row=7, pady=3)

        self.ContinueBtn = Button(self.master, text='Register', command=self.DataValidation, width=18, font=('Calibri', 12)).grid(column=1, row=8, pady=5)
        self.ConfirmCustBtn = Button(self.master, text='Confirm Customer', command=self.ConfirmCust, width=18, font=('Calibri', 12)).grid(column=1, row=9, pady=5)

        #still need room num dropdown, totalcost and cost per night, duration of stay
    def DataValidation(self):
        self.CustID = CustIDVar.get()
        self.SpecialReq = SpecialRequestsVar.get()
        self.CheckInDate = CheckInDateVar.get()
        self.CheckOutDate = CheckOutDateVar.get()
        self.Room = RoomOption.get()

        # self.CostPerNight = CostPerNightVar.get()
        # self.TotalCost = TotalCostVar.get()
        #self.DurationOfStay = DurationOfStayVar.get()

        if self.CustID == '':
            messagebox.showerror('Error', 'Customer ID requried')
        else:
            self.CustID == self.CustID

        if self.SpecialReq == '':
            messagebox.showerror('Error', 'Special Requests requried')
        else:
            self.SpecialReq == self.SpecialReq

        if self.CheckInDate == '':
            messagebox.showerror('Error', 'Check-in-date requried')
        else:
            self.CheckInDate == self.CheckInDate

        if self.CheckOutDate == '':
            messagebox.showerror('Error', 'Check-out-date requried')
        else:
            self.CheckOutDate == self.CheckOutDate

        if len(self.CustID) > 0 < 3:
            self.CustID == self.CustID
        else:
            messagebox.showerror('Error', 'Customer ID invalid')

        if len(self.SpecialReq) > 0 < 250:
            self.SpecialReq = self.SpecialReq
        else:
            messagebox.showerror('Error', 'Special Requests invalid')

        if len(self.CheckInDate) == 10:
            self.CheckInDate = self.CheckInDate
        else:
            messagebox.showerror('Error', 'Check-in-date invalid')

        if len(self.CheckOutDate) == 10:
            self.CheckOutDate = self.CheckOutDate
        else:
            messagebox.showerror('Error', 'Check-out-date invalid')

        self.FetchInputs(self.CustID, self.Room, self.SpecialReq, self.CheckInDate, self.CheckOutDate)

    def FetchInputs(self, CustID, Room, SpecialReqs, CheckInDate, CheckOutDate):
        #need to calc = total cost, room info from db
        BookingDate = date.today()
        date_format = "%d/%m/%Y"
        FormatedCheckIn = datetime.strptime(CheckInDate, date_format)
        FormatedCheckOut = datetime.strptime(CheckOutDate, date_format)
        DurationOfStay = FormatedCheckOut - FormatedCheckIn


        #print(DurationOfStay.days)
        #print(Room[1:3])

        #Get Room Details
        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            RoomSql = '''SELECT * FROM Rooms WHERE RoomID = ?'''
            RoomValu = Room[1:3]

            for char in RoomValu:
                if char in "[](),'":
                    RoomValu = RoomValu.replace(char, '')

            c.execute(RoomSql, RoomValu)
            RoomDetails = c.fetchone()
            #print(RoomDetails)

            RoomID = RoomDetails[0]
            CostPerNight = str(RoomDetails[2])
            Avaliablity = str(RoomDetails[4])

            for char in CostPerNight:
                if char in "[](),'£":
                    CostPerNight = CostPerNight.replace(char, '')

            CostPerNight = int(CostPerNight)
            TotalCost = CostPerNight * DurationOfStay.days
            #print(CostPerNight)
            #print(TotalCost)
            if Avaliablity == 'Yes':
                c = db.cursor()
                BookingSql = '''INSERT INTO Booking (CustID, RoomID, BookingDate, RoomNum, SpecialRequests, CostPerNight, TotalCost, DurationOfStay, CheckInDate, CheckOutDate) VALUES (?,?,?,?,?,?,?,?,?,?)'''
                BookingValues = (CustID, RoomID, BookingDate, RoomDetails[0], SpecialReqs, CostPerNight, TotalCost, DurationOfStay.days, CheckInDate, CheckOutDate)
                c.execute(BookingSql, BookingValues)

                #Getting booking id from booking table as it is automatically assigned by db.

                GetBookingIDSQL = '''SELECT * FROM Booking WHERE (CustID, RoomID, BookingDate, RoomNum, SpecialRequests, CostPerNight, TotalCost, DurationOfStay, CheckInDate, CheckOutDate) = (?,?,?,?,?,?,?,?,?,?)'''
                GetBookingIDValues = (CustID, RoomID, BookingDate, RoomDetails[0], SpecialReqs, CostPerNight, TotalCost, DurationOfStay.days, CheckInDate, CheckOutDate)
                c.execute(GetBookingIDSQL, GetBookingIDValues)

                BookingID = c.fetchone()

                self.DisplayBookingInfo(BookingID[0], CustID, RoomID, RoomDetails[3], TotalCost, DurationOfStay.days, CheckInDate, CheckOutDate)
            else:
                messagebox.showerror('Error', 'Room Not Available')

    def DisplayBookingInfo(self, BookingID, CustID, RoomID, Sleeps, TotalCost,DurationOfStay, CheckInDate, CheckOutDate):
        time.sleep(0.25)
        AllWidgets = self.master.grid_slaves()

        #print(AllWidgets)
        #Only deletes required widgets (Entries and 2 buttons at bottom)
        for i in AllWidgets[0:13]:
            i.destroy()
        #renames window

        self.master.title('Booking Details')

        #Resizes window

        self.master.minsize(width=400, height=375)
        self.master.maxsize(width=400, height=375)

        #Displays booking details for staff to view.

        self.BookingIDlbl = Label(self.master, text='Booking ID: ', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=2, pady=3)
        self.BookingID = Label(self.master, text=BookingID, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=2, pady=3)

        self.CustIDlbl = Label(self.master, text='Customer ID:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=3, pady=3)
        self.CustID = Label(self.master, text=CustID, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=3, pady=3)

        self.RoomNumlbl = Label(self.master, text='Room number: ', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=4, pady=3)
        self.RoomNum = Label(self.master, text=RoomID, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=4, pady=3)

        self.RoomSleepsLbl = Label(self.master, text='Sleeps: ', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=5, pady=3)
        self.RoomSleeps = Label(self.master, text=Sleeps, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=5, pady=3)

        self.TotalCostlbl = Label(self.master, text='Total cost: ', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=6, pady=3)
        self.TotalCost = Label(self.master, text=('£', TotalCost), font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=6, pady=3)

        self.DurationOfStaylbl = Label(self.master, text='Duration of stay: ', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=7, pady=3)
        self.DurationOfStay = Label(self.master, text=(DurationOfStay, 'days'), font=('Calibri',12), bg='#85C1E9').grid(column=1, row=7, pady=3)

        self.CheckInDatelbl = Label(self.master, text='Check-In-Date: ', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=8, pady=3)
        self.CheckInDate = Label(self.master, text=CheckInDate, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=8, pady=3)

        self.CheckOutDatelbl = Label(self.master, text='Check-Out-Date: ', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=9, pady=3)
        self.CheckOutDate = Label(self.master, text=CheckOutDate, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=9, pady=3)

        if globalAccessLevel == 'Manager':
            self.CreateBackButtonManagerMenu(8)
        if globalAccessLevel == 'Reception':
            self. CreateBackButtonReceptionMenu(8)

    def ConfirmCust(self):
        time.sleep(0.25)
        self.CustomerID = CustIDVar.get()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            FetchCustomer = '''SELECT * FROM Customers WHERE CustID = ?'''
            c.execute(FetchCustomer, self.CustomerID)
            Customer = c.fetchall()
            if Customer is not '':
                messagebox.showinfo('Customer Found', Customer)

            else:
                messagebox.showerror('Error', 'Customer not found')()

    def CreateBackButtonManagerMenu(self, row):
        self.BackButton = Button(master, text='Exit', command=self.ManagerBack, font=('Calibri', 12), width=8).grid(column=0, row=row, pady=10)

    def CreateBackButtonReceptionMenu(self,row):
        self.BackButton = Button(master, text='Exit', command=self.ReceptionBack, font=('Calibri', 12), width=8).grid(column=0, row=row, pady=10)

    def ReceptionBack(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        GUICommand = RBS.BookingSettings(self.master, 400, 375, '#85C1E9', '#EBF5FB', 'Booking Settings', 'Reception')

        GUICommand.CreateNewBooking(RowCount)
        RowCount += 1
        GUICommand.ViewBooking(RowCount)
        RowCount += 1
        GUICommand.EditBooking(RowCount)
        GUICommand.ReceptionBack()

    def ManagerBack(self):
        AllWidgets = self.master.grid_slaves()
        RowCount = 1
        # Clears the window of widgets
        for i in AllWidgets:
            i.destroy()
        GUICommand = MBS.BookingSettings(self.master, 400, 375, '#85C1E9', '#EBF5FB', 'Booking Settings')

        GUICommand.CreateNewBooking(RowCount)
        RowCount += 1
        GUICommand.ViewBooking(RowCount)
        RowCount += 1
        GUICommand.EditBooking(RowCount)
        RowCount += 1
        GUICommand.DeleteBooking(RowCount)


if __name__ == '__main__':
    root = Tk()
    gui = AddBookingGUI(root, 450, 400, '#85C1E9', '#EBF5FB', 'Add Booking', 'Manager')
    root.mainloop()