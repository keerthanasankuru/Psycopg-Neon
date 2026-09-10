import psycopg

my_db="postgresql://neondb_owner:npg_N4it1eRYyUzd@ep-winter-queen-ayzfofj8.c-5.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
conn=psycopg.connect(my_db)
cur=conn.cursor()

def create_table():
    cur.execute("""CREATE TABLE STUDENTS(ID INT PRIMARY KEY,NAME VARCHAR(50),AGE INT)""")
    print("Table Student Got Created")
    conn.commit()
    
def insert_table():
    id=int(input("Enter Id:"))
    name=input("Enter Name:")
    age=int(input("Enter Age:"))
    cur.execute("""INSERT INTO STUDENTS VALUES(%s,%s,%s)""",(id,name,age))
    print("Got inserted")
    conn.commit()
def delete_table():   
    user_id_to_delete=int(input("Enter Student ID to Delete:"))
    cur.execute("""DELETE FROM STUDENTS WHERE ID=%s""",(user_id_to_delete,))
    conn.commit()

def exitt():
    print("EXITING")

def project():
    user_input=int(input("Enter 1:Create Table/2:Insert Values/3:Delete Table/4:Exit:-"))
    if user_input==1:
        create_table()
    if user_input==2:
        insert_table()
    if user_input==3:
        delete_table()
    if user_input==4:
        exitt()
    else:
        print("Invalid Input")
    
project()



conn.close()
