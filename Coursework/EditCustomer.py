import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import time
import sqlite3

from MainGUI import main
import ManagerCustomerSettings as MCS


class EditCustGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title, AccessLevel):

        global CustomerIDVar, ReplaceWith, AttToEdit, globalAccessLevel
        CustomerIDVar = StringVar()
        ReplaceWith = StringVar()
        AttToEdit = StringVar()

        globalAccessLevel = AccessLevel

        if globalAccessLevel == 'Manager':
            self.CreateBackButtonManagerMenu(12)
        if globalAccessLevel == 'Reception':
            self. CreateBackButtonReceptionMenu(12)

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.CustomerIDLabel = Label(self.master, text='Customer ID:', font=('Calibri', 12), bg=bgcolour).grid(row=2, column=0)
        self.CustomerIDEntry = Entry(self.master, text='....', textvariable=CustomerIDVar, width=25).grid(row=2, column=1)

        self.FirstNameRadio = Radiobutton(self.master, text="First Name", variable=AttToEdit, value='FirstName',font=('Calibri', 12), bg=bgcolour).grid(row=3, column=1)
        self.SurNameRadio = Radiobutton(self.master, text="Surname", variable=AttToEdit, value='Surname',font=('Calibri', 12), bg=bgcolour).grid(row=4, column=1)
        self.PhoneRadio = Radiobutton(self.master, text="Phone", variable=AttToEdit, value='Phone', font=('Calibri', 12),  bg=bgcolour).grid(row=5, column=1)
        self.EmailRadio = Radiobutton(self.master, text="Email", variable=AttToEdit, value='Email', font=('Calibri', 12), bg=bgcolour).grid(row=6, column=1)
        self.AddressRadio = Radiobutton(self.master, text="Address", variable=AttToEdit, value='Address', font=('Calibri', 12), bg=bgcolour).grid(row=7, column=1)
        self.PostCodeRadio = Radiobutton(self.master, text="Postcode", variable=AttToEdit, value='PostCode', font=('Calibri', 12), bg=bgcolour).grid(row=8, column=1)
        self.DOBRadio = Radiobutton(self.master, text="DOB", variable=AttToEdit, value='DOB', font=('Calibri', 12), bg=bgcolour).grid(row=9, column=1)

        self.ReplaceWithLbl = Label(self.master, text='Replace With:', font=('Calibri', 12), bg=bgcolour).grid(row=11, column=0)
        self.ReplaceWithEntry = Entry(self.master, textvariable=ReplaceWith, width=25).grid(row=11, column=1)

        self.ConfirmCustBtn = Button(self.master, text='Confirm Customer', command=self.ConfirmCust, font=('Calibri', 12), width=15).grid(row=12, column=1, pady=5)
        self.EditBtn = Button(self.master, text='Edit', command=self.EditCust, font=('Calibri', 12), width=15).grid(row=13, column=1, pady=5)


    def ConfirmCust(self):
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
                messagebox.showerror('Error', 'Customer not found')()

    def EditCust(self):
        self.CustomerID = CustomerIDVar.get()
        self.AttToEdit = AttToEdit.get()
        self.ReplaceWith = ReplaceWith.get()
        #print(self.AttToEdit)

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()

            if self.AttToEdit == 'FirstName':
                UpdateSql = '''UPDATE Customers SET FirstName = ? WHERE CustID = ?'''
                values = (self.ReplaceWith, self.CustomerID)
                c.execute(UpdateSql, values)
                db.commit()

            if self.AttToEdit == 'Surname':
                UpdateSql = '''UPDATE Customers SET Surname = ? WHERE CustID = ?'''
                values = (self.ReplaceWith, self.CustomerID)
                c.execute(UpdateSql, values)
                db.commit()

            if self.AttToEdit == 'Phone':
                UpdateSql = '''UPDATE Customers SET Phone = ? WHERE CustID = ?'''
                values = (self.ReplaceWith, self.CustomerID)
                c.execute(UpdateSql, values)
                db.commit()

            if self.AttToEdit == 'Email':
                UpdateSql = '''UPDATE Customers SET Email = ? WHERE CustID = ?'''
                values = (self.ReplaceWith, self.CustomerID)
                c.execute(UpdateSql, values)
                db.commit()

            if self.AttToEdit == 'Addess':
                UpdateSql = '''UPDATE Customers SET Address = ? WHERE CustID = ?'''
                values = (self.ReplaceWith, self.CustomerID)
                c.execute(UpdateSql, values)
                db.commit()

            if self.AttToEdit == 'PostCode':
                UpdateSql = '''UPDATE Customers SET PostCode = ? WHERE CustID = ?'''
                values = (self.ReplaceWith, self.CustomerID)
                c.execute(UpdateSql, values)
                db.commit()

            if self.AttToEdit == 'DOB':
                UpdateSql = '''UPDATE Customers SET FirstName = ? WHERE CustID = ?'''
                values = (self.ReplaceWith, self.CustomerID)
                c.execute(UpdateSql, values)
                db.commit()

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
    gui = EditCustGUI(root, 450, 450, '#85C1E9', '#EBF5FB', 'Edit Customer')
    root.mainloop()