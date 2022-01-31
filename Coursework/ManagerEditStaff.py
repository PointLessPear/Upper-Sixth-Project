import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import time
import sqlite3

from MainGUI import main
import ManagerStaffSettings as MSS

class EditStaffGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):
        self.master = master
        super().__init__(self.master, height, width, bgcolour, framecolour, title)

        master.title(title)

        global StaffIDVar, AttToEditVar, ReplacementDataVar

        StaffIDVar = StringVar()
        AttToEditVar = StringVar()
        ReplacementDataVar = StringVar()

        AttToEditList = ['FirstName', 'Surname', 'Mobile Number', 'Telephone Number',
                         'Email', 'Address', 'Post Code', 'DOB', 'Gender',
                         'Job Title', 'NIN', 'Contracted Hours', 'Username']

        AttToEditVar.set('None')

        self.BackButton = Button(self.master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=5, pady=10)

        self.IDlbl = Label(self.master, text='Staff ID: ', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=2, pady=3)
        self.IDEntry = Entry(self.master, text='....', textvariable=StaffIDVar, width=25).grid(column=1, row=2, pady=3)

        self.AttToEditlbl = Label(self.master, text='Attribute to edit:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=3, pady=3)
        self.AttToEdit = OptionMenu(self.master, AttToEditVar, *AttToEditList).grid(column=1, row=3, pady=3)

        self.ReplacementDatalbl = Label(self.master, text='Replace with:', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=4, pady=3)
        self.ReplacementDataEntry = Entry(self.master, text='....', textvariable=ReplacementDataVar, width=25).grid(column=1, row=4, pady=3)

        self.EditAttBtn = Button(self.master, text='Edit', command=self.EditAtt, width=18, font=('Calibri', 12)).grid(column=1, row=5, pady=5)
        self.ConfirmBookingBtn = Button(self.master, text='Confirm Staff', font=('Calibri', 12), command=self.ConfirmStaff, width=18).grid(column=1, row=6, pady=3)

    def EditAtt(self):
        self.StaffID = StaffIDVar.get()
        self.AttToEdit = AttToEditVar.get()
        self.ReplacementData = ReplacementDataVar.get()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()


            if self.StaffID == '':
                messagebox.showerror('Error', 'BookingID Required')

            if self.AttToEdit == 'None':
                messagebox.showerror('Error', 'Attribute to edit required')

            if self.ReplacementData == '':
                messagebox.showerror('Replacement Data Required')

            if self.AttToEdit == 'FirstName':
                if len(self.ReplacementData) > 0 < 30:
                    UpdateSql = '''UPDATE Staff SET FirstName = ? WHERE StaffID = ?'''
                    values = (self.ReplacementData, self.StaffID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'First Name invalid')

            if self.AttToEdit == 'Surname':
                if len(self.ReplacementData) > 0 < 30:
                    UpdateSql = '''UPDATE Staff SET Surname = ? WHERE StaffID = ?'''
                    values = (self.ReplacementData, self.StaffID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'Surname invalid')

            if self.AttToEdit == 'Mobile Number':
                if len(self.ReplacementData) == 11:
                    UpdateSql = '''UPDATE Staff SET MobileNumber = ? WHERE StaffID = ?'''
                    values = (self.ReplacementData, self.StaffID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'MobileNumber invalid')

            if self.AttToEdit == 'Telephone Number':
                if len(self.ReplacementData) == 11:
                    UpdateSql = '''UPDATE Staff SET TelephoneNumber = ? WHERE StaffID = ?'''
                    values = (self.ReplacementData, self.StaffID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'Telephone Number invalid')

            if self.AttToEdit == 'Email':
                if len(self.ReplacementData) > 0 < 50:
                    UpdateSql = '''UPDATE Staff SET Email = ? WHERE StaffID = ?'''
                    values = (self.ReplacementData, self.StaffID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'Email invalid')

            if self.AttToEdit == 'Address':
                if len(self.ReplacementData) > 0 < 50:
                    UpdateSql = '''UPDATE Staff SET Address = ? WHERE StaffID = ?'''
                    values = (self.ReplacementData, self.StaffID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'Email invalid')

            if self.AttToEdit == 'Post Code':
                if len(self.ReplacementData) == 8:
                    UpdateSql = '''UPDATE Staff SET Postcode = ? WHERE StaffID = ?'''
                    values = (self.ReplacementData, self.StaffID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'Email invalid')

            if self.AttToEdit == 'DOB':
                if len(self.ReplacementData) == 10:
                    UpdateSql = '''UPDATE Staff SET DOBx = ? WHERE StaffID = ?'''
                    values = (self.ReplacementData, self.StaffID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'Date-Of-Birth invalid')

            if self.AttToEdit == 'Gender':
                if len(self.ReplacementData) > 0 < 6:
                    UpdateSql = '''UPDATE Staff SET Gender = ? WHERE StaffID = ?'''
                    values = (self.ReplacementData, self.StaffID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'Gender invalid')

            if self.AttToEdit == 'Job Title':
                if len(self.ReplacementData) > 0 < 3:

                    self.HourlyRate = 0

                    if self.ReplacementData == 'Owner':
                        self.HourlyRate = 15

                    elif self.ReplacementData == 'Manager':
                        self.HourlyRate = 15

                    elif self.ReplacementData == ' Receptionist':
                        self.HourlyRate = 10

                    elif self.ReplacementData == 'Concierge':
                        self.HourlyRate = 7.50

                    UpdateHourlyRate = '''UPDATE Staff SET HourlyRate = ? WHERE StaffID = ?'''
                    HourlyRateValues = (self.HourlyRate, self.StaffID)
                    c.execute(UpdateHourlyRate, HourlyRateValues)

                    UpdateSql = '''UPDATE Staff SET Email = ? WHERE StaffID = ?'''
                    values = (self.ReplacementData, self.StaffID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'Email invalid')

            if self.AttToEdit == 'Contracted Hours':
                if len(self.ReplacementData) > 0 < 3:
                    UpdateSql = '''UPDATE Staff SET ContractedHours = ? WHERE StaffID = ?'''
                    values = (self.ReplacementData, self.StaffID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'Contracted Hours invalid')

            if self.AttToEdit == 'Username':
                if len(self.ReplacementData) > 10 < 40:
                    UpdateSql = '''UPDATE Staff SET Username = ? WHERE StaffID = ?'''
                    values = (self.ReplacementData, self.StaffID)
                    c.execute(UpdateSql, values)
                    db.commit()
                else:
                    messagebox.showerror('Error', 'Username invalid')

    def ConfirmStaff(self):

        self.StaffID = StaffIDVar.get()

        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            c = db.cursor()
            ConfirmStaffSQL = '''SELECT * FROM Staff WHERE StaffID = ?'''
            c.execute(ConfirmStaffSQL, self.StaffID)
            Staff = c.fetchone()

            if Staff is not '':
                messagebox.showinfo('Staff Found', Staff)
            else:
                messagebox.showerror('Error', 'Staff Not Found')

    def Back(self):
        AllWidgets = self.master.grid_slaves()
        RowCount = 1
        # Clears the window of widgets
        for i in AllWidgets:
            i.destroy()

        MSS.ManagerStaffSettingsGUI(self.master, 545, 350, '#85C1E9', '#EBF5FB', 'Staff Settings')


if __name__ == '__main__':
    root = Tk()
    gui = EditStaffGUI(root, 460, 475, '#85C1E9', '#EBF5FB', 'Edit Staff')
    root.mainloop()