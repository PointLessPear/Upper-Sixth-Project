import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import time
import sqlite3

from MainGUI import main
import ManagerCustomerSettings as MCS


class DeleteCustGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):
        global CustIDVar
        CustIDVar = StringVar()

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.BackButton = Button(master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=4, pady=5)

        self.CustomerIDLabel = Label(self.master, text='Customer ID:', font=('Calibri', 12), bg=bgcolour).grid(row=2, column=0)
        self.CustomerIDEntry = Entry(self.master, text='....', textvariable=CustIDVar, width=25).grid(row=2, column=1)

        self.CustomerIDBtn = Button(self.master, text='Confirm Customer', command=self.ConfirmCustomer, font=('Calibri', 12), width=18, height=1).grid(row=4, column=1, pady=5)
        self.CustomerDeleteBtn = Button(self.master, text='Delete Customer', command=self.DeleteCustomer, font=('Calibri', 12), width=18, height=1).grid(row=5, column=1, pady=5)

    def ConfirmCustomer(self):
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

    def DeleteCustomer(self):
        time.sleep(0.25)
        self.CustomerID = CustIDVar.get()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            DeleteCustomer = '''DELETE FROM Customers WHERE CustID = ?'''
            c.execute(DeleteCustomer, self.CustomerID)

            db.commit()
            messagebox.showinfo('Customers Deleted', 'Customer succesfully deleted')

    def Back(self):
        # Clears the window of widgets
        RowCount = 1
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        GUIcommand = MCS.CustSettings(self.master, 450, 475, '#85C1E9', '#EBF5FB', 'Customer Settings')
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
        RowCount += 1
        GUIcommand.Backup(RowCount)

if __name__ == '__main__':
    root = Tk()
    gui = DeleteCustGUI(root, 350, 475, '#85C1E9', '#EBF5FB', 'Delete Customer')
    root.mainloop()