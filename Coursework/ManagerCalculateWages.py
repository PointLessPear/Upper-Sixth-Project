import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import sqlite3
import time

from MainGUI import main
import ManagerStaffSettings as MSS

class CalculateWagesGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):
        global StaffIDVar
        StaffIDVar = StringVar()

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.BackButton = Button(master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=1, pady=10)

        self.StaffIDLabel = Label(self.master, text='Staff ID', font=('Calibri', 12), bg=bgcolour).grid(row=2,column=0)
        self.StaffIDEntry = Entry(self.master, text='....', textvariable=StaffIDVar, width=25).grid(row=2, column=1)
        self.StaffConfirmBtn = Button(self.master, command=self.StaffIDValidation, text='Confirm Staff', font=('Calibri', 12)).grid(row=3, column=1, pady=5)
        self.CalcStaffWages = Button(self.master, command=self.IntialWageWindow, text='Start Wages', font=('Calibri', 12)).grid(row=4, column=1, pady=5)


    def StaffIDValidation(self):

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
        self.ViewAnotherBtn = Button(self.master, text='Create Rota', command=self.IntialWageWindow, font=('Calibri', 12), width=15).grid(column=2, row=10, pady=5)
        self.BackButton = Button(self.master, text='Exit', command=self.Back, font=('Calibri', 12), width=15).grid(column=1, row=10, pady=5)

    def IntialWageWindow(self):
        self.StaffID = StaffIDVar.get()

        AllWidgets = self.master.grid_slaves()
        #print(AllWidgets[0:7])
        #Only deletes required widgets (Staff ID Label/Entry and two bottom button)
        for i in AllWidgets[0:5]:
            i.destroy()
        self.ViewWages()

    def ViewWages(self):
        self.master.minsize(width=650, height=525)
        self.master.maxsize(width=650, height=525)
        #TitleFrame.configure(width=650)

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            StaffNameSQL = '''SELECT FirstName, Surname FROM Staff WHERE StaffID = ?'''
            c.execute(StaffNameSQL, self.StaffID)
            self.Staff = c.fetchall()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:

            c = db.cursor()
            GetRotaDetails = '''SELECT * FROM Rota WHERE StaffID = ?'''
            c.execute(GetRotaDetails, (self.StaffID,))
            RotaDetails = c.fetchone()

        global HoursToEdit, WeekStartVar, MonStartVar, MonFinishVar, TuesStartVar, TuesFinishVar, WedStartVar, WedFinishVar, ThursStartVar, ThursFinishVar, FriStartVar, FriFinishVar, SatStartVar, SatFinishVar, SunStartVar, SunFinishVar
        print(RotaDetails)
        #Variables required
        WeekStartVar = RotaDetails[2]
        MonStartVar = RotaDetails[3]
        MonFinishVar = RotaDetails[4]
        TuesStartVar = RotaDetails[5]
        TuesFinishVar = RotaDetails[6]
        WedStartVar = RotaDetails[7]
        WedFinishVar = RotaDetails[8]
        ThursStartVar = RotaDetails[9]
        ThursFinishVar = RotaDetails[10]
        FriStartVar = RotaDetails[11]
        FriFinishVar = RotaDetails[12]
        SatStartVar = RotaDetails[13]
        SatFinishVar = RotaDetails[14]
        SunStartVar = RotaDetails[15]
        SunFinishVar = RotaDetails[16]

        HoursToEdit = StringVar()
        self.ReplacementHours = IntVar()

        self.StaffIDLabel = Label(self.master, text='Staff Name:', font=('Calibri', 12), bg='#85C1E9').grid(row=2,column=0, pady=3)
        self.InputtedID = Label(self.master, text=self.Staff, font=('Calibri', 12), bg='#85C1E9').grid(row=2,column=1, pady=3)

        self.WeekStartLabel = Label(self.master, text='Week Start', font=('Calibri', 12), bg='#85C1E9').grid(row=3,column=0, pady=3)
        self.WeekStartEntry = Entry(self.master, text='....', textvariable=WeekStartVar, width=25).grid(row=3, column=1)

        #Entry Labels
        self.MonLabel = Label(self.master, text='Monday Start - Monday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=4, column=0, pady=3)
        self.TuesLabel = Label(self.master, text='Tuesday Start - Tuesday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=5, column=0, pady=3)
        self.WedLabel = Label(self.master, text='Wednesday Start - Wednesday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=6, column=0, pady=3)
        self.ThursLabel = Label(self.master, text='Thursday Start - Thursday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=7, column=0, pady=3)
        self.FriLabel = Label(self.master, text='Friday Start - Friday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=8, column=0, pady=3)
        self.SatLabel = Label(self.master, text='Saturday Start - Saturday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=9, column=0, pady=3)
        self.SunLabel = Label(self.master, text='Sunday Start - Sunday Finish', font=('Calibri', 11), bg='#85C1E9').grid(row=10, column=0, pady=3)

        #Entries
        self.MonStartLabel = Label(self.master, text=MonStartVar, font=('Calibri', 11), bg='#85C1E9').grid(row=4, column=1,pady=3)
        self.MonFinishLabel = Label(self.master, text=MonFinishVar, font=('Calibri', 11), bg='#85C1E9' ).grid(row=4, column=2, pady=3)
        self.TuesStartLabel = Label(self.master, text=TuesStartVar, font=('Calibri', 11), bg='#85C1E9' ).grid(row=5, column=1, pady=3)
        self.TuesFinishLabel = Label(self.master, text=TuesFinishVar, font=('Calibri', 11), bg='#85C1E9' ).grid(row=5, column=2, pady=3)
        self.WedStartLabel = Label(self.master, text=WedStartVar, font=('Calibri', 11), bg='#85C1E9').grid(row=6, column=1,pady=3)
        self.WedFinishLabel = Label(self.master, text=WedFinishVar, font=('Calibri', 11), bg='#85C1E9').grid(row=6, column=2, pady=3)
        self.ThursStartLabel = Label(self.master, text=ThursStartVar, font=('Calibri', 11), bg='#85C1E9' ).grid(row=7, column=1, pady=3)
        self.ThursFinishLabel = Label(self.master, text=TuesFinishVar, font=('Calibri', 11), bg='#85C1E9' ).grid(row=7, column=2, pady=3)
        self.FriStartLabel = Label(self.master, text=FriStartVar, font=('Calibri', 11), bg='#85C1E9' ).grid(row=8, column=1, pady=3)
        self.FriFinishLabel = Label(self.master, text=FriFinishVar, font=('Calibri', 11), bg='#85C1E9' ).grid(row=8, column=2, pady=3)
        self.SatStartLabel = Label(self.master, text=SatStartVar, font=('Calibri', 11), bg='#85C1E9' ).grid(row=9, column=1, pady=3)
        self.SatFinishLabel = Label(self.master, text=SatFinishVar, font=('Calibri', 11), bg='#85C1E9' ).grid(row=9, column=2, pady=3)
        self.SunStartLabel = Label(self.master, text=SunStartVar, font=('Calibri', 11), bg='#85C1E9' ).grid(row=10, column=1, pady=3)
        self.SunFinishLabel = Label(self.master, text=SunFinishVar, font=('Calibri', 11), bg='#85C1E9' ).grid(row=10, column=2, pady=3)

        StartFinishOptions = ['Monday Start', 'Monday Finish', 'Tuesday Start', 'Tuesday Finish', 'Wednesday Start', 'Wednesday Finish',
                              'Thursday Start', 'Thursday Finish', 'Friday Start', 'Friday Finish', 'Saturday Start', 'Saturday Finish',
                              'Sunday Start', 'Sunday Finish']

        HoursToEdit.set('None')

        self.ReplacementHourslbl = Label(self.master, text='Replacement Time:', font=('Calibri', 12), bg='#85C1E9').grid(row=11, column=0, pady=3)
        self.ReplacementHoursEntry = Entry(self.master, text='....', textvariable=self.ReplacementHours, width=25).grid(row=11, column=1, pady=3)
        self.EditHoursOption = OptionMenu(self.master, HoursToEdit, *StartFinishOptions).grid(row=11, column=2, pady=3)

        self.CalculateWagebtn = Button(self.master, text='Calculate Wages', command=self.SubmitWages, font=('Calibri', 12), width=15).grid(column=2, row=12, pady=5)
        self.ReplaceHoursBtn = Button(self.master, text='Replace Hours', command=self.ReplaceHours, font=('Calibri', 12), width=15).grid(column=1, row=12, pady=5)
        self.BackButton = Button(self.master, text='Exit', command=self.Back, font=('Calibri', 12), width=15).grid(column=0, row=12, pady=5)

    def ReplaceHours(self):
        self.StaffID = StaffIDVar.get()
        self.HoursToEdit = HoursToEdit.get()
        self.ReplacementHours = self.ReplacementHours.get()
        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            if self.HoursToEdit == 'Monday Start':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaMonStart = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Monday Finish':
                c = db.cursor()

                UpdateSQL = ('''UPDATE Rota SET RotaMonFinish = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Tuesday Start':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaTuesStart = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Tuesday Finish':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaTuesFinish = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Wednesday Start':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaWedStart = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Wednesday Finish':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaWedFinish = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Thursday Start':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaThursStart = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Thursday Finish':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaThursFinish = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Friday Start':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaFriStart = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Friday Finish':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaFriFinish = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Saturday Start':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaSatStart = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Saturday Finish':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaSatFinish = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Sunday Start':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaSunStart = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

            if self.HoursToEdit == 'Sunday Finish':
                c = db.cursor()
                UpdateSQL = ('''UPDATE Rota SET RotaSunFinish = ? WHERE StaffID = ?''')
                Values = (self.ReplacementHours, self.StaffID)
                c.execute(UpdateSQL, Values)
                db.commit()

        AllWidgets = self.master.grid_slaves()

        for i in AllWidgets[0:31]:
            i.destroy()
        self.ViewWages()

    def SubmitWages(self):
        self.CalcWagesSQL(WeekStartVar, MonStartVar, MonFinishVar, TuesStartVar, TuesFinishVar, WedStartVar, WedFinishVar, ThursStartVar, ThursFinishVar, FriStartVar, FriFinishVar, SatStartVar, SatFinishVar, SunStartVar, SunFinishVar)

    def CalcWagesSQL(self, WeekStart, MonStart, MonFinish, TuesStart, TuesFinish, WedStart, WedFinish, ThursStart, ThursFinish, FriStart, FriFinish, SatStart, SatFinish, SunStart, SunFinish):
        self.StaffID = StaffIDVar.get()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            #Gets staff members hourly rate of pay from Staff table
            sql = '''SELECT HourlyRate FROM Staff WHERE StaffID = ? '''
            c.execute(sql, self.StaffID)
            HourlyRate = c.fetchall()
            HourlyRate = str(HourlyRate)
            for char in HourlyRate:
                #Strips any [](),' from the str then converts it to a float for calculation
                if char in "[](),'":
                    HourlyRate = HourlyRate.replace(char, '')

        HourlyRate = float(HourlyRate)
        print(HourlyRate)
        #Getting the hours worked each day
        MonHours = MonFinish - MonStart
        TuesHours = TuesFinish - TuesStart
        WedHours = WedFinish - WedStart
        ThursHours = ThursFinish - ThursStart
        FriHours = FriFinish - FriStart
        SatHours = SatFinish - SatStart
        SunHours = SunFinish - SunStart

        TotalHours = MonHours + TuesHours + WedHours + ThursHours + FriHours + SatHours + SunHours
        TotalWage = TotalHours * HourlyRate
        print(TotalHours)
        print(TotalWage)


        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            sql = '''INSERT INTO Wages (StaffID, WeekStart,MonStart, MonFinish, TuesStart, TuesFinish, WedStart, WedFinish, ThursStart, ThursFinish, FriStart, FriFinish, SatStart, SatFinish, SunStart, SunFinish, TotalHours, TotalWages) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
            wagevalues = (self.StaffID, WeekStart, MonStart, MonFinish, TuesStart, TuesFinish, WedStart, WedFinish, ThursStart, ThursFinish, FriStart, FriFinish, SatStart, SatFinish, SunStart, SunFinish, TotalHours, TotalWage)
            c.execute(sql, wagevalues)
            db.commit()

    def WrongStaff(self):
        AllWidgets = self.master.grid_slaves()

        for i in AllWidgets:
            i.destroy()

        CalculateWagesGUI(self.master, 500, 650, '#85C1E9', '#EBF5FB', 'Calculate Wages')

    def Back(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        MSS.ManagerStaffSettingsGUI(self.master, 500, 350, '#85C1E9', '#EBF5FB', 'Staff Settings')

if __name__ == '__main__':
    root = Tk()
    gui = CalculateWagesGUI(root, 500, 650, '#85C1E9', '#EBF5FB', 'Calculate Wages')
    root.mainloop()