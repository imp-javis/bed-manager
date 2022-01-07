import sqlite3
# from login_functions import  User

conn = sqlite3.connect('amu.db')

c = conn.cursor()

# list of existing tables in database: 
# 1. patientInfo for registered patients
# 2. waitlist
# 3. bed Allocation
# 4. patient Status
# 5. user registration

#----- login database-------------------

# c.execute("""CREATE TABLE registered_user (
#     email text,
#     password text)""")

def login(email, password): #login function
    c.execute("SELECT * FROM registered_user WHERE email LIKE :email AND password LIKE :password", {'email': email, 'password': password})
    if (c.fetchone() == None):
        return 1
    else: 
        return 2

 #------------Register patient---------------------
def reset(): # restart a table  if a table exist
    try: 
        c.execute("DROP TABLE patInfo")
        c.execute("""CREATE TABLE patInfo (
            patID integer PRIMARY KEY, 
            first text, 
            last text,
            age integer,
            gender text,
            diagnosis text,
            isolation integer)""") 
    except: 
        c.execute("""CREATE TABLE patInfo (
            patID integer PRIMARY KEY, 
            first text, 
            last text,
            age integer,
            gender text,
            diagnosis text,
            isolation integer)""") 

def register(first, last, age, gender, diagnosis, isolate): #register a table
    c.execute("INSERT INTO patInfo(first, last, age, gender, diagnosis, isolation) VALUES (:first, :last, :age, :gender, :diagnosis, :isolate)", {'first': first, 'last': last, 'age': age, 'gender': gender, 'diagnosis': diagnosis, 'isolate': isolate })
    conn.commit()

def getPatientID(first, last, age, gender, diagnosis, isolate):
    c.execute("SELECT patID FROM patInfo WHERE first='{}' AND last='{}' AND age='{}' AND gender='{}' AND diagnosis='{}' AND isolation='{}'".format(first, last, age, gender, diagnosis, isolate))
    getID= c.fetchone()
    return getID

def getPatientInfo(patID):
    c.execute("SELECT * FROM patInfo where patID= :patID", {'patID': patID})
    info= c.fetchone()
    return info
# reset()

#--------------Adding to waitlist-------------
def resetwaitlist():
    try:
        c.execute("""DROP TABLE waitlist""")
        c.execute("""CREATE TABLE waitlist (
        patID integer, 
        waittime integer)""") 
    except: 
        c.execute("""CREATE TABLE waitlist (
        patID integer, 
        waittime integer)""") 

# resetwaitlist()

def addtowaitlist(patID, time):
    c.execute("INSERT INTO waitlist  VALUES (:patID, :waittime)", {'patID': patID, 'waittime': time})
    conn.commit()

def getPatientinWaitlist():
    c.execute("SELECT * FROM waitlist")
    items = c.fetchall()
    return items

def deletePatfromWaitlist(id):
    c.execute("DELETE FROM waitlist WHERE patID= '{}'".format(id))
    conn.commit()

def getListSize(): #get the size of the waitlist
    c.execute("SELECT COUNT(*) FROM waitlist")
    res= c.fetchone()
    return res[0]

#-------------------- highlight functions----------------------

def resetcoloursys(): #function to update the waitlist patient status
    try:
        c.execute("DROP TABLE colourcount")
        c.execute("""CREATE TABLE colourcount (
            green integer, 
            yellow integer,
            red integer,
            black integer)""")
    except:
        c.execute("""CREATE TABLE colourcount (
            green integer, 
            yellow integer,
            red integer,
            black integer)""")

# coloursys()

# colour code for waitlist
def updatecolour(green, yellow, red, black):
    c.execute("DELETE FROM colourcount")
    c.execute("INSERT INTO colourcount VALUES (:green, :yellow, :red, :black)", {'green': green, 'yellow': yellow, 'red': red, 'black': black})
    conn.commit()

def getColournum():
    c.execute("SELECT * FROM colourcount")
    items= c.fetchall() #c.fetchone()
    return items  



#---------------- patient status for patients in bed ---------------------

def resetbedallocation():
    try:
        c.execute("""DROP TABLE patient_inBed""")
        c.execute("""CREATE TABLE patient_inBed (
        patID integer,
        bed text)""") 
    except:
        c.execute("""CREATE TABLE patient_inBed (
        patID integer
        bed text)""") 

# resetbedallocation()


#--------------- bed allocation functions -----------------

def addtoBed(patID, bed):
    c.execute("INSERT INTO patient_inBed VALUES (:patID, :bed)", {'patID': patID, 'bed': bed})
    conn.commit()

# to sort the list of patients in bed in order of their beds (A1-4, B1-4, C1-4, D1-4, R1-4)
def sortByBed():
    c.execute("SELECT * FROM patient_inBed ORDER BY bed")
    conn.commit()

def getPatientsinBed():
    c.execute("SELECT * FROM patient_inBed")
    items = c.fetchall()
    return items

def deletePatfromBed(id):
    c.execute("DELETE FROM patient_inBed WHERE patID= '{}'".format(id))
    conn.commit()

def getBedListSize():   #get the size of the waitlist
    c.execute("SELECT COUNT(*) FROM patient_inBed")
    res= c.fetchone()
    return res[0]

def bedAvailability():
    c.execute("SELECT COUNT(*) FROM patient_inBed")
    res = c.fetchone()
    y = 20 - res[0]
    return y


# to fetch beds and their current status: occupied, discharge, downstream (if not on list, then free)
# def takenBeds():



#---------------- patient status for patients in bed/lounge ---------------------






#---------------- free bed availability in downstream wards ---------------------


def resetwardavailability():
    try:
        c.execute("""DROP TABLE wardAvailability""")
        c.execute("""CREATE TABLE wardAvailability (
        cardio integer,
        endo integer,
        gastro integer,
        geri integer,
        resp integer)""") 
    except:
        c.execute("""CREATE TABLE patient_inBed (
        cardio integer,
        endo integer,
        gastro integer,
        geri integer,
        resp integer)""") 




# conn.close() #close connections