import sqlite3
# from login_functions import  User

conn = sqlite3.connect('amu.db')

c = conn.cursor()

# c.execute("""CREATE TABLE waiting_list ( 
#     first text, 
#     last text,
#     reg_number integer,
#     age integer,
#     gender text,
#     diagnosis text)""") 

# c.execute("""CREATE TABLE registered_user (
#     email text,
#     password text)""")



def login(email, password):
    c.execute("SELECT * FROM registered_user WHERE email LIKE :email AND password LIKE :password", {'email': email, 'password': password})
    if (c.fetchone() == None):
        return 1
    else: 
        return 2

c.execute("INSERT INTO registered_user VALUES ('javis', '1234javis')")
conn.commit() #commit changes
# user1= User('zatyhan', '1234zaty')

# c.execute("DELETE FROM registered_user WHERE email='javis2'")
conn.commit()
# print(c.fetchall())

# for item in items:
#     print(item)

# print(login('zatyhan', '1234zaty'))
c.execute("SELECT * FROM registered_user")
print(c.fetchall()) # only returns one row

conn.close() #close connections

