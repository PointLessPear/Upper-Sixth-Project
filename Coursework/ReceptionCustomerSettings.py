import tkinter as Tk
from tkinter import *

import time

from MainGUI import main
import AddBooking as AB
import ViewBooking as VB
import EditBooking as EB
import DeleteBooking as DB

import ReceptionMenu as RM

class CustSettings(main):
    def __init__(self, master, height, width, bgcolour, framecolour, title):

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.BackBtn = Button(self.master, text='Exit', command=self.Back, width=8, font=('Calibri', 12)).grid(column=0, row=1, pady=10)

    def ViewCust(self, RowCount):
        self.ViewCust = Button(self.master, text='View Booking', command=self.CreateViewCustGUI, width=18, pady=5, font=('Calibri', 12)).grid(column=1, row=RowCount + 1, pady=3)

    def CreateViewCustGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        time.sleep(0.25)
        ViewCustGUI(self.master, 300, 450, '#85C1E9', '#EBF5FB', 'View Customer', 'Reception')

    def EditCust(self, RowCount):
        self.EditCust = Button(self.master, text='Edit Customer Details', command=self.CreateEditCustGUI, width=18, pady=5, font=('Calibri', 12)).grid(column=1, row=RowCount + 1, pady=3)

    def CreateEditCustGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        time.sleep(0.25)
        EditCustGUI(self.master, 450, 475, '#85C1E9', '#EBF5FB', 'Edit Customer', 'Reception')

    def ChangeCustPassword(self, RowCount):
        self.RecoverPass = Button(self.master, text='Change Password', command=self.CreateChangeCustPassGUI,  width=18, pady=5, font=('Calibri', 12)).grid(column=1, row=RowCount + 1, pady=3)

    def CreateChangeCustPassGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        ChangeCustPassGUI(self.master, 400, 475, '#85C1E9', '#EBF5FB', 'Change Customer Password', 'Reception')

    def Back(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        RM.ReceptionMenu(self.master, 375, 350, '#85C1E9', '#EBF5FB', 'Reception Menu')




if __name__ == '__main__':
    root = Tk()

