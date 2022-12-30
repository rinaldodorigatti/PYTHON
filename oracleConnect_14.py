import cx_Oracle
import time


def insertrecord():
    connection1 = cx_Oracle.connect(user="rickyd", password="lu48cie",
                                   dsn="192.168.122.205:1521/DBHA001")
    cursor1 = connection1.cursor()

    rows = [(11, 1, "Wiget Frederic", "99 92", "BC"),
            (22, 1, "Marc Audret", "99 93", "CB"),
            (33, 1, "Philippe Dubois", "99 94", "AC"),
            (44, 1, "Hubert Jean", "99 95", "AZ"),
            (55, 1, "Shirin Azartach", "99 96", "OP")]

    cursor1.executemany("INSERT INTO PHONES02(PHONE_ID, MANAGER, NOM_PRENOM, PHONE_NUMBER, PHONE_TYPE)"
                        "VALUES (:1, :2, :3, :4, :5)", rows)

    for error in cursor1.getbatcherrors():
        print("Error", error.message.rstrip(), "at row offset", error.offset)

    res2 = cursor1.callfunc('myfunc', int, ('efg', 3))
    print(res2)

    myvar = cursor1.var(int)
    cursor1.callproc('myproc', (123, myvar))
    print(myvar.getvalue())

    connection1.commit()
    # connection1.rollback()


connection = cx_Oracle.connect(user="rickyd", password="lu48cie",
                               dsn="192.168.122.205:1521/DBHA001")

start = time.time()

cursor = connection.cursor()

sql = """SELECT PHONE_ID, MANAGER, NOM_PRENOM, PHONE_NUMBER, PHONE_TYPE FROM PHONES02"""

cursor.execute(sql)

res = cursor.fetchall()

print("-" * 70)
print("%-10s %-10s %-30s %-10s %-10s" % ("ID", "MANAGER", "FULL NAME", "PHONE", "TYPE"))
print("-" * 70)
for row in res:
    print("%-10s %-10s %-30s %-10s %-10s" % (row[0], row[1], row[2], row[3], row[4]))
print("-" * 70)
print("Database version : ", connection.version)
print("Client version:", cx_Oracle.clientversion())
print("-" * 70)
for a, b, c, d, e in res:
    print("%-10s %-10s %-30s %-10s %-10s" % (a, b, c, d, e))
print("-" * 70)
elapsed = (time.time() - start)
print("Elasped time : %.5f" % elapsed)
print("-" * 70)
insertrecord()

