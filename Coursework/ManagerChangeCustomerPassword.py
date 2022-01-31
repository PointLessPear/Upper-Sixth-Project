import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import sqlite3
import hashlib
import binascii
import os

from MainGUI import main

class ChangeCustPassGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):
        global CustomerIDVar, NewPasswordVar
        CustomerIDVar = StringVar()
        NewPasswordVar = StringVar()

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.CustomerIDLabel = Label(self.master, text='Customer ID:', font=('Calibri', 12), bg=bgcolour).grid(row=2, column=0)
        self.CustomerIDEntry = Entry(self.master, text='....', textvariable=CustomerIDVar, width=25).grid(row=2, column=1)

        self.CustomerIDBtn = Button(self.master, command=self.ConfirmCustomer,text='Confirm Customer', font=('Calibri', 12)).grid(row=4, column=1, pady=5)

        self.NewPasswordLbl = Label(self.master, text='New Passowrd:', font=('Calibri', 12), bg=bgcolour).grid(row=3, column=0)
        self.NewPasswordEntry = Entry(self.master, text='....', textvariable=NewPasswordVar, width=25).grid(row=3, column=1)
        self.NewPasswordBtn = Button(self.master, text='Change Password', command=self.ChangePassword, font=('Calibri', 12)).grid(row=5, column=1, pady=5)

    def ConfirmCustomer(self):
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

    def ChangePassword(self):
        self.CustomerID = CustomerIDVar.get()
        self.NewPassword = NewPasswordVar.get()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            GetOldPassSQL = '''SELECT Password FROM Customers WHERE CustID = ?'''
            c.execute(GetOldPassSQL, self.CustomerID)
            self.OldPass = c.fetchall()
            salt = os.urandom(32)
            self.HashedPassword = self.hash_password(self.NewPassword)

            ChangePassSQL = '''UPDATE Customers SET Password = ? WHERE CustID = ?'''
            NewPassValues = (self.HashedPassword, self.CustomerID)
            c.execute(ChangePassSQL, NewPassValues)

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)

        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')


    def Back(self):
        AllWidgets = self.master.grid_slaves()
        # Clears the window of widgets
        for i in AllWidgets:
            i.destroy()
        MSS.ManagerStaffSettingsGUI(self.master, 500, 350, '#85C1E9', '#EBF5FB', 'Staff Settings')


if __name__ == '__main__':
    root = Tk()
    gui = ChangeCustPassGUI(root, 400, 475, '#85C1E9', '#EBF5FB', 'Change Password')
    root.mainloop()