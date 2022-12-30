import cx_Oracle


# SCRIPT SIMPLE SELECT AS CALLFUNC

user1 = "rickyd"
password1 = "lu48cie"
dsn1 = "192.168.122.205:1521/DBHA001"

con = ''
cur = ''

try:
    con = cx_Oracle.connect(user=user1, password=password1, dsn=dsn1)

except cx_Oracle.DatabaseError as er:
    print("Connexion on database DBHA001 failed : ", er)
else:
    try:
        cur = con.cursor()
        res = cur.callfunc('myfunc', int, ("version 3.11", 11))

        for error in cur.getbatcherrors():
            print("Error", error.message, "at row offset", error.offset)

        con.commit()

        print("Records selected successfully : ", res)

    except cx_Oracle.DatabaseError as eq:
        print("Query on database DBHA001 failed : ", eq)

    except Exception as ex:
        print('Exception Error:', ex)

    finally:
        if cur:
            cur.close()
finally:
    if con:
        con.close()
