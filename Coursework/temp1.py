
import os
import sqlite3

with sqlite3.connect('Montalto Estate Hotel.db') as db:

    dbfile = 'D://CourseWork//ExampleBackup//Backup.db'
    if os.path.exists(dbfile):
        os.remove(dbfile)

    new_db = sqlite3.connect(dbfile)
    c = new_db.cursor()
    c.executescript("\r\n".join(db.iterdump()))
    new_db.close()