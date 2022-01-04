import sqlite3
# from login_functions import  User

conn = sqlite3.connect('patientList.db')

c = conn.cursor()

def reset():
    c.execute("DROP TABLE patient_inBed")
    c.execute("""CREATE TABLE patient_inBed(
         bed text,
         first text, 
         last text,
         age integer,
         gender text,
         diagnosis text,
         isolation text,
         discharge integer,
         discharge_lounge integer
         discharge_sum integer,
         discharge_meds integer,
         destination text,
         death integer
         )""")

    c.execute("DROP TABLE patient_inLounge")
    c.execute("""CREATE TABLE patient_inLounge(
         first text, 
         last text,
         age integer,
         gender text,
         diagnosis text,
         isolation text,
         discharge integer,
         discharge_lounge integer
         discharge_sum integer,
         discharge_meds integer,
         )""")

    patient_inBed()
    patient_inLounge()



# reset()

# this inserts patient info into the bed they have been assigned
def addtoBed(first, last, age, gender, diagnosis, isolate):
    c.execute("INSERT INTO patient_inBed (first, last, age, gender, diagnosis, isolation) VALUES (:first, :last, :age, :gender, :diagnosis, :isolate)", {'first': first, 'last': last, 'age': age, 'gender': gender, 'diagnosis': diagnosis, 'time': time, 'isolate': isolate})
    conn.commit()

# function to get ALL patient details of a SINGLE patient from list of patient_inBed (can send patient info to patient_inLounge or destination.db)
def getDetails(row):
    c.execute("SELECT FROM patient_inBed WHERE rowid LIKE :row", {'row': row})
    lists = c.fetchone()
    return lists

def getListSize():
    c.execute("SELECT COUNT(*) FROM patient_inBed")
    res = c.fetchone()
    return res[0]

def getContent():
    c.execute("SELECT * FROM patient_inBed")
    items= c.fetchall() #c.fetchone()
    return items

def deletePat(first, last):
    c.execute("DELETE FROM patient_inBed WHERE first = '{}' AND last= '{}'".format(first, last))
    conn.commit()
    
def sortByBed():
    c.execute("SELECT * FROM patient_inBed ORDER BY bed")
    conn.commit()


# conn.close() #close connections

