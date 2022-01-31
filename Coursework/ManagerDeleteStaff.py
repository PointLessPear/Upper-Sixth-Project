import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import os
import time
import sqlite3

from MainGUI import main
import ManagerStaffSettings as MSS


class DeleteStaffGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        global StaffIDVar

        StaffIDVar = StringVar()

        self.StaffIDLabel = Label(self.master, text='Staff ID:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=2, pady=3)
        self.StaffIDEntry = Entry(self.master, text='....', textvariable=StaffIDVar, width=25).grid(column=1, row=2, pady=3)

        self.ConfirmStaffBtn = Button(self.master, text='Confirm Staff', command=self.DataValidation, font=('Calibri', 12), width=15).grid(column=1, row=3, pady=5)
        self.BackButton = Button(master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=3, pady=5)

    def DataValidation(self):

        StaffID = StaffIDVar.get()

        if StaffID == '':
            messagebox.showerror('Error', 'StaffID Requried')

        if len(StaffID) > 3:
            messagebox.showerror('Error', 'StaffID Invalid')

        self.ConfirmStaff(StaffID)

    def ConfirmStaff(self, StaffID):

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            GetStaffDetailsSQL = '''SELECT * FROM Staff WHERE StaffID = ?'''
            c.execute(GetStaffDetailsSQL, (StaffID,))

            StaffDetails = c.fetchone()

            self.DisplayStaffInfo(StaffDetails[0], StaffDetails[1], StaffDetails[2], StaffDetails[3], StaffDetails[4], StaffDetails[5], StaffDetails[6], StaffDetails[7], StaffDetails[8], StaffDetails[9], StaffDetails[10], StaffDetails[11], StaffDetails[12], StaffDetails[13], StaffDetails[14])

    def DisplayStaffInfo(self, StaffID, FirstName, Surname, MobileNum, TelephoneNum, Email, Address, PostCode, DOB, Gender, JobTitle, NIN, HourlyRate, ContractedHours, Username):

        AllWidgets = self.master.grid_slaves()
        #print(AllWidgets[0:10])
        for i in AllWidgets[0:4]:
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

        self.WrongStaffBtn = Button(self.master, text='Wrong StaffID', command=self.WrongStaff, font=('Calibri', 12), width=15).grid(column=3, row=10, pady=5)
        self.DeleteStaffBtn = Button(self.master, text='Delete', command=self.DeleteStaff, font=('Calibri', 12), width=15).grid(column=2, row=10, pady=5)
        self.BackButton = Button(self.master, text='Done', command=self.Back, font=('Calibri', 12), width=8).grid(column=1, row=10, pady=5)


    def DeleteStaff(self):

        self.StaffID = StaffIDVar.get()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            DeleteStaffSQL = '''DELETE FROM Staff WHERE StaffID = ?'''
            c.execute(DeleteStaffSQL, (self.StaffID,))

            messagebox.showinfo('Staff Member Deleted', 'Staff Member Deleted Succesfully')
            db.commit()

            AllWidgets = self.master.grid_slaves()

            for i in AllWidgets:
                i.destroy()

            DeleteStaffGUI(self.master, 500, 650, '#85C1E9', '#EBF5FB', 'Delete Staff')

    def WrongStaff(self):

        AllWidgets = self.master.grid_slaves()

        for i in AllWidgets:
            i.destroy()

        DeleteStaffGUI(self.master, 500, 650, '#85C1E9', '#EBF5FB', 'Delete Staff')

    def Back(self):
        AllWidgets = self.master.grid_slaves()
        # Clears the window of widgets
        for i in AllWidgets:
            i.destroy()
        MSS.ManagerStaffSettingsGUI(self.master, 500, 350, '#85C1E9', '#EBF5FB', 'Staff Settings')

if __name__ == '__main__':
    root = Tk()
    gui = DeleteStaffGUI(root, 500, 650, '#85C1E9', '#EBF5FB', 'Delete Staff')
    root.mainloop()