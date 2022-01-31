import tkinter as Tk
from tkinter import *
from tkinter import messagebox

import sqlite3
import hashlib
import binascii
import os
import time

from MainGUI import main

import ManagerMenu as MM
import ReceptionMenu as RM

class login(main):


    def __init__(self, master, height, width, bgcolour, framecolour, title):
        global UsernameVar, PasswordVar
        UsernameVar = StringVar()
        PasswordVar = StringVar()
        super().__init__(master, height, width, bgcolour, framecolour, title)

        master.title(title)
        self.ExitButton = Button(master, text='Exit', command=self.Exit, font=('Calibri', 12), height=1, width=12).grid(column=0, row=6, padx=10)


        self.UsernameLabel = Label(master, text='Username: ', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=4)
        self.UsernameEntry = Entry(master, text='....', textvariable=UsernameVar, width=25).grid(column=1, row=4)

        self.PasswordLabel = Label(master, text='Password: ', font=('Calibri', 12), bg=bgcolour).grid(column=0, row=5)
        self.PasswordEntry = Entry(master, text='....', textvariable=PasswordVar, show='*', width=25).grid(column=1, row=5)

        self.LoginButton = Button(master, text='Login', command=self.LoginFetch, font=('Calibri', 12), height=1, width=12).grid(column=1, row=6, pady=10)
    def LoginFetch(self):
        self.Username = UsernameVar.get()
        self.Password = PasswordVar.get()
        # print(self.Username, self.Password)

        # Connects to the db
        with sqlite3.connect('Montalto Estate Hotel.db') as conn:
            c = conn.cursor()

            LoginSql = ('''SELECT * FROM Staff WHERE Username= ?''')
            c.execute(LoginSql, (self.Username,))
            LoginFetch = c.fetchone()

            StoredPass = LoginFetch[15]

            for char in StoredPass:
                if char in "[](),'":
                    StoredPass = StoredPass.replace(char, '')

            if self.verify_password(StoredPass, self.Password) is not False:
                time.sleep(0.25)
                messagebox.showinfo('Login Succesfull', 'Success . . .')
                AccessSql = ('''SELECT JobTitle FROM Staff WHERE Username = ? AND Password = ?''')
                c.execute(AccessSql, [(self.Username), (self.Password)])
                AccessLevel = c.fetchall()
                AccessLevel = str(AccessLevel)
                
                # Fetches access level stored in db
                for char in AccessLevel:
                    if char in "[](),'":
                        AccessLevel = AccessLevel.replace(char, '')
                # Iterates over access level string stored in db to remove unnessecary characters for easier reading
                # print(AccessLevel)
                if AccessLevel == "Owner":
                    AllWidget = self.master.grid_slaves()

                    # Clears the widgets from the window
                    for i in AllWidget:
                        i.destroy()
                    # Calls the GUI class for the Owner/Manager menu
                    time.sleep(0.25)
                    MM.OwnerMenu(self.master, 375, 350, '#85C1E9', '#EBF5FB', 'Owner Menu')

                elif AccessLevel == "Manager":
                    AllWidget = self.master.grid_slaves()

                    for i in AllWidget:
                        i.destroy()
                    time.sleep(0.25)
                    MM.OwnerMenu(self.master, 375, 350, '#85C1E9', '#EBF5FB', 'Manager Menu')

                elif AccessLevel == 'Receptionist':
                    print('')

                else:
                    print('')
            else:
                messagebox.showerror('Error', 'Incorrect details . . .')

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)

        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)

        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def Exit(self):
        self.master.destroy()

if __name__ == '__main__':
    root = Tk()
    gui = login(root, 300, 475, '#85C1E9', '#EBF5FB', 'Staff Login')
    root.mainloop()
