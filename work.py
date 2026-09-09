import psycopg

my_db="postgresql://neondb_owner:npg_N4it1eRYyUzd@ep-winter-queen-ayzfofj8.c-5.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
conn=psycopg.connect(my_db)
cur=conn.cursor()

user_input=int(input("Enter 1/2/3/4:"))
if user_input==1:

    cur.execute("""CREATE TABLE STUDENTS(ID INT PRIMARY KEY,NAME VARCHAR(50),AGE INT)""")
    print("Got Created")
    conn.commit()
    
if user_input==2:
    id=int(input("Enter Id:"))
    name=input("Enter Name:")
    age=int(input("Enter Age:"))
    cur.execute("""INSERT INTO STUDENTS VALUES(%s,%s,%s)""",(id,name,age))
    print("Got inserted")
    conn.commit()
   
if user_input==3:
    user_id_to_delete=int(input("Enter Student ID to Delete:"))
    cur.execute("""DELETE FROM STUDENTS WHERE ID=%s""",(user_id_to_delete,))
    conn.commit()
if user_input==4:
    print("EXITING")

conn.close()