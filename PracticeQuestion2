import psycopg
conn=psycopg.connect("postgresql://neondb_owner:npg_N4it1eRYyUzd@ep-winter-queen-ayzfofj8-pooler.c-5.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
cur=conn.cursor()


def project():
    entry1=input("Enter values to insert seperated by space:").split()
    entry2=input("Enter values to insert seperated by space:").split()
    entry3=input("Enter values to insert seperated by space:").split()
    # entry1=[1111,"G",77.12]
    # entry2=[2222,"U",99.0]
    # entry3=[4444,"J",33.7]
    entries=[]
    entries.append(entry1)
    entries.append(entry2)
    entries.append(entry3)
    for i in range(len(entries)):
        entries[i][2]=float(entries[i][2])
        int_part=int(entries[i][2])
        decimal=round((entries[i][2]-int_part),2)
        print(decimal)
        if decimal>0.12:
            print("Months In Age cannot be greater than 12")
            return
        if decimal==0.12:
            
            entries[i][2]=int_part+1
            print(entries[i][2])
        
    cur.execute("""CREATE TABLE USERS (ID INT PRIMARY KEY,
    NAME VARCHAR(50),AGE FLOAT)""")
    conn.commit()
    check_condition="""SELECT id FROM USERS WHERE ID=%s"""
    print("table created")
    for i in range(len(entries)):

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
