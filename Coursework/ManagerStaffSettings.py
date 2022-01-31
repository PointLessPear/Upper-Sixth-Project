import tkinter as Tk
from tkinter import *

from MainGUI import main

import ManagerMenu as MM
import ManagerCalculateWages as MCW
import ManagerAddStaff as MAS
import ManagerEditStaff as MES
import ManagerViewStaff as MVS
import ManagerDeleteStaff as MDS
import ManagerCreateRota as MCR
import ManagerStaffChangePassword as MSCP

class ManagerStaffSettingsGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):
        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.BackButton = Button(master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=1, pady=10)

        self.AddStaffBtn = Button(master, text='Add Staff', command=self.CreateAddStaffGUI, width=18, pady=5, font=('Calibri', 12)).grid(row=2, column=1, pady=3)
        self.ViewStaffBtn = Button(master, text='View Staff Details', command=self.CreateAddStaffGUI, width=18, pady=5, font=('Calibri', 12)).grid(row=3, column=1, pady=3)
        self.EditStaffBtn = Button(master, text='Edit Staff Details', command=self.CreateEditStaffGUI, width=18, pady=5, font=('calibri', 12)).grid(row=4, column=1, pady=3)
        self.DeleteStaffBtn = Button(master, text='Delete Staff', command=self.CreateDeleteStaffGUI, width=18, pady=5, font=('Calibri', 12)).grid(row=5, column=1, pady=3)
        self.CalculateStaffWages = Button(master, text='Calculate Wages', command=self.CreateCalculateWagesGUI, width=18, pady=5, font=('Calibri', 12)).grid(row=6, column=1, pady=3)
        self.CreateRotaBtn = Button(master, text='Create Rota', command=self.CreateRotaGUI, width=18, pady=5, font=('Calibri', 12)).grid(row=7, column=1, pady=3)
        self.ApproveHolidaysBtn = Button(master, text='Approve Holidays', command=self.temp, width=18, pady=5, font=('calibri', 12)).grid(row=8, column=1, pady=3)
        self.ChangeStaffPassBtn = Button(master, text='Change Password', command=self.temp, width=18, pady=5, font=('Calibri', 12)).grid(row=9, column=1, pady=3)

    def CreateAddStaffGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        MAS.AddStaffGUI(self.master, 500, 650, '#85C1E9', '#EBF5FB', 'Add Staff')

    def CreateEditStaffGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        MES.EditStaffGUI(self.master, 300, 350, '#85C1E9', '#EBF5FB', 'Edit Staff')

    def CreateViewStaffGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        MVS.ViewStaffGUI(self.master, 300, 350, '#85C1E9', '#EBF5FB', 'View Staff')

    def CreateDeleteStaffGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        MDS.DeleteStaffGUI(self.master, 300, 350, '#85C1E9', '#EBF5FB', 'Delete Staff')

    def CreateCalculateWagesGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        MCW.CalculateWagesGUI(self.master, 500, 650, '#85C1E9', '#EBF5FB', 'Calculate Wages')

    def CreateRotaGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        MCR.CreateRotaGUI(self.master,  500, 650, '#85C1E9', '#EBF5FB', 'Calculate Rota')

    def CreateChangePasswordGUI(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
    def temp(self):
        print

    def Back(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        MM.OwnerMenu(self.master, 300, 350, '#85C1E9', '#EBF5FB', 'Manager Menu')

if __name__ == '__main__':
    root = Tk()
    gui = ManagerStaffSettingsGUI(root, 545, 350, '#85C1E9', '#EBF5FB', 'Staff Settings')
    root.mainloop()