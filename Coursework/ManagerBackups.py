import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import sqlite3
import os

from MainGUI import main
import ManagerMenu as MM

class CreateBackupMenuGUI(main):

    def __init__(self, master, height, width, bgcolour, framecolour, title):
        global StaffUsernameVar, NewPasswordVar
        StaffUsernameVar = StringVar()
        NewPasswordVar = StringVar()

        self.master = master
        super().__init__(master, height, width, bgcolour, framecolour, title)
        master.title(title)

        self.BackupDatabaseTableBtn = Button(self.master, text='Create Backup', command=self.CreateBackup, font=('Calibri', 12), width=18).grid(column=1, row=3, pady=3)
        self.RestoreFromBackup = Button(self.master, text='Restore Backup', command=self.RestoreFromBackuo, font=('Calibri', 12), width=18).grid(column=1, row=4, pady=3)

        self.BackButton = Button(master, text='Exit', command=self.Back, font=('Calibri', 12), width=8).grid(column=0, row=1, pady=10)


    def CreateBackup(self):
        with sqlite3.connect('Montalto Estate Hotel.db') as db:
            dbfile = 'D://CourseWork//ExampleBackup//Backup.db'
            if os.path.exists(dbfile):
                os.remove(dbfile)

            new_db = sqlite3.connect(dbfile)
            c = new_db.cursor()
            c.executescript("\r\n".join(db.iterdump()))
            new_db.close()

    def RestoreFromBackuo(self):
        with sqlite3.connect('ExampleBackup//Backup.db') as db:
            bckup = 'Montalto Estate Hotel'
            if os.path.exists(bckup):
                os.remove(bckup)

            RestoreTo = sqlite3.connect(bckup)
            c = RestoreTo.cursor()
            c.executescript("\r\n".join(db.iterdump()))
            RestoreTo.close()

    def Back(self):
        AllWidgets = self.master.grid_slaves()
        for i in AllWidgets:
            i.destroy()
        MM.OwnerMenu(self.master, 375, 350, '#85C1E9', '#EBF5FB', 'Manager Menu')

if __name__ == '__main__':
    root = Tk()
    gui = CreateBackupMenuGUI(root, 375, 400, '#85C1E9', '#EBF5FB', 'Backup Settings')
    root.mainloop()