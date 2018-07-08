import sqlite3

# Creating a sqlite database file called email #
conn = sqlite3.connect('email.sqlite')
# Creating a file handle to perform operations on the database #
cur = conn.cursor()

# Droping the pre-existing table #
cur.execute ('DROP TABLE IF EXISTS Counts')
# Creating a table called Counts #
cur.execute ('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Opening the mbox.txt file #
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)

# Selecting the correct lines #
for line in fh:
    if not line.startswith('From'):
        continue
    pieces = line.split()
    print(pieces)

# Closing the connection #
conn.close()
