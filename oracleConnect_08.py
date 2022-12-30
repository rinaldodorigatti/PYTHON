import cx_Oracle


# SCRIPT SIMPLE INSERT AS FETCHMANY, BIND VARIABLES, LIST OF TUPLES


rows = [
    (1, "version 2.2"),
    (2, "version 2.3"),
    (3, "version 3.1"),
    (4, "version 3.2"),
    (5, "version 3.4"),
    (6, "version 3.7"),
    (7, "version 3.9"),
    (8, "version 3.10")
]

username = "rickyd"
passw = "lu48cie"
dsn1 = "192.168.122.205:1521/DBHA001"

con = ''
cur = ''

try:
    con = cx_Oracle.connect(user=username, password=passw, dsn=dsn1)

except cx_Oracle.DatabaseError as er:
    print("Connexion on database DBHA001 failed : ", er)
else:
    try:
        cur = con.cursor()
        sql = "INSERT INTO PYTHON (id, version) VALUES (:1, :2)"
        cur.executemany(sql, rows, batcherrors=True)

        for error in cur.getbatcherrors():
            print("Error", error.message, "at row offset", error.offset)

        con.commit()

        print("Records inserted successfully")

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
