import tkinter as Tk
from tkinter import *

from MainGUI import main

import ManagerCustomerSettings as MCS
import ManagerStaffSettings as MSS
import ManagerBookingSettings as MBS
import ManagerBackups as MB
import Login as l

class OwnerMenu(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):
        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)

        self.BackButton = Button(master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=1, pady=10)

        master.title(title)

        self.OwnerCustSettings = Button(master, text='Customer Settings', command=self.CustSettings, width=18, pady=5, font=('Calibri', 12)).grid(row=4, column=1, pady=3)
        self.OwnerBookingSettings = Button(master, text='Booking Settings', command=self.BookingSettings, width=18, pady=5, font=('Calibri', 12)).grid(row=5, column=1, pady=3)
        self.OwnerStaffSettings = Button(master, text='Staff Settings', command=self.StaffSettings, width=18, pady=5, font=('calibri', 12)).grid(row=6, column=1, pady=3)
        self.OwnerBackup = Button(master, text='Backups', command=self.BackupSettings, width=18, pady=5, font=('Calibri', 12)).grid(row=7, column=1, pady=3)

    def CustSettings(self):
        AllWidgets = self.master.grid_slaves()
        RowCount = 1
        # Clears the window of widgets
        for i in AllWidgets:
            i.destroy()
        GUIcommand = MCS.CustSettings(self.master, 450, 375, '#85C1E9', '#EBF5FB', 'Customer Settings')
        # Only calling the required widgets to the window

        GUIcommand.CreateNewCust(RowCount)
        RowCount += 1
        GUIcommand.ViewCust(RowCount)
        RowCount += 1
        GUIcommand.EditCust(RowCount)
        RowCount += 1
        GUIcommand.DeleteCust(RowCount)
        RowCount += 1
        GUIcommand.ChangeCustPassword(RowCount)

    def StaffSettings(self):
        AllWidgets = self.master.grid_slaves()
        # Clears the window of widgets
        for i in AllWidgets:
            i.destroy()
        MSS.ManagerStaffSettingsGUI(self.master, 500, 400, '#85C1E9', '#EBF5FB', 'Staff Settings')

    def BookingSettings(self):
        AllWidgets = self.master.grid_slaves()
        RowCount = 1
        # Clears the window of widgets
        for i in AllWidgets:
            i.destroy()
        GUICommand = MBS.BookingSettings(self.master, 400, 375,'#85C1E9', '#EBF5FB', 'Booking Settings')

        GUICommand.CreateNewBooking(RowCount)
        RowCount += 1
        GUICommand.ViewBooking(RowCount)
        RowCount += 1
        GUICommand.EditBooking(RowCount)
        RowCount += 1
        GUICommand.DeleteBooking(RowCount)

        GUICommand.ManagerBack()


    def BackupSettings(self):
        for i in AllWidgets:
            i.destroy()
        l.login(self.master, 300, 475, '#85C1E9', '#EBF5FB', 'Staff Login')

    def Back(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        l.login(self.master, 300, 475, '#85C1E9', '#EBF5FB', 'Staff Login')


if __name__ == '__main__':
    root = Tk()
    gui = OwnerMenu(root, 350, 375, '#85C1E9', '#EBF5FB', 'Manager Menu')
    root.mainloop()

    #for testing this module