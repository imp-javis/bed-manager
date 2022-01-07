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

# c.execute("DROP TABLE registered_user")
# c.execute("""CREATE TABLE registered_user (
#     email text,
#     password text,
#     photo text,
#     name text)""")

# c.execute("DELETE FROM registered_user")
# c.execute("INSERT INTO registered_user VALUES ('javis', '1234javis', 'marklee.png', 'Mark Lee')")
# c.execute("INSERT INTO registered_user VALUES ('new', '1234', 'taeyong.png', 'Lee Taeyong')")
# conn.commit()
def login(email, password): #login function
    c.execute("SELECT * FROM registered_user WHERE email LIKE :email AND password LIKE :password", {'email': email, 'password': password})
    if (c.fetchone() == None):
        return 1
    else: 
        return 2

def getUser(email, password):
    c.execute("SELECT photo, name FROM registered_user WHERE email LIKE :email AND password LIKE :password", {'email': email, 'password': password})
    user= c.fetchone()
    return user[0], user[1]

# c.execute("SELECT * FROM registered_user ")
# print(c.fetchall())

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
        clerkcheck integer,
        pwtr integer,  
        waittime integer)""") 
    except: 
        c.execute("""CREATE TABLE waitlist (
        patID integer,
        clerkcheck integer,
        pwtr integer, 
        waittime integer)""") 

# resetwaitlist()
def addtowaitlist(patID, time):
    c.execute("INSERT INTO waitlist  VALUES (:patID,'0','0', :waittime)", {'patID': patID, 'waittime': time})
    conn.commit()

def updateCC(patID, check):
    c.execute("UPDATE waitlist SET clerkcheck='{}' WHERE patID= '{}'".format(check, patID))
    conn.commit()

def updatePWTR(patID, check):
    c.execute("UPDATE waitlist SET pwtr='{}' WHERE patID= '{}'".format(check, patID))
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
        bed text,
        discharge integer,
        lounge integer,
        dis_sum integer,
        dis_meds integer,
        downstream text,
        death integer)""") 
    except:
        c.execute("""CREATE TABLE patient_inBed (
        patID integer
        bed text
        discharge integer,
        lounge integer,
        dis_sum integer,
        dis_meds integer,
        downstream text
        death integer)""") 

#resetbedallocation()


#--------------- bed allocation functions -----------------

#def addtoBed(patID, bed):
#    c.execute("INSERT INTO patient_inBed (patID, bed) VALUES (:patID, :bed)", {'patID': patID, 'bed': bed})
#    conn.commit()

def addtoBed(patID, bed, discharge, lounge, dis_sum, dis_meds, downstream, death):
    c.execute("INSERT INTO patient_inBed VALUES (:patID, :bed, :discharge, :lounge, :dis_sum, :dis_meds, :downstream, :death)", {'patID': patID, 'bed': bed, 'discharge': discharge, 'lounge': lounge, 'dis_sum': dis_sum, 'dis_meds': dis_meds, 'downstream': downstream,'death': death})
    conn.commit()

def getPatientsinBed():
    c.execute("SELECT * FROM patient_inBed ORDER BY bed")
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



#---------------- patient status for patients in discharge lounge ---------------------

def resetdischargelounge():
    try:
        c.execute("""DROP TABLE patient_inLounge""")
        c.execute("""CREATE TABLE patient_inLounge (
        patID integer,
        bed text,
        discharge integer,
        lounge integer,
        dis_sum integer,
        dis_meds integer)""") 
    except:
        c.execute("""CREATE TABLE patient_inLounge (
        patID integer
        bed text
        discharge integer,
        lounge integer,
        dis_sum integer,
        dis_meds integer)""") 

#resetdischargelounge()




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
        c.execute("""CREATE TABLE wardAvailability (
        cardio integer,
        endo integer,
        gastro integer,
        geri integer,
        resp integer)""") 

#resetwardavailability()


# conn.close() #close connections