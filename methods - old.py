import sqlite3

DB_FILENAME = 'awards.db'

class UserNotFound(Exception):
    pass
    
class Student:
    def __init__(self,
                 id,
                 student_code,
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
                 ):
        self.id = id
        self.student_code = student_code
        self.fname = fname
        self.lname = lname
        self.pname = pname
        self.year_level = year_level
        self.home_group = home_group
        self.house = house
        self.gender = gender
        self.address = address
        self.suburb = suburb
        self.postcode = postcode
        self.primary_parent = primary_parent
        self.attending = attending

    def __str__(self):
        #return '{fname} {lname} ({student_code})'.format(fname=self.fname, lname=self.lname, student_code=self.student_code)
        return '{} {} - {}'.format(self.fname, self.lname, self.student_code)
    

class Recipient:
    def __init__(self, id, student, award):
        self.id = id
        self.student = student
        self.award = award
        # student and award point to an object of same name

    def __str__(self):
        return '{} - {} {}'.format(self.id, self.student, self.award)
        
class Award:
    def __init__(self,
                 id,
                 name,
                 description,
                 title1,
                 title2,
                 title3,
                 subtitle,
                 special,
                 quantity,
                 prize,
                 ):
        self.id = id
        self.name = name
        self.description = description
        self.title1 = title1
        self.title2 = title2
        self.title3 = title3
        self.subtitle = subtitle
        self.special = special
        self.quantity = quantity
        self.prize = prize

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)


def get_student(id):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.execute('''SELECT *
        FROM students
        WHERE id=?''', (id,))
    row = cur.fetchone()
    if row is None:
        raise UserNotFound('{} does not exist'.format(id))
    return Student(*row)

def get_award(id):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.execute('''SELECT *
        FROM awards
        WHERE id=?''', (id,))
    row = cur.fetchone()
    if row is None:
        raise UserNotFound('{} does not exist'.format(id))
    return Award(*row)

def find_recipients():
    recipients = []
    recipient = None

    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.execute('''SELECT * FROM recipients r''')
    for row in cur:
        student = get_student(row[1])
        award = get_award(row[2])
        recipient = Recipient(row[0], student, award)
        print(recipient)
        recipients.append(recipient)
    return recipients

def find_recipients_by_year(year_level):
    recipients = []
    recipient = None

    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.execute('''SELECT r.*
      FROM recipients r
      JOIN students s ON r.student_id = s.id
      WHERE s.year_level = ?
      ORDER BY s.lname, s.fname
      ''', [year_level])
    for row in cur:
        student = get_student(row[1])
        award = get_award(row[2])
        recipient = Recipient(row[0], student, award)
        recipients.append(recipient)
    return recipients

def find_recipients_by_year_name_only(year_level):
    students = []
    stud = None
    last = None
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.execute('''SELECT s.id, s.student_code, s.lname, s.fname
      FROM students s
      JOIN recipients r ON s.id = r.student_id
      WHERE s.year_level = ?
      ORDER BY s.lname, s.fname
      ''', [year_level])
    for row in cur:
        stud = row
        if stud != last:
            students.append(stud)
            last = stud
    return students

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()


