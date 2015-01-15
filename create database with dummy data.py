import sqlite3
import os

DB_FILENAME = 'awards.db'

if os.path.exists(DB_FILENAME):
    os.remove(DB_FILENAME)

# Connect to the awards database and assing it to conn
conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

cur.execute('''CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    student_id TEXT NOT NULL,
    fname TEXT,
    lname TEXT,
    pname TEXT,
    year_level INTEGER,
    home_group TEXT,
    house TEXT,
    gender TEXT,
    address TEXT,
    suburb TEXT,
    postcode TEXT,
    primary_parent TEXT,
    attending TEXT
    );''')

cur.execute('''CREATE TABLE awards (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    title1 TEXT,
    title2 TEXT,
    title3 TEXT,
    subtitle TEXT,
    special TEXT,
    quantity INTEGER,
    prize TEXT
    );''')

cur.execute('''CREATE TABLE recipients (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    student_id INTEGER NOT NULL,
    award_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
    FOREIGN KEY (award_id) REFERENCES awards(id)
    );''')

cur.execute("""INSERT INTO students (
            student_id,
            fname,
            lname,
            pname,
            year_level,
            home_group,
            house,
            gender,
            address,
            suburb,
            postcode,
            primary_parent,
            attending
            )
            VALUES (
            'BRU0004',
            'Leah',
            'Bruckner',
            'Leah',
            10,
            'S7',
            'Swan',
            'F',
            '1 Jimmy Murran Street',
            'Ocean Grove',
            '3226',
            'Neil Bruckner',
            'Yes'
            );""")
cur.execute("INSERT INTO awards (name) VALUES ('Excellent Achievement Award');")
cur.execute("INSERT INTO awards (name) VALUES ('Outstanding Effort Award');")
cur.execute("INSERT INTO recipients (student_id, award_id) VALUES (1, 1);")
cur.execute("INSERT INTO recipients (student_id, award_id) VALUES (1, 2);")

# If you don't commit the changes aren't written to the file
conn.commit()

# Close the cursor
cur.close()

# Close the connection
conn.close()
