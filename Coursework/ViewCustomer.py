import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import sqlite3
import time

from MainGUI import main
import ManagerCustomerSettings as MCS



class ViewCustGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):

        global CustomerIDVar
        CustomerIDVar = StringVar()

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.BackButton = Button(master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=3, pady=5)

        self.CustomerIDLabel = Label(self.master, text='Customer ID', font=('Calibri', 12), bg=bgcolour).grid(row=2, column=0)
        self.CustomerIDEntry = Entry(self.master, text='....', textvariable=CustomerIDVar, width=25).grid(row=2, column=1)

        self.ViewCustBtn = Button(self.master, text='View Customer', command=self.FindCust, height=1, width=18, font=('Calibri', 12)).grid(column=1, row=3, pady=5)



    def FindCust(self):
        time.sleep(0.25)
        self.CustomerID = CustomerIDVar.get()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            FetchCustomer = '''SELECT * FROM Customers WHERE CustID = ?'''
            c.execute(FetchCustomer, self.CustomerID)
            Customer = c.fetchall()
            if Customer is not '':
                messagebox.showinfo('Customer Found', Customer)

            else:
                messagebox.showerror('Error', 'Customer not found')

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

if __name__ == '__main__':
    root = Tk()
    gui = ViewCustGUI(root, 300, 450, '#85C1E9', '#EBF5FB', 'View Customer')
    root.mainloop()