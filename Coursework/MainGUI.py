import tkinter as tk
from tkinter import *

class main(Frame):

    def __init__(self, master, height, width, bgcolour, framecolour, title):
        Frame.__init__(self, master)

        #master.grid_rowconfigure(0, weight=0)
        #master.grid_columnconfigure(0, weight=2)

        self.height = height
        self.width = width
        self.title = title
        self.bgcolour = bgcolour
        self.framecolour = framecolour
        TitleFrame = Frame(master, bg=self.framecolour, width=self.width, height=self.height/7).grid(row=0, columnspan=3, sticky=N)


        self.WindowLabel = Label(master, text='', fg=self.framecolour, bg=self.bgcolour).grid(row=1, columnspan=4)

        #sets window size and colour
        master.minsize(width=self.width, height=self.height)
        master.maxsize(width=self.width, height=self.height)
        master.configure(background=self.bgcolour)

        # Labels for current window and company
        CompanyTitle = Label(TitleFrame, text='Montalto Estate Hotel', bg=self.framecolour, font=('Calibri', 15), fg='Black').grid(column=1, row=0, sticky=N)
        WindowTitle = Label(TitleFrame, text=self.title, bg=self.bgcolour, font=('Calibri', 15), fg='Black').grid(row=1, column=1)

        Photo = PhotoImage(file='montalto estate.gif')
        CompanyLogo = Label(TitleFrame, image=Photo)
        CompanyLogo.image = Photo
        CompanyLogo.grid(column=2, row=0)
if __name__ == '__main__':
    root = Tk()
    gui = main(root, 380, 450, 'grey', 'white',  'one testy boi')
    root.mainloop()