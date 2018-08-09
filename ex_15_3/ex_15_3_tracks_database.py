# Importing XML data and sqlite3 #
import xml.etree.ElementTree as ET
import sqlite3

# Creating a sqlite database file #
conn = sqlite3.connect('tracksdb.sqlite')
# Creating a file handle to perform operations on the database #
cur = conn.cursor()

# Using executescript to execute all following codes at once instead of plain execute, in order to create multiple tables for the database #

conn.executescript ("""
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE if EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

""")

# Prompting the XML file name #
fname = input ('Enter file location: ')
if len(fname) < 1:
    fname = 'Library.xml'


# Writing a custom function to look through the following entries #
# <key>Track ID</key><integer>369</integer> #
# <key>Name</key><string>Another One Bites The Dust</string> #
# <key>Artist</key><string>Queen</string> #
# <key>Album</key><string>Greatest Hits</string> #
# <key>Genre</key><string>Rock</string> #
# <key>Total Time</key><integer>217103</integer> #
# <key>Rating</key><integer>100</integer> #
# <key>Play Count</key><integer>55</integer> #
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None


# Pasring the string in the XML, and find all data within dict/dict/dict directory #
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

# Going through all the entries within dict/dict/dict #
for entry in all:
    if (lookup(entry, 'Track ID') is None):
        continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    length = lookup(entry, 'Total Time')
    rating = lookup(entry, 'Rating')
    count = lookup(entry, 'Play Count')

# Doing sanity checking #
    if name is None or artist is None or album is None or genre is None:
        continue
# Printing the results out #
    print (name, artist, album, genre, length, rating, count)

# Inserting the values into the sqlite database #
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''' , (artist, ))
    cur.execute('''SELECT id FROM Artist WHERE name = ? ''', (artist, ))
    artist_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''' , (genre, ))
    cur.execute('''SELECT id FROM Genre WHERE name = ? ''', (genre, ))
    genre_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?,?)''', (artist_id, album))
    cur.execute('''SELECT id FROM Album WHERE title = ? ''', (album, ))
    album_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,?)''', (name, album_id, genre_id, length, rating, count))

# Commiting the SQL command to the database#
    conn.commit()
