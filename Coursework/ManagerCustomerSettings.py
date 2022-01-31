import tkinter as Tk
from tkinter import *

import time

from MainGUI import main
from CreateNewCustomer import NewCustGUI
from ViewCustomer import ViewCustGUI
from EditCustomer import EditCustGUI
from DeleteCustomer import DeleteCustGUI
from ManagerChangeCustomerPassword import ChangeCustPassGUI


import ManagerMenu as MM

class CustSettings(main):
    def __init__(self, master, height, width, bgcolour, framecolour, title):

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.BackButton = Button(master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=1, pady=10)

    def CreateNewCust(self, RowCount):
        self.CreateNewCustBtt = Button(self.master, text='Register Customer', command=self.CreateNewCustGUI, width=18, pady=5, font=('Calibri', 12)).grid(column=1, row=RowCount + 1, pady=3)

    def CreateNewCustGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        time.sleep(0.25)
        NewCustGUI(self.master, 450, 475, '#85C1E9', '#EBF5FB', 'Register')

    def ViewCust(self, RowCount):
        self.ViewCust = Button(self.master, text='View Booking', command=self.CreateViewCustGUI, width=18, pady=5, font=('Calibri', 12)).grid(column=1, row=RowCount + 1, pady=3)

    def CreateViewCustGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        time.sleep(0.25)
        ViewCustGUI(self.master, 300, 450, '#85C1E9', '#EBF5FB', 'View Customer')

    def EditCust(self, RowCount):
        self.EditCust = Button(self.master, text='Edit Customer Details', command=self.CreateEditCustGUI, width=18, pady=5, font=('Calibri', 12)).grid(column=1, row=RowCount + 1, pady=3)

    def CreateEditCustGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        time.sleep(0.25)
        EditCustGUI(self.master, 450, 475, '#85C1E9', '#EBF5FB', 'Edit Customer')

    def DeleteCust(self, RowCount):
        self.DeleteCust = Button(self.master, text='Delete Customer', command=self.CreateDeleteCustGUI, width=18, pady=5, font=('Calibri', 12)).grid(column=1, row=RowCount + 1, pady=3)

    def CreateDeleteCustGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        DeleteCustGUI(self.master, 450, 475, '#85C1E9', '#EBF5FB', 'Delete Customer')

    def ChangeCustPassword(self, RowCount):
        self.RecoverPass = Button(self.master, text='Change Password', command=self.CreateChangeCustPassGUI,  width=18, pady=5, font=('Calibri', 12)).grid(column=1, row=RowCount + 1, pady=3)

    def CreateChangeCustPassGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        ChangeCustPassGUI(self.master, 400, 475, '#85C1E9', '#EBF5FB', 'Change Customer Password')

    def Back(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        MM.OwnerMenu(self.master, 375, 350, '#85C1E9', '#EBF5FB', 'Owner Menu')


if __name__ == '__main__':
    root = Tk()
    gui = CustSettings(root, 400, 350, '#85C1E9', '#EBF5FB', 'Customer Settings')
    gui.CreateNewCust(1)
    root.mainloop()
