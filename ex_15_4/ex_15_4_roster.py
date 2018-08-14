import json
import sqlite3

# Creating a sqlite database
conn = sqlite3.connect('roster.sqlite')
# Creating a file handle to perform operations in the database
cur = conn.cursor()

# Droping existing tables, creating tables,
cur.executescript("""
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Course (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    TEXT UNIQUE
);

CREATE TABLE Member (
    user_id  INTEGER,
    course_id   INTEGER,
    role    INTEGER,
    PRIMARY KEY (user_id, course_id))
""")

# Opening the json file to start reading it
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# Opening and loading the string of the json file
str_data = open(fname).read()
json_data = json.loads(str_data)

# Identifying entries and insert into the database
for entry in json_data:
    name = entry[0];
    title = entry[1];
    role = entry[2];
    print((name, title, role))

    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (name, ))
    cur.execute('''SELECT id FROM User WHERE name = ?''', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', (title, ))
    cur.execute('''SELECT id FROM Course WHERE title = ?''', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?,?,?)''', (user_id, course_id, role))

    conn.commit()
