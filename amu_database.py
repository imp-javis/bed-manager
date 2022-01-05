import sqlite3
# from login_functions import  User

conn = sqlite3.connect('amu.db')

c = conn.cursor()

def reset():
    c.execute("DROP TABLE waiting_list")
    c.execute("""CREATE TABLE waiting_list (
        first text, 
        last text,
        age integer,
        gender text,
        diagnosis text,
        timer blob,
        isolation integer)""") 

def coloursys():
    c.execute("DROP TABLE colourcount")
    c.execute("""CREATE TABLE colourcount (
        green integer, 
        yellow integer,
        red integer,
        black integer)""")

# coloursys()
def resetgoingBlack():
    c.execute("DROP TABLE goingBlack")
    c.execute("""CREATE TABLE goingBlack (
        time integer)""")



def toBlack(time):
    c.execute("DELETE FROM goingBlack")
    c.execute("INSERT INTO goingBlack VALUES (:time)", {'time': time})

def getBlack():
    c.execute("SELECT * FROM goingBlack")
    time= c.fetchone()
    return time[0]

# print(getBlack())
# resetgoingBlack()
# c.execute("""CREATE TABLE patient_inBed(
#         first text, 
#         last text,
#         age integer,
#         gender text,
#         diagnosis text,
#         isolation text,
#         bed text,
#         discharge text,
#         discharge_sum text,
#         discharge_meds text,
#         )""") 

# reset()

 
# c.execute("""CREATE TABLE registered_user (
#     email text,
#     password text)""")

def login(email, password):
    c.execute("SELECT * FROM registered_user WHERE email LIKE :email AND password LIKE :password", {'email': email, 'password': password})
    if (c.fetchone() == None):
        return 1
    else: 
        return 2

def addtowaitlist(first, last, age, gender, diagnosis, time, isolate):
    c.execute("INSERT INTO waiting_list VALUES (:first, :last, :age, :gender, :diagnosis, :time, :isolate)", {'first': first, 'last': last, 'age': age, 'gender': gender, 'diagnosis': diagnosis, 'time': time, 'isolate': isolate })
    conn.commit()

# def getTime():
#     c.execute("SELECT timer FROM waiting_list WHERE rowid LIKE :row", {'row': row})
#     times= c.fetchall()
#     return times

def getDetails(row):
    c.execute("SELECT first, last FROM waiting_list WHERE rowid LIKE :row", {'row': row})
    lists= c.fetchone()
    return lists[0], lists[1]

def getListSize():
    c.execute("SELECT COUNT(*) FROM waiting_list")
    res= c.fetchone()
    return res[0]

def getContent():
    c.execute("SELECT * FROM waiting_list")
    items= c.fetchall() #c.fetchone()
    return items

def deletePat(first, last):
    c.execute("DELETE FROM waiting_list WHERE first= '{}' AND last= '{}'".format(first, last))
    conn.commit()

def getPatWithBed(rowsWithBeds):
    c.execute("SELECT * FROM waiting_list WHERE row = '{}'".format(rowWithBeds))
    items = c.fetchall() #c.fetchone()
    return items    # returns a list of patients with beds assigned


def updatecolour(green, yellow, red, black):
    c.execute("DELETE FROM colourcount")
    c.execute("INSERT INTO colourcount VALUES (:green, :yellow, :red, :black)", {'green': green, 'yellow': yellow, 'red': red, 'black': black})
    conn.commit()

def getColournum():
    c.execute("SELECT * FROM colourcount")
    items= c.fetchall() #c.fetchone()
    return items  

# print(getColournum())
# c.execute("SELECT * FROM waiting_list")
# print(c.fetchall())

# conn.close() #close connections

