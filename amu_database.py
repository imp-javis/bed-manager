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
# c.execute("""CREATE TABLE dummy_table (
#     first text, 
#     last text,
#     age integer,
#     gender text,
#     diagnosis text)""")
 
# c.execute("INSERT INTO dummy_table VALUES ('mel', 'kasim', 20, 'fem', 'crazy')")
# conn.commit()

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
    print("hey{}you".format(first))
    print(last)
    # c.execute("DELETE FROM waiting_list WHERE first LIKE :first AND last LIKE :last", {'first': first, 'last': last})
    c.execute("DELETE FROM waiting_list WHERE first= '{}' AND last= '{}'".format(first, last))
    # c.execute("DELETE FROM waiting_list WHERE first= 'seo joon AND last = park")
    conn.commit()
    c.execute("SELECT * FROM waiting_list")
    items= c.fetchall() #c.fetchone()
    print(items)
    # print('done')



# deletePat('nur ', 'jamadk')

# print(getContent())
# c.execute("SELECT * FROM waiting_list")
# print(c.fetchall())

# c.execute("SELECT COUNT(*) FROM dummy_table")
# res= c.fetchone()
# row= res[0]
# c.execute("SELECT rowid, * FROM dummy_table WHERE rowid LIKE :row", {'row': row})
# print(c.fetchall())



# def addwait(rownumber):
#     c.execute("SELECT * FROM waiting_list where ")
    # print(res[0])
# c.execute("INSERT INTO registered_user VALUES ('javis', '1234javis')")
# conn.commit() #commit changes


# conn.close() #close connections

