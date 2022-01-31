import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import time

from datetime import datetime
from datetime import date
from datetime import timedelta


import sqlite3

from MainGUI import main
import ManagerBookingSettings as MBS

class EditBookingGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title, AccessLevel):
        self.master = master
        super().__init__(self.master, height, width, bgcolour, framecolour, title)

        master.title(title)

        global BookingIDVar, AttToEditVar, ReplacementDataVar, globalAccessLevel

        BookingIDVar = StringVar()
        AttToEditVar = StringVar()
        ReplacementDataVar = StringVar()

        globalAccessLevel = AccessLevel

        if globalAccessLevel == 'Manager':
            self.CreateBackButtonManagerMenu(12)
        if globalAccessLevel == 'Reception':
            self.CreateBackButtonReceptionMenu(12)

        BookingIDVar = StringVar()
        AttToEditList = ['CustID', 'RoomID', 'SpecialRequests', 'CheckInDate', 'CheckOutDate']

        AttToEditVar.set('None')

        self.BackButton = Button(self.master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=5, pady=10)

        self.IDlbl = Label(self.master, text='Booking ID: ', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=2, pady=3)
        self.IDEntry = Entry(self.master, text='....', textvariable=BookingIDVar, width=25).grid(column=1, row=2, pady=3)

        self.AttToEditlbl = Label(self.master, text='Attribute to edit:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=3, pady=3)
        self.AttToEdit = OptionMenu(self.master, AttToEditVar, *AttToEditList).grid(column=1, row=3, pady=3)

        self.ReplacementDatalbl = Label(self.master, text='Replace with:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=4, pady=3)
        self.ReplacementDataEntry = Entry(self.master, text='....', textvariable=ReplacementDataVar, width=25).grid(column=1, row=4, pady=3)

        self.EditAttBtn = Button(self.master, text='Edit', command=self.EditAtt, width=18, font=('Calibri', 12)).grid(column=1, row=5, pady=5)
        self.ConfirmBookingBtn = Button(self.master, text='Confirm Booking', font=('Calibri', 12), command=self.ConfirmBooking, width=18).grid(column=1, row=6, pady=3)

    def EditAtt(self):
        self.BookingID = BookingIDVar.get()
        self.AttToEdit = AttToEditVar.get()
        self.ReplacementData = ReplacementDataVar.get()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()

            if self.BookingID == '':
                messagebox.showerror('Error', 'BookingID Required')

            if self.AttToEdit == 'None':
                messagebox.showerror('Error', 'Attribute to edit required')

            if self.ReplacementData == '':
                messagebox.showerror('Replacement Data Required')

            if self.AttToEdit == 'CustID':
                if len(self.ReplacementData) > 0 < 3:
                    UpdateSql = '''UPDATE Booking SET CustID = ? WHERE BookingID = ?'''
                    values = (self.ReplacementData, self.BookingID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'CustID invalid')

            if self.AttToEdit == 'RoomID':
                if len(self.ReplacementData) > 0 < 3:
                    UpdateRoomIDSQL = '''UPDATE Booking SET RoomID = ? WHERE BookingID = ?'''
                    UpdateRoomIDValues = (self.ReplacementData, self.BookingID)
                    c.execute(UpdateRoomIDSQL, UpdateRoomIDValues)

                    UpdateRoomNumSQL = '''UPDATE Booking SET RoomNum = ? WHERE BookingID = ?'''
                    UpdateRoomNumValues = (self.ReplacementData, self.BookingID)
                    c.execute(UpdateRoomNumSQL, UpdateRoomNumValues)

                    #With the changing off rooms the cost per nights and total cost has to be updated to suit

                    #print(self.ReplacementData)
                    c.execute('''SELECT CostPerNight FROM Rooms WHERE RoomID = ?''', (self.ReplacementData,))
                    CostPerNight = str(c.fetchone())
                    #print(CostPerNight)

                    c.execute('''SELECT DurationOfStay FROM Booking WHERE BookingID = ?''', (self.BookingID))
                    DurationOfStay = str(c.fetchone())
                    #print(DurationOfStay)

                    for char in CostPerNight:
                        if char in "[](),'£":
                            CostPerNight = CostPerNight.replace(char, '')
                            #print(CostPerNight)

                    for char in DurationOfStay:
                        if char in "[](),'":
                            DurationOfStay = DurationOfStay.replace(char, '')
                            #print(DurationOfStay)

                    TotalCost = int(CostPerNight) * int(DurationOfStay)

                    UpdateCostPerNightSQL = '''UPDATE Booking SET CostPerNight = ? WHERE BookingID = ?'''
                    UpdateCostPerNightValues = (CostPerNight, self.BookingID)
                    c.execute(UpdateCostPerNightSQL, UpdateCostPerNightValues)

                    UpdateTotalCostSQL = '''UPDATE Booking SET TotalCost = ? WHERE BookingID = ?'''
                    UpdateTotalCostValues = (TotalCost, self.BookingID)
                    c.execute(UpdateTotalCostSQL, UpdateTotalCostValues)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'RoomID invalid')


            if self.AttToEdit == 'SpecialRequests':
                if len(self.ReplacementData) > 0 < 250:
                    UpdateSql = '''UPDATE Booking SET SpecialRequests = ? WHERE BookingID = ?'''
                    values = (self.ReplacementData, self.BookingID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'Special Requests invalid')

            if self.AttToEdit == 'CheckInDate':
                if len(self.ReplacementData) == 10:
                    date_format = "%d/%m/%Y"

                    UpdateCheckInDate = '''UPDATE Booking SET CheckInDate = ? WHERE BookingID = ?'''
                    UpdateCheckInDateValues = (self.ReplacementData, self.BookingID,)
                    c.execute(UpdateCheckInDate, UpdateCheckInDateValues)

                    GetBookingInfo = '''SELECT * FROM Booking WHERE BookingID = ?'''
                    BookingInfoValues = (self.BookingID)
                    c.execute(GetBookingInfo, BookingInfoValues)
                    BookingInfo = c.fetchone()
                    CheckOut = BookingInfo[10]
                    print(CheckOut)
                    CostPerNight = BookingInfo[6]
                    FormatedCheckOut = datetime.strptime(CheckOut, date_format)
                    FormatedCheckIn = datetime.strptime(self.ReplacementData, date_format)
                    DurationOfStay = FormatedCheckOut - FormatedCheckIn
                    TotalCost = CostPerNight * DurationOfStay.days


                    UpdateBookingInfo = '''UPDATE Booking SET (TotalCost, DurationOfStay) = (?,?) WHERE BookingID = ?'''
                    UpdateBookingInfoValues = (TotalCost, DurationOfStay.days, self.BookingID)
                    c.execute(UpdateBookingInfo, UpdateBookingInfoValues)
                    #print(FormatedCheckOut)
                    #print(FormatedCheckIn)
                    #print(DurationOfStay.days)
                    #print(CostPerNight)
                    db.commit()

            if self.AttToEdit == 'CheckOutDate':
                if len(self.ReplacementData) == 10:
                    date_format = "%d/%m/%Y"

                    UpdateCheckOutDate = '''UPDATE Booking SET CheckOutDate = ? WHERE BookingID = ?'''
                    UpdateCheckOutDateValues = (self.ReplacementData, self.BookingID,)
                    c.execute(UpdateCheckOutDate, UpdateCheckOutDateValues)

                    GetBookingInfo = '''SELECT * FROM Booking WHERE BookingID = ?'''
                    BookingInfoValues = (self.BookingID)
                    c.execute(GetBookingInfo, BookingInfoValues)
                    BookingInfo = c.fetchone()
                    CheckIn = BookingInfo[9]
                    CostPerNight = BookingInfo[6]
                    FormatedCheckIn = datetime.strptime(CheckIn, date_format)
                    FormatedCheckOut = datetime.strptime(self.ReplacementData, date_format)
                    DurationOfStay = FormatedCheckOut - FormatedCheckIn
                    TotalCost = int(CostPerNight) * DurationOfStay.days
                    #print(CostPerNight)
                    #print(TotalCost)
                    #print(DurationOfStay.days)
                    #print(FormatedCheckIn, FormatedCheckOut)

                    UpdateBookingInfo = '''UPDATE Booking SET (TotalCost, DurationOfStay) = (?,?) WHERE BookingID = ?'''
                    UpdateBookingInfoValues = (TotalCost, DurationOfStay.days, self.BookingID)
                    c.execute(UpdateBookingInfo, UpdateBookingInfoValues)
                    db.commit()

    def ConfirmBooking(self):
        self.BookingValue = BookingIDVar.get()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            BookingIDSQL = '''SELECT * FROM Booking WHERE BookingID = ?'''
            c.execute(BookingIDSQL, self.BookingValue)
            BookingData = c.fetchone()
            #print(BookingData)
            if BookingData[0] != '':
                self.DisplayBooking(BookingData[0], BookingData[1], BookingData[2], BookingData[3], BookingData[4],
                                    BookingData[5], BookingData[6], BookingData[7], BookingData[8], BookingData[9],
                                    BookingData[10])
            if BookingData == '':
                messagebox.showerror('Error', 'Booking Not Found')

    def DisplayBooking(self, BookingID, CustomerID, RoomID, BookingDate, RoomNum, SpecialReq, CostPerNight, TotalCost, DurationOfStay, CheckInDate, CheckOutDate):

        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets[0:4]:
            i.destroy()

        self.master.minsize(width=450, height=525)
        self.master.maxsize(width=450, height=525)

        self.BookingIDLbl = Label(self.master, text='Booking ID:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=2, pady=3)
        self.BookingID = Label(self.master, text=BookingID, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=2, pady=3)

        self.CustIDLbl = Label(self.master, text='Customer ID:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=3, pady=3)
        self.CustID = Label(self.master, text=CustomerID, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=3, pady=3)

        self.RoomIDlbl = Label(self.master, text='Room ID:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=4, pady=3)
        self.RoomID = Label(self.master, text=RoomID, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=4, pady=3)

        self.BookingDatelbl = Label(self.master, text='Booking Date:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=5, pady=3)
        self.BookingDate = Label(self.master, text=BookingDate, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=5, pady=3)

        self.RoomNumlbl = Label(self.master, text='Room Number:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=6, pady=3)
        self.RoomNum = Label(self.master, text=RoomNum, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=6, pady=3)

        self.SpecialReqlbl = Label(self.master, text='Special Requests:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=7, pady=3)
        self.SpecialReq = Label(self.master, text=SpecialReq, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=7, pady=3)

        self.CostPerNightlbl = Label(self.master, text='Cost-Per-Night:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=8, pady=3)
        self.CostPerNight = Label(self.master, text=('£', CostPerNight), font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=8, pady=3)

        self.TotalCostlbl = Label(self.master, text='Total Cost:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=9, pady=3)
        self.TotalCost = Label(self.master, text=('£', TotalCost), font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=9, pady=3)

        self.DurationOfStaylbl = Label(self.master, text='Duration-Of-Stay:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=10, pady=3)
        self.DurationOfStay = Label(self.master, text=(DurationOfStay, 'Days'), font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=10, pady=3)

        self.CheckInDatelbl = Label(self.master, text='Check-In-Date:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=11, pady=3)
        self.CheckInDate = Label(self.master, text=CheckInDate, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=11, pady=3)

        self.CheckOutDatelbl = Label(self.master, text='Check-Out-Date:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=12, pady=3)
        self.CheckOutDate = Label(self.master, text=CheckOutDate, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=12,pady=3)

        self.WrongBookingbtn = Button(self.master, text='Wrong Booking', command=self.WrongBooking, font=('Calibri', 12), width=18).grid(column=1, row=13)
        self.DeleteButtonbtn = Button(self.master, text='Delete Booking', command=self.DeleteBooking, font=('Calibri', 12), width=18).grid(column=1, row=14, pady=5)
        self.BackButton = Button(self.master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=13, pady=5)

        if globalAccessLevel == 'Manager':
            self.CreateBackButtonManagerMenu(13)
        if globalAccessLevel == 'Reception':
            self.CreateBackButtonReceptionMenu(13)

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
    gui = EditBookingGUI(root, 460, 475, '#85C1E9', '#EBF5FB', 'Edit Booking')
    root.mainloop()