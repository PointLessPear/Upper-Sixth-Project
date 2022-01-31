import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import time
import sqlite3
import hashlib
import binascii
import os

from MainGUI import main
import ManagerStaffSettings as MSS


class AddStaffGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        global FirstNameVar, SurnameVar, MobileNumVar, TelephoneNumVar, EmailVar, AddressVar, PostCodeVar, DOBVar, GenderVar, JobTitleVar, NINVar, ContractedHoursVar, UsernameVar, PasswordVar

        FirstNameVar = StringVar()
        SurnameVar = StringVar()
        MobileNumVar = StringVar()
        TelephoneNumVar = StringVar()
        EmailVar = StringVar()
        AddressVar = StringVar()
        PostCodeVar = StringVar()
        DOBVar = StringVar()
        NINVar = StringVar()
        ContractedHoursVar = IntVar()
        UsernameVar = StringVar()
        PasswordVar = StringVar()

        #calc password hash from usernames ascii value
        #Jobtitle == dropdown
        JobTitleVar = StringVar(self.master)
        JobTitleChoices = ['Owner', 'Manager', 'Receptionist', 'Concierge']
        JobTitleVar.set('......')

        #Variable for gender dropdown
        GenderVar = StringVar(self.master)
        #Choices and default option for gender dropdown
        GenderChoices = ['Male', 'Female', 'Other']
        GenderVar.set('......')

        #Intalises all Labels, Entries, OptionMenus and Buttons

        self.FirstNamelbl = Label(self.master, text='First Name:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=2, pady=3)
        self.FirstNameEntry = Entry(self.master, text='....', textvariable=FirstNameVar, width=25).grid(column=1, row=2, pady=3)

        self.Surnamelbl = Label(self.master, text='Surname:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=3, pady=3)
        self.SurnameEntry = Entry(self.master, text='....', textvariable=SurnameVar, width=25).grid(column=1, row=3, pady=3)

        self.Phonelbl = Label(self.master, text='Phone Number:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=4, pady=3)
        self.PhoneEntry = Entry(self.master, text='....', textvariable=MobileNumVar, width=25).grid(column=1, row=4, pady=3)

        self.Telephonelbl = Label(self.master, text='Telephone Number:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=5, pady=3)
        self.TelephoneEntry = Entry(self.master, text='....', textvariable=TelephoneNumVar, width=25).grid(column=1, row=5, pady=3)

        self.Emaillbl = Label(self.master, text='Email:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=6, pady=3)
        self.EmailEntry = Entry(self.master, text='....', textvariable=EmailVar, width=25).grid(column=1, row=6, pady=3)

        self.Addresslbl = Label(self.master, text='Address:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=7, pady=3)
        self.AddressEntry = Entry(self.master, text='....', textvariable=AddressVar, width=25).grid(column=1, row=7, pady=3)

        self.PostCodelbl = Label(self.master, text='PostCode:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=8, pady=3)
        self.PostCodeEntry = Entry(self.master, text='....', textvariable=PostCodeVar, width=25).grid(column=1, row=8, pady=3)

        self.DOBlbl = Label(self.master, text='DOB:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=9, pady=3)
        self.DOBEntry = Entry(self.master, text='....', textvariable=DOBVar, width=25).grid(column=1, row=9, pady=3)

        self.Genderlbl = Label(self.master, text='Gender:', font=('Calibri', 12), bg=bgcolour).grid(column=2, row=2, pady=3)
        self.GenderDropdown = OptionMenu(self.master, GenderVar, *GenderChoices).grid(column=3, row=2, pady=3)

        self.JobTitlelbl = Label(self.master, text='Job Title:', font=('Calibri', 12), bg=bgcolour).grid(column=2, row=3, pady=3)
        self.JobTitleDropDown = OptionMenu(self.master, JobTitleVar, *JobTitleChoices).grid(column=3, row=3, pady=3)

        self.NINlbl = Label(self.master, text='National Insurance:', font=('Calibri', 12), bg=bgcolour).grid(column=2, row=4, pady=3)
        self.NINEntry = Entry(self.master, text='....', textvariable=NINVar, width=25).grid(column=3, row=4, pady=3)

        self.ContactedHourslbl = Label(self.master, text='Contracted Hours:', font=('Calibri', 12), bg=bgcolour).grid(column=2, row=5, pady=3)
        self.ContractedHoursEntry = Entry(self.master, text='....', textvariable=ContractedHoursVar, width=25).grid(column=3, row=5, pady=3)

        self.Usernamelbl = Label(self.master, text='Username:', font=('Calibri', 12), bg=bgcolour).grid(column=2, row=6, pady=3)
        self.UsernameEntry = Entry(self.master, text='....', textvariable=UsernameVar, width=25).grid(column=3, row=6, pady=3)

        self.Passwordlbl = Label(self.master, text='Password:', font=('Calibri', 12), bg=bgcolour).grid(column=2, row=7, pady=3)
        self.PasswordEntry = Entry(self.master, text='....', textvariable=PasswordVar, show='*', width=25).grid(column=3, row=7, pady=3)

        self.AddStaffbtn = Button(self.master, text='Add Staff', command=self.DataValidation, font=('Calibri', 12), width=15).grid(column=2, row=10, pady=5)
        self.BackButton = Button(master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=1, row=10, pady=5)

    def DataValidation(self):
        self.FirstName = FirstNameVar.get()
        self.Surname = SurnameVar.get()
        self.MobileNumber = MobileNumVar.get()
        self.TelephoneNum = TelephoneNumVar.get()
        self.Email = EmailVar.get()
        self.Address = AddressVar.get()
        self.PostCode = PostCodeVar.get()
        self.DOB = DOBVar.get()
        self.Gender = GenderVar.get()
        self.JobTitle = JobTitleVar.get()
        self.NIN = NINVar.get()
        self.ContractedHours = ContractedHoursVar.get()
        self.Username = UsernameVar.get()
        self.Password = PasswordVar.get()

        if self.FirstName == '':
            messagebox.showerror('Error', 'First Name Required')

        if self.Surname == '':
            messagebox.showerror('Error', 'Surname Required')

        if self.MobileNumber == '':
            messagebox.showerror('Error', 'Mobile Number Required')

        if self.TelephoneNum == '':
            messagebox.showerror('Error', 'Telephone Number Required')

        if self.Email == '':
            messagebox.showerror('Error', 'Email Required')

        if self.Address == '':
            messagebox.showerror('Error', 'Address Required')

        if self.PostCode == '':
            messagebox.showerror('Error', 'Postcode Required')

        if self.DOB == '':
            messagebox.showerror('Error', 'Date-Of-Birth Required')

        if self.Gender == '':
            messagebox.showerror('Error', 'Gender Required')

        if self.JobTitle == '':
            messagebox.showerror('Error', 'Job Title Required')

        if self.NIN == '':
            messagebox.showerror('Error', 'National Insurance Required')

        if self.ContractedHours == '':
            messagebox.showerror('Error', 'Contracted Hours Required')

        if self.Username == '':
            messagebox.showerror('Error', 'Username Required')

        if self.Password == '':
            messagebox.showerror('Error', 'Password required')

        if len(self.FirstName) > 0 and len(self.FirstName) < 30:
            self.FirstName = self.FirstName
        else:
            messagebox.showerror('Error', 'First Name Invalid')

        if len(self.Surname) > 0 and len(self.Surname) < 30:
            self.Surname = self.Surname
        else:
            messagebox.showerror('Error', 'Surname Invalid')

        if len(self.MobileNumber) == 11:
            self.MobileNumber = self.MobileNumber
        else:
            messagebox.showerror('Error', 'Mobile Number Invalid')

        if len(self.TelephoneNum) == 11:
            self.TelephoneNum = self.TelephoneNum
        else:
            messagebox.showerror('Error', 'Telephone Number Invalid')

        if len(self.Email) > 0 and len(self.Email) < 40:
            self.Email = self.Email
        else:
            messagebox.showerror('Error', 'Email Invalid')

        if len(self.Address) > 0 and len(self.Address) < 50:
            self.Address = self.Address
        else:
            messagebox.showerror('Error', 'Address Invalid')

        if len(self.PostCode) == 8:
            self.PostCode = self.PostCode
        else:
            messagebox.showerror('Error', 'Postcode Invalid')

        if len(self.DOB) == 10:
            self.DOB = self.DOB
        else:
            messagebox.showerror('Error', 'Date-Of-Birth Invalid')

        if len(self.NIN) == 9:
            self.NIN = self.NIN
        else:
            messagebox.showerror('Error', 'National Insurance Invalid')

        if self.ContractedHours > 0:
            self.Email = self.Email
        else:
            messagebox.showerror('Error', 'Email Invalid')

        if len(self.Username) > 10 and len(self.Username) < 50:
            self.Username = self.Username
        else:
            messagebox.showerror('Error', 'Username Invalid')

        if len(self.Password) > 10 and len(self.Password) < 50:
            self.Password = self.Password
        else:
            messagebox.showerror('Error', 'Password Invalid')

        self.AddStaff(self.FirstName, self.Surname, self.MobileNumber, self.TelephoneNum, self.Email, self.Address, self.PostCode, self.DOB, self.Gender, self.JobTitle, self.NIN, self.ContractedHours, self.Username, self.Password)

    def AddStaff(self, FirstName, Surname, MobileNum, TelephoneNum, Email, Address, PostCode, DOB, Gender, JobTitle, NIN, ContractedHours, Username, Password):

        self.HourlyRate = 0

        if JobTitle == 'Owner':
            self.HourlyRate = 15
        elif JobTitle == 'Manager':
            self.HourlyRate = 15
        elif JobTitle == ' Receptionist':
            self.HourlyRate = 10
        elif JobTitle == 'Concierge':
            self.HourlyRate = 7.50

        self.HashedPassword = self.hash_password(Password)

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()

            AddStaffSQL = '''INSERT OR REPLACE INTO Staff (FirstName, Surname, MobileNumber, TelephoneNumber, Email, Address, PostCode, DOB, Gender, JobTitle, NIN, HourlyRate, ContractedHours, Username, Password) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
            AddStaffValues = (FirstName, Surname, MobileNum, TelephoneNum, Email, Address, PostCode, DOB, Gender, JobTitle, NIN, self.HourlyRate, ContractedHours, Username, self.HashedPassword)
            c.execute(AddStaffSQL, AddStaffValues)

            db.commit()

            GetStaffID = '''SELECT * FROM Staff WHERE MobileNumber = ? '''
            StaffIDValues = MobileNum

            c.execute(GetStaffID, (StaffIDValues,))
            StaffID = c.fetchone()

            self.DisplayStaffInfo(StaffID[0], FirstName, Surname, MobileNum, TelephoneNum, Email, Address, PostCode, DOB, Gender, JobTitle, NIN, self.HourlyRate, ContractedHours, Username)


    def DisplayStaffInfo(self, StaffID, FirstName, Surname, MobileNum, TelephoneNum, Email, Address, PostCode, DOB, Gender, JobTitle, NIN, HourlyRate, ContractedHours, Username):
        AllWidgets = self.master.grid_slaves()
        #print(AllWidgets[0:10])
        for i in AllWidgets[0:30]:
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


        self.AddStaffbtn = Button(self.master, text='Add Another', command=self.AddAnother, font=('Calibri', 12), width=15).grid(column=2, row=10, pady=5)
        self.BackButton = Button(self.master, text='Done', command=self.Back, font=('Calibri', 12), width=8).grid(column=1, row=10, pady=5)

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)

        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def AddAnother(self):

        AllWidgets = self.master.grid_slaves()

        for i in AllWidgets:
            i.destroy()

        AddStaffGUI(root, 500, 650, '#85C1E9', '#EBF5FB', 'Add Staff')

    def Back(self):
        AllWidgets = self.master.grid_slaves()
        # Clears the window of widgets
        for i in AllWidgets:
            i.destroy()
        MSS.ManagerStaffSettingsGUI(self.master, 500, 350, '#85C1E9', '#EBF5FB', 'Staff Settings')

if __name__ == '__main__':
    root = Tk()
    gui = AddStaffGUI(root, 500, 650, '#85C1E9', '#EBF5FB', 'Add Staff')
    root.mainloop()