import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import sqlite3
import time

from MainGUI import main
import ManagerStaffSettings as MSS

class CreateRotaGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):

        global StaffIDVar
        StaffIDVar = StringVar()

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.BackButton = Button(master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=1, pady=10)

        self.StaffIDLabel = Label(self.master, text='Staff ID', font=('Calibri', 12), bg=bgcolour).grid(row=2,column=0)
        self.StaffIDEntry = Entry(self.master, text='....', textvariable=StaffIDVar, width=25).grid(row=2, column=1)
        self.StaffConfirmBtn = Button(self.master, command=self.DataValidation, text='Confirm Staff', font=('Calibri', 12), width=15).grid(row=3, column=1, pady=5)
        self.CreateRotaBtn = Button(self.master, command=self.CreateRota, text='Start Rota', font=('Calibri', 12), width=15).grid(row=4, column=1, pady=5)


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

        self.WrongStaffBtn = Button(self.master, text='Wrong Staff Member:', command=self.WrongStaff, font=('Calibri', 12), width=20).grid(column=3, row=10, pady=5)
        self.ViewAnotherBtn = Button(self.master, text='Create Rota', command=self.CreateRota, font=('Calibri', 12), width=15).grid(column=2, row=10, pady=5)
        self.BackButton = Button(self.master, text='Exit', command=self.Back, font=('Calibri', 12), width=15).grid(column=1, row=10, pady=5)

    def CreateRota(self):
        self.StaffID = StaffIDVar.get()
        AllWidgets = self.master.grid_slaves()
        # print(AllWidgets[0:7])
        # Only deletes required widgets (Staff ID Label/Entry and two bottom button)
        for i in AllWidgets[0:18]:
            i.destroy()

        self.master.minsize(width=650, height=525)
        self.master.maxsize(width=650, height=525)
        # TitleFrame.configure(width=650)

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            StaffNameSQL = '''SELECT FirstName, Surname FROM Staff WHERE StaffID = ?'''
            c.execute(StaffNameSQL, self.StaffID)
            self.Staff = c.fetchall()

        global RotaWeekStartVar, RotaMonStartVar, RotaMonFinishVar, RotaTuesStartVar, RotaTuesFinishVar, RotaWedStartVar, RotaWedFinishVar, RotaThursStartVar, RotaThursFinishVar, RotaFriStartVar, RotaFriFinishVar, RotaSatStartVar, RotaSatFinishVar, RotaSunStartVar, RotaSunFinishVar

        # Variables required
        RotaWeekStartVar = StringVar()
        RotaMonStartVar = IntVar()
        RotaMonFinishVar = IntVar()
        RotaTuesStartVar = IntVar()
        RotaTuesFinishVar = IntVar()
        RotaWedStartVar = IntVar()
        RotaWedFinishVar = IntVar()
        RotaThursStartVar = IntVar()
        RotaThursFinishVar = IntVar()
        RotaFriStartVar = IntVar()
        RotaFriFinishVar = IntVar()
        RotaSatStartVar = IntVar()
        RotaSatFinishVar = IntVar()
        RotaSunStartVar = IntVar()
        RotaSunFinishVar = IntVar()

        self.StaffIDLabel = Label(self.master, text='Staff Name:', font=('Calibri', 12), bg='#85C1E9').grid(row=2, column=0, pady=3)
        self.InputtedID = Label(self.master, text=self.Staff, font=('Calibri', 12), bg='#85C1E9').grid(row=2, column=1, pady=3)

        self.WeekStartLabel = Label(self.master, text='Week Start', font=('Calibri', 12), bg='#85C1E9').grid(row=3, column=0,  pady=3)
        self.WeekStartEntry = Entry(self.master, text='....', textvariable=RotaWeekStartVar, width=25).grid(row=3, column=1)

        # Entry Labels
        self.MonLabel = Label(self.master, text='Monday Start - Monday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=4, column=0, pady=3)
        self.TuesLabel = Label(self.master, text='Tuesday Start - Tuesday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=5, column=0, pady=3)
        self.WedLabel = Label(self.master, text='Wednesday Start - Wednesday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=6, column=0, pady=3)
        self.ThursLabel = Label(self.master, text='Thursday Start - Thursday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=7, column=0, pady=3)
        self.FriLabel = Label(self.master, text='Friday Start - Friday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=8, column=0, pady=3)
        self.SatLabel = Label(self.master, text='Saturday Start - Saturday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=9, column=0, pady=3)
        self.SunLabel = Label(self.master, text='Sunday Start - Sunday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=10, column=0, pady=3)

        # Entries
        self.MonStartEntry = Entry(self.master, text='....', textvariable=RotaMonStartVar, width=25).grid(row=4, column=1, pady=3)
        self.MonFinishEntry = Entry(self.master, text='....', textvariable=RotaMonFinishVar, width=25).grid(row=4, column=2, pady=3)
        self.TuesStartEntry = Entry(self.master, text='....', textvariable=RotaTuesStartVar, width=25).grid(row=5, column=1, pady=3)
        self.TuesFinishEntry = Entry(self.master, text='....', textvariable=RotaTuesFinishVar, width=25).grid(row=5, column=2, pady=3)
        self.WedStartEntry = Entry(self.master, text='....', textvariable=RotaWedStartVar, width=25).grid(row=6, column=1, pady=3)
        self.WedFinishEntry = Entry(self.master, text='....', textvariable=RotaWedFinishVar, width=25).grid(row=6, column=2, pady=3)
        self.ThursStartEntry = Entry(self.master, text='....', textvariable=RotaThursStartVar, width=25).grid(row=7, column=1, pady=3)
        self.ThursFinishEntry = Entry(self.master, text='....', textvariable=RotaThursFinishVar, width=25).grid(row=7, column=2,pady=3)
        self.FriStartEntry = Entry(self.master, text='....', textvariable=RotaFriStartVar, width=25).grid(row=8, column=1, pady=3)
        self.FriFinishEntry = Entry(self.master, text='....', textvariable=RotaFriFinishVar, width=25).grid(row=8, column=2, pady=3)
        self.SatStartEntry = Entry(self.master, text='....', textvariable=RotaSatStartVar, width=25).grid(row=9, column=1, pady=3)
        self.SatFinishEntry = Entry(self.master, text='....', textvariable=RotaSatFinishVar, width=25).grid(row=9, column=2, pady=3)
        self.SunStartEntry = Entry(self.master, text='....', textvariable=RotaSunStartVar, width=25).grid(row=10, column=1, pady=3)
        self.SunFinishEntry = Entry(self.master, text='....', textvariable=RotaSunFinishVar, width=25).grid(row=10, column=2, pady=3)

        self.ContinueBtn = Button(self.master, command=self.RotaDataValidation, text='Continue', font=('Calibri', 12), width=25).grid(row=11, column=1, pady=3)
        self.ExitBtn = Button(self.master, command=self.Back, text='Exit', font=('Calibri', 12), width=25).grid(row=11, column=2, pady=3)

    def RotaDataValidation(self):

        self.WeekStartVar = RotaWeekStartVar.get()
        self.MonStart = RotaMonStartVar.get()
        self.MonFinish = RotaMonFinishVar.get()
        self.TuesStart = RotaTuesStartVar.get()
        self.TuesFinish = RotaTuesFinishVar.get()
        self.WedStart = RotaWedStartVar.get()
        self.WedFinish = RotaWedFinishVar.get()
        self.ThursStart = RotaThursStartVar.get()
        self.ThursFinish = RotaThursFinishVar.get()
        self.FriStart = RotaFriStartVar.get()
        self.FriFinish = RotaFriFinishVar.get()
        self.SatStart = RotaSatStartVar.get()
        self.SatFinish = RotaSatFinishVar.get()
        self.SunStart = RotaSunStartVar.get()
        self.SunFinish = RotaSunFinishVar.get()

        # Presence check
        if self.MonStart == '':
            messagebox.showerror('Error', 'Monday start required')
        else:
            self.MonStart = self.MonStart

        if self.MonFinish == '':
            messagebox.showerror('Error', 'Monday finish required')
        else:
            self.MonFinish = self.MonFinish

        if self.TuesStart == '':
            messagebox.showerror('Error', 'Tuesday start required')
        else:
            self.TuesStart = self.TuesStart

        if self.TuesFinish == '':
            messagebox.showerror('Error', 'Tuesday finish required')
        else:
            self.TuesFinish = self.TuesFinish

        if self.WedStart == '':
            messagebox.showerror('Error', 'Wednesday start required')
        else:
            self.WedStart = self.WedStart

        if self.WedFinish == '':
            messagebox.showerror('Error', 'Wednesday finish required')
        else:
            self.WedFinish = self.WedFinish

        if self.ThursStart == '':
            messagebox.showerror('Error', 'Thursday start required')
        else:
            self.ThursStart = self.ThursStart

        if self.ThursFinish == '':
            messagebox.showerror('Error', 'Thursday finish required')
        else:
            self.ThursFinish = self.ThursFinish

        if self.FriStart == '':
            messagebox.showerror('Error', 'Friday start required')
        else:
            self.FriStart = self.FriStart

        if self.FriFinish == '':
            messagebox.showerror('Error', 'Friday finish required')
        else:
            self.FriFinish = self.FriFinish

        if self.SatStart == '':
            messagebox.showerror('Error', 'Saturday start required')
        else:
            self.SatStart = self.SatStart

        if self.SatFinish == '':
            messagebox.showerror('Error', 'Saturday finish required')
        else:
            self.SatFinish = self.SatFinish

        if self.SunStart == '':
            messagebox.showerror('Error', 'Sunday Start required')
        else:
            self.SunStart = self.SunStart

        if self.SunFinish == '':
            messagebox.showerror('Error', 'Sunday Finish required')
        else:
            self.SunFinish = self.SunFinish

        self.SetRota(self.MonStart, self.MonFinish, self.TuesStart, self.TuesFinish, self.WedStart, self.WedFinish, self.ThursStart, self.ThursFinish, self.FriStart, self.FriFinish, self.SatStart, self.SatFinish, self.SunStart, self.SunFinish)


    def SetRota(self, MonStart, MonFinish, TuesStart, TuesFinish, WedStart, WedFinish, ThursStart, ThursFinish, FriStart, FriFinish, SatStart, SatFinish, SunStart, SunFinish):
        self.StaffID = StaffIDVar.get()
        self.WeekStart = RotaWeekStartVar.get()

        MonHours = MonFinish - MonStart
        TuesHours = TuesFinish - TuesStart
        WedHours = WedFinish - WedStart
        ThursHours = ThursFinish - ThursStart
        FriHours = FriFinish - FriStart
        SatHours = SatFinish - SatStart
        SunHours = SunFinish - SunStart

        TotalHours = MonHours + TuesHours + WedHours + ThursHours + FriHours + SatHours + SunHours

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            sql = '''INSERT INTO Rota (StaffID, RotaWeekStart, RotaMonStart, RotaMonFinish, RotaTuesStart, RotaTuesFinish, RotaWedStart, RotaWedFinish, RotaThursStart, RotaThursFinish, RotaFriStart, RotaFriFinish, RotaSatStart, RotaSatFinish, RotaSunStart, RotaSunFinish, RotaTotalHours) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
            wagevalues = (self.StaffID, self.WeekStart, MonStart, MonFinish, TuesStart, TuesFinish, WedStart, WedFinish, ThursStart, ThursFinish, FriStart, FriFinish, SatStart, SatFinish, SunStart, SunFinish, TotalHours)
            c.execute(sql, wagevalues)
            db.commit()

    def WrongStaff(self):
        AllWidgets = self.master.grid_slaves()

        for i in AllWidgets:
            i.destroy()

        CreateRotaGUI(self.master, 500, 650, '#85C1E9', '#EBF5FB', 'Calculate Rota')

    def Back(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        MSS.ManagerStaffSettingsGUI(self.master, 500, 350, '#85C1E9', '#EBF5FB', 'Staff Settings')

if __name__ == '__main__':
    root = Tk()
    gui = CreateRotaGUI(root,  500, 650, '#85C1E9', '#EBF5FB', 'Calculate Rota')
    root.mainloop()