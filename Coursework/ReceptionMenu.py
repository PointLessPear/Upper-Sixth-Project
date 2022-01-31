import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import os
import time

from MainGUI import main

import ReceptionCustomerSettings as RCS
import ReceptionBookingSettings as RBS
import Login as l

class ReceptionMenu(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):
        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.BackButton = Button(master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=1, pady=10)

        self.CustomerSettings = Button(master, text='Customer Settings', command=self.CreateCustomerSettingsGUI, font=('Calibri', 12), width=18, pady=5).grid(column=1, row=2, pady=3)
        self.BookingSettings = Button(master, text='Booking Settings', command=self.CreateBookingSettingsGUI, font=('Calibri', 12), width=18, pady=5).grid(column=1, row=3, pady=3)
        self.StaffSettings = Button(master, text='Staff Settings', command=self.CreateStaffSettingsGUI, font=('Calibri', 12), width=18, pady=5).grid(column=1, row=4, pady=3)

    def CreateCustomerSettingsGUI(self):
        AllWidgets = self.master.grid_slaves()
        RowCount = 1
        # Clears the window of widgets
        for i in AllWidgets:
            i.destroy()
        GUIcommand = RCS.CustSettings(self.master, 450, 375, '#85C1E9', '#EBF5FB', 'Customer Settings')
        # Only calling the required widgets to the window

        GUIcommand.ViewCust(RowCount)
        RowCount += 1
        GUIcommand.EditCust(RowCount)
        RowCount += 1
        GUIcommand.ChangeCustPassword(RowCount)
        GUIcommand.ReceptionBack()

    def CreateBookingSettingsGUI(self):
        AllWidgets = self.master.grid_slaves()
        RowCount = 1
        # Clears the window of widgets
        for i in AllWidgets:
            i.destroy()
        GUICommand = RBS.BookingSettings(self.master, 400, 375, '#85C1E9', '#EBF5FB', 'Booking Settings')

        GUICommand.CreateNewBooking(RowCount)
        RowCount += 1
        GUICommand.ViewBooking(RowCount)
        RowCount += 1
        GUICommand.EditBooking(RowCount)
        GUICommand.ReceptionBack()

    def CreateStaffSettingsGUI(self):
        print

    def Back(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()



if __name__ == '__main__':
    root = Tk()
    gui = ReceptionMenu(root, 350, 375, '#85C1E9', '#EBF5FB', 'Reception Menu')
    root.mainloop()