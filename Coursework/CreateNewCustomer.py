import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import time
import sqlite3
import hashlib
import binascii
import os

from MainGUI import main
import ManagerCustomerSettings as MCS


class NewCustGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):
        global FirstNameVar, SurnameVar, PhoneVar, EmailVar, AddressVar, PostCodeVar, DOBVar, GenderVar, PasswordVar, UsernameVar
        FirstNameVar = StringVar()
        SurnameVar = StringVar()
        PhoneVar = StringVar()
        EmailVar = StringVar()
        AddressVar = StringVar()
        PostCodeVar = StringVar()
        DOBVar = StringVar()
        PasswordVar = StringVar()
        UsernameVar = StringVar()

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.BackButton = Button(master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=12, pady=5)

        #Variable for gender dropdown
        GenderVar = StringVar(self.master)
        #Choices and default option for gender dropdown
        GenderChoices = ['Male', 'Female', 'Other']
        GenderVar.set('....')

        #Intalises all Labels, Entries, OptionMenus and Buttons

        self.FirstNamelbl = Label(self.master, text='First Name:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=2)
        self.FirstNameEntry = Entry(self.master, text='....', textvariable=FirstNameVar, width=25).grid(column=1, row=2)

        self.Surnamelbl = Label(self.master, text='Surname:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=3)
        self.SurnameEntry = Entry(self.master, text='....', textvariable=SurnameVar, width=25).grid(column=1, row=3)

        self.Phonelbl = Label(self.master, text='Phone number:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=4)
        self.PhoneEntry = Entry(self.master, text='....', textvariable=PhoneVar, width=25).grid(column=1, row=4)

        self.Emaillbl = Label(self.master, text='Email:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=5)
        self.EmailEntry = Entry(self.master, text='....', textvariable=EmailVar, width=25).grid(column=1, row=5)

        self.Addresslbl = Label(self.master, text='Address:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=6)
        self.AddressEntry = Entry(self.master, text='....', textvariable=AddressVar, width=25).grid(column=1, row=6)

        self.PostCodelbl = Label(self.master, text='PostCode:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=7)
        self.PostCodeEntry = Entry(self.master, text='....', textvariable=PostCodeVar, width=25).grid(column=1, row=7)

        self.DOBlbl = Label(self.master, text='DOB:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=8)
        self.DOBEntry = Entry(self.master, text='....', textvariable=DOBVar, width=25).grid(column=1, row=8)

        self.GenderVar = Label(self.master, text='Gender:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=9)
        self.GenderDropdown = OptionMenu(self.master, GenderVar, *GenderChoices).grid(column=1, row=9)

        self.Passwordlbl = Label(self.master, text='Password:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=10)
        self.PasswordEntry = Entry(self.master, text='....', show='*', textvariable=PasswordVar, width=25).grid(column=1, row=10)

        self.Usernamelbl = Label(self.master, text='Username:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=11)
        self.UsernameEntry = Entry(self.master, text='....', textvariable=UsernameVar, width=25).grid(column=1, row=11)

        self.ContinueBtn = Button(self.master, text='Register', command=self.DataValidation, width=18, font=('Calibri', 12)).grid(column=1, row=12, pady=5)

    def DataValidation(self):
        self.FirstName = FirstNameVar.get()
        self.Surname = SurnameVar.get()
        self.PhoneNumber = PhoneVar.get()
        self.Email = EmailVar.get()
        self.Address = AddressVar.get()
        self.PostCode = PostCodeVar.get()
        self.DOB = DOBVar.get()
        self.Gender = GenderVar.get()
        self.Username = UsernameVar.get()
        self.Password = PasswordVar.get()


        #Presence Checks
        if self.FirstName == '':
            messagebox.showerror('Error', 'Firstname is required')

        if self.Surname == '':
            messagebox.showerror('Error', 'Surname is required')

        if self.PhoneNumber == '':
            messagebox.showerror('Error', 'Phone number is required')

        if self.Email == '':
            messagebox.showerror('Error', 'Email is required')

        if self.Address == '':
            messagebox.showerror('Error', 'Address is required')

        if self.PostCode == '':
            messagebox.showerror('Error', 'Post code is required')

        if self.DOB == '':
            messagebox.showerror('Error', 'Date Of Birth is required')

        if self.Username == '':
            messagebox.showerror('Error', 'Username is required')

        if self.Password == '':
            messagebox.showerror('Error', 'Password is required')

        #Length Checks
        if len(self.FirstName) > 0 and len(self.FirstName) < 20:
            self.FirstName = self.FirstName
        else:
            messagebox.showerror('Error', 'First Name invalid')

        if len(self.Surname) > 0 and len(self.Surname) < 20:
            self.Surname = self.Surname
        else:
            messagebox.showerror('Error', 'Surname invalid')

        if len(self.PhoneNumber) == 11:
            self.PhoneNumber = self.PhoneNumber
        else:
            messagebox.showerror('Error', 'Phone number invalid')

        if len(self.Email) > 0 and  len(self.Email) < 30:
            self.Email = self.Email
        else:
            messagebox.showerror('Error', ' Email address invalid')

        if len(self.Address) > 0 and len(self.Address) < 50:
            self.Address = self.Address
        else:
            messagebox.showerror('Error', 'Address invalid')

        if len(self.PostCode) == 8:
            self.PostCode = self.PostCode
        else:
            messagebox.showerror('Error', 'Postcode invalid')

        if len(self.DOB) == 8:
            self.DOB == self.DOB
        else:
            messagebox.showerror('Error', 'Date of birth invalid')

        if len(self.Username) > 10 and len(self.Username) < 30:
            self.Username = self.Username
        else:
            messagebox.showerror('Error', 'Username invalid')

        if len(self.Password) > 10 and len(self.Username) < 30:
            self.Password = self.Password
        else:
            messagebox.showerror('Error', 'Password invalid')

        self.FetchInput(self.FirstName, self.Surname, self.PhoneNumber, self.Email, self.Address, self.PostCode, self.DOB, self.Gender, self.Password, self.Username)

    def FetchInput(self, FirstName, Surname, PhoneNumber, Email, Address, PostCode, DOB, Gender, Password, Username):
        #Encrypts password
        self.HashedPassword = self.hash_password(Password)


        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            sql = '''INSERT INTO Customers (FirstName, Surname, Phone, Email, Address, PostCode, DOB, Gender, Password, Username) VALUES(?,?,?,?,?,?,?,?,?,?)'''
            Values = (FirstName, Surname, PhoneNumber, Email, Address, PostCode, DOB, Gender, self.HashedPassword, Username)
            c.execute(sql, Values)
            db.commit()


        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            CustIDSQL = '''SELECT * FROM Customers WHERE Phone = ?'''
            PhoneValues = PhoneNumber
            c.execute(CustIDSQL, PhoneValues)
            CustID = c.fetchall()
            messagebox.showinfo('Customer ID', CustID)


    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)

        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

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
    gui = NewCustGUI(root, 425, 375, '#85C1E9', '#EBF5FB', 'Register')
    root.mainloop()
