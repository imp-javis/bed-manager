import sqlite3
# from login_functions import  User

conn = sqlite3.connect('amu.db')

c = conn.cursor()

# c.execute("DROP TABLE dummy_table")
# c.execute("""CREATE TABLE waiting_list (
#     first text, 
#     last text,
#     age integer,
#     gender text,
#     diagnosis text)""") 

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

def addtowaitlist(first, last, age, gender, diagnosis):
    c.execute("INSERT INTO waiting_list VALUES (:first, :last, :age, :gender, :diagnosis)", {'first': first, 'last': last, 'age': age, 'gender': gender, 'diagnosis': diagnosis})
    conn.commit()
    
def getLast(row):
    c.execute("SELECT first, last FROM waiting_list WHERE rowid LIKE :row", {'row': row})
    names= c.fetchone()
    return([names[0], names[1]])

def getListSize():
    c.execute("SELECT COUNT(*) FROM waiting_list")
    res= c.fetchone()
    return res[0]

# addtowaitlist("mel", "kasim", 20, "female", "crazy")

# c.execute("SELECT * FROM waiting_list")
# print(c.fetchall())

# c.execute("SELECT COUNT(*) FROM dummy_table")
# res= c.fetchone()
# row= res[0]
# c.execute("SELECT rowid, * FROM dummy_table WHERE rowid LIKE :row", {'row': row})
# print(c.fetchall())

# def getContent():
#     c.execute("SELECT * FROM waiting_list")
#     items= c.fetchall()
#     return items

# def addwait(rownumber):
#     c.execute("SELECT * FROM waiting_list where ")
    # print(res[0])
# c.execute("INSERT INTO registered_user VALUES ('javis', '1234javis')")
# conn.commit() #commit changes
# user1= User('zatyhan', '1234zaty')
# 
# c.execute("DELETE FROM registered_user WHERE email='javis'")
# conn.commit()
# print(c.fetchall())
# c.execute("SELECT * FROM registered_user")
# items= c.fetchall()
# for item in items:
#     print(item[0])


# print(login('zatyhan', '1234zaty'))
# c.execute("SELECT * FROM registered_user")
# print(c.fetchall()) # only returns one row

# conn.close() #close connections

