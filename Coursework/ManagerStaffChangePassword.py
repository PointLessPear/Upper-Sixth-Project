import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import sqlite3
import hashlib
import binascii
import os

from MainGUI import main
import ManagerStaffSettings as MSS

class ChangeStaffPassword(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):
        global StaffUsernameVar, NewPasswordVar
        StaffUsernameVar = StringVar()
        NewPasswordVar = StringVar()

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.UsernameLbl = Label(self.master, text='Staff Username:', font=('Calibri', 12), bg=bgcolour).grid(row=2, column=0)
        self.UsernameEntry = Entry(self.master, text='....', textvariable=StaffUsernameVar, width=25).grid(row=2, column=1)

        self.ConfirmStaffButton = Button(self.master, command=self.ConfirmStaff,text='Confirm Staff', font=('Calibri', 12)).grid(row=4, column=1, pady=5)

        self.NewPasswordLbl = Label(self.master, text='New Passowrd:', font=('Calibri', 12), bg=bgcolour).grid(row=3, column=0)
        self.NewPasswordEntry = Entry(self.master, text='....', textvariable=NewPasswordVar, width=25).grid(row=3, column=1)
        self.NewPasswordBtn = Button(self.master, text='Change Password', command=self.ChangePassword, font=('Calibri', 12)).grid(row=5, column=1, pady=5)
        self.BackButton = Button(self.master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=5, pady=5)

    def ChangePassword(self):

        Username = StaffUsernameVar.get()
        NewPassword = NewPasswordVar.get()

        self.HashedPassword = self.hash_password(NewPassword)

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            UpdatePasswordSQL = '''UPDATE Staff SET Password = ? WHERE Username = ? '''
            Values = (self.HashedPassword, Username)
            c.execute(UpdatePasswordSQL, Values)

            db.commit()

    def ConfirmStaff(self):

        Username = StaffUsernameVar.get()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            GetStaffDetailsSQL = '''SELECT * FROM Staff WHERE Username = ?'''
            c.execute(GetStaffDetailsSQL, (Username,))

            StaffDetails = c.fetchone()

            self.DisplayStaffInfo(StaffDetails[0], StaffDetails[1], StaffDetails[2], StaffDetails[3], StaffDetails[4], StaffDetails[5], StaffDetails[6], StaffDetails[7], StaffDetails[8], StaffDetails[9], StaffDetails[10], StaffDetails[11], StaffDetails[12], StaffDetails[13], StaffDetails[14])

    def DisplayStaffInfo(self, StaffID, FirstName, Surname, MobileNum, TelephoneNum, Email, Address, PostCode, DOB, Gender, JobTitle, NIN, HourlyRate, ContractedHours, Username):

        AllWidgets = self.master.grid_slaves()
        #print(AllWidgets[0:10])
        for i in AllWidgets[0:5]:
            i.destroy()
        #for i in AllWidgets:

        self.StaffIDlbl = Label(self.master, text='Staff ID:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=2, pady=3)
        self.StaffID = Label(self.master, text=StaffID, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=2, pady=3)

        self.FirstNamelbl = Label(self.master, text='First Name:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=3, pady=3)
        self.FirstName = Label(self.master, text=FirstName, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=3, pady=3)

        self.Surnamelbl = Label(self.master, text='Surname:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=4, pady=3)
        self.Surname = Label(self.master, text=Surname, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=4, pady=3)

        self.Phonelbl = Label(self.master, text='Phone Number:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=5, pady=3)
        self.Phone = Label(self.master, text=MobileNum, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=5, pady=3)

        self.Telephonelbl = Label(self.master, text='Telephone Number:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=6, pady=3)
        self.Telephone =Label(self.master, text=TelephoneNum, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=6, pady=3)

        self.Emaillbl = Label(self.master, text='Email:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=7, pady=3)
        self.Email = Label(self.master, text=Email, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=7, pady=3)

        self.Addresslbl = Label(self.master, text='Address:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=8, pady=3)
        self.Address = Label(self.master, text=Address, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=8, pady=3)

        self.PostCodelbl = Label(self.master, text='PostCode:', font=('Calibri', 12), bg='#85C1E9').grid(column=0, row=9, pady=3)
        self.PostCode = Label(self.master, text=PostCode, font=('Calibri', 12), bg='#85C1E9').grid(column=1, row=9, pady=3)

        self.DOBlbl = Label(self.master, text='DOB:', font=('Calibri', 12), bg='#85C1E9').grid(column=2, row=2, pady=3)
        self.DOB = Label(self.master, text=DOB, font=('Calibri', 12), bg='#85C1E9').grid(column=3, row=2, pady=3)

        self.Genderlbl = Label(self.master, text='Gender:', font=('Calibri', 12), bg='#85C1E9').grid(column=2, row=3, pady=3)
        self.Gender = Label(self.master, text=Gender, font=('Calibri', 12), bg='#85C1E9').grid(column=3, row=3, pady=3)

        self.JobTitlelbl = Label(self.master, text='Job Title:', font=('Calibri', 12), bg='#85C1E9').grid(column=2, row=4, pady=3)
        self.JobTitle = Label(self.master, text=JobTitle, font=('Calibri', 12), bg='#85C1E9').grid(column=3, row=4, pady=3)

        self.NINlbl = Label(self.master, text='National Insurance:', font=('Calibri', 12), bg='#85C1E9').grid(column=2, row=5, pady=3)
        self.NIN = Label(self.master, text=NIN, font=('Calibri', 12), bg='#85C1E9').grid(column=3, row=5, pady=3)

        self.HourlyRatelbl = Label(self.master, text='Hourly Rate:', font=('Calibri', 12), bg='#85C1E9').grid(column=2, row=6, pady=3)
        self.HourlyRate = Label(self.master, text=('£', HourlyRate), font=('Calibri', 12), bg='#85C1E9').grid(column=3, row=6, pady=3)

        self.ContactedHourslbl = Label(self.master, text='Contracted Hours:', font=('Calibri', 12), bg='#85C1E9').grid(column=2, row=7, pady=3)
        self.ContractedHours = Label(self.master, text=(ContractedHours, 'Hours'), font=('Calibri', 12), bg='#85C1E9').grid(column=3, row=7, pady=3)

        self.Usernamelbl = Label(self.master, text='Username:', font=('Calibri', 12), bg='#85C1E9').grid(column=2, row=8, pady=3)
        self.Username = Label(self.master, text=Username, font=('Calibri', 12), bg='#85C1E9').grid(column=3, row=8, pady=3)

        self.ViewAnotherBtn = Button(self.master, text='Done', command=self.Confirmed, font=('Calibri', 12), width=15).grid(column=2, row=10, pady=5)
        self.BackButton = Button(self.master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=1, row=10, pady=5)

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)

        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def Confirmed(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        ChangeStaffPassword(self.master, 500, 650, '#85C1E9', '#EBF5FB', 'Change Staff Password')

    def Back(self):
        AllWidgets = self.master.grid_slaves()
        # Clears the window of widgets
        for i in AllWidgets:
            i.destroy()
        MSS.ManagerStaffSettingsGUI(self.master, 500, 350, '#85C1E9', '#EBF5FB', 'Staff Settings')

if __name__ == '__main__':
    root = Tk()
    gui = ChangeStaffPassword(root, 500, 650, '#85C1E9', '#EBF5FB', 'Change Staff Password')
    root.mainloop()