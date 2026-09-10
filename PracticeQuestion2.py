import psycopg
conn=psycopg.connect("postgresql://neondb_owner:npg_N4it1eRYyUzd@ep-winter-queen-ayzfofj8-pooler.c-5.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
cur=conn.cursor()


def project():
    entries = []
    n=int(input("No of values you want to enter:"))
    for i in range(n):
        entry = input("Enter values: ").split()
        entries.append(entry)
    # entry1=input("Enter values to insert seperated by space:").split()
    # entry2=input("Enter values to insert seperated by space:").split()
    # entry3=input("Enter values to insert seperated by space:").split()
    # entry1=[1111,"G","77.12"]
    # entry2=[2222,"U","99.0"]
    # entry3=[4444,"J","33.7"]
    
    # entries.append(entry1)
    # entries.append(entry2)
    # entries.append(entry3)
    for i in range(len(entries)):
        for char in entries[i][1]:
            if char.isdigit():
                print("Invalid Name to Insert")
                return

    for i in range(len(entries)):
        int_part=int(float(entries[i][2]))
        year,month=entries[i][2].split(".")
        if int(month)>12:
            print( "Invalid Age,Check Again.")
            return
        
        if int(month)==12:
            entries[i][2]=int_part+1

        
    cur.execute("""CREATE TABLE USERS (ID INT PRIMARY KEY,
    NAME VARCHAR(50),AGE FLOAT)""")
    conn.commit()
    print("table created")
    for i in range(len(entries)):
        check_condition="""SELECT id FROM USERS WHERE ID=%s"""

        cur.execute(check_condition,(entries[i][0],))
        if cur.fetchone() is None:

            insert_query="""INSERT INTO USERS VALUES(%s,%s,%s)"""
            cur.execute(insert_query,(entries[i][0],entries[i][1],entries[i][2]))
            print(entries[i])
            print("values inserted")
        else:
            print("Id Already Present")
    conn.commit()

project()

conn.close()
