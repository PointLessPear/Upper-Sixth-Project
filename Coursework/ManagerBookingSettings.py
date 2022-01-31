import tkinter as Tk
from tkinter import *

import time

from MainGUI import main
import AddBooking as AB
import ViewBooking as VB
import EditBooking as EB
import DeleteBooking as DB

import ManagerMenu as MM

class BookingSettings(main):
    def __init__(self, master, height, width, bgcolour, framecolour, title):

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.BackBtn = Button(self.master, text='Exit', command=self.ManagerBack, width=8, font=('Calibri', 12)).grid(column=0, row=1, pady=10)

    def CreateNewBooking(self, RowCount):
        self.CreateNewBookingBtn = Button(self.master, text='Add Booking', command=self.CreateNewBookingGUI, width=18, pady=5, font=('Calibri', 12)).grid(column=1, row=RowCount + 1, pady=3)

    def CreateNewBookingGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        time.sleep(0.25)
        AB.AddBookingGUI(self.master, 450, 400, '#85C1E9', '#EBF5FB', 'Add Booking', 'Manager')

    def ViewBooking(self, RowCount):
        self.ViewBookingBtn = Button(self.master, text='View Booking', command=self.CreateViewBookingGUI, width=18, pady=5, font=('Calibri', 12)).grid(column=1, row=RowCount + 1, pady=3)

    def CreateViewBookingGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        time.sleep(0.25)
        VB.ViewBookingGUI(self.master, 300, 450, '#85C1E9', '#EBF5FB', 'View Booking', 'Manager')

    def EditBooking(self, RowCount):
        self.EditBookingBtn = Button(self.master, text='Edit Booking', command=self.CreateEditBookingGUI, width=18, pady=5, font=('Calibri', 12)).grid(column=1, row=RowCount + 1, pady=3)

    def CreateEditBookingGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        time.sleep(0.25)
        EB.EditBookingGUI(self.master, 450, 475, '#85C1E9', '#EBF5FB', 'Edit Booking', 'Manager')

    def DeleteBooking(self, RowCount):
        self.DeleteBookingGUI = Button(self.master, text='Delete Booking', command=self.CreateDeleteBookingGUI, width=18, pady=5, font=('Calibri', 12)).grid(column=1, row=RowCount + 1, pady=3)

    def CreateDeleteBookingGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        DB.DeleteBookingGUI(self.master, 450, 525, '#85C1E9', '#EBF5FB', 'Delete Booking', 'Manager')

    def ManagerBack(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        MM.OwnerMenu(self.master, 375, 350, '#85C1E9', '#EBF5FB', 'Manager Menu')