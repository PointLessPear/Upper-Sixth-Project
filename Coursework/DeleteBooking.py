import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import time
import sqlite3

from MainGUI import main
import ManagerBookingSettings as MBS

class DeleteBookingGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title, AccessLevel):
        self.master = master
        super().__init__(self.master, height, width, bgcolour, framecolour, title)

        master.title(title)

        global BookingIDVar, globalAccessLevel
        BookingIDVar = StringVar()


        globalAccessLevel = AccessLevel

        if globalAccessLevel == 'Manager':
            self.CreateBackButtonManagerMenu(3)

        self.IDlbl = Label(self.master, text='Booking ID: ', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=2, pady=3)
        self.IDEntry = Entry(self.master, text='....', textvariable=BookingIDVar, width=25).grid(column=1, row=2, pady=3)

        self.ConfirmBookingBtn = Button(self.master, text='Confirm Booking', font=('Calibri', 12), command=self.ConfirmBooking, width=18).grid(column=1, row=3, pady=3)

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


        if globalAccessLevel == 'Manager':
            self.CreateBackButtonManagerMenu(13)

    def WrongBooking(self):

        AllWidgets = self.master.grid_slaves()

        for i in AllWidgets:
            i.destroy()

        DeleteBookingGUI(self.master, 450, 475, '#85C1E9', '#EBF5FB', 'Delete Booking')

    def DeleteBooking(self):
        self.BookingID = BookingIDVar.get()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            DeleteBookingSQL = '''DELETE FROM Booking WHERE BookingID = ?'''
            c.execute(DeleteBookingSQL, self.BookingID)

            messagebox.showinfo('Booking Deleted', 'Booking Deleted Succesfully')
            db.commit()

            AllWidgets = self.master.grid_slaves()

            for i in AllWidgets:
                i.destroy()

            time.sleep(0.25)
            DeleteBookingGUI(self.master, 450, 525, '#85C1E9', '#EBF5FB', 'Delete Booking', 'Manager')


    def CreateBackButtonManagerMenu(self, row):
        self.BackButton = Button(master, text='Exit', command=self.ManagerBack, font=('Calibri', 12), width=8).grid(column=0, row=row, pady=10)

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
    gui = DeleteBookingGUI(root, 450, 500, '#85C1E9', '#EBF5FB', 'Delete Booking', 'Manager')
    root.mainloop()