import cx_Oracle
import configOracle as co

# SCRIPT SIMPLE SELECT AS FETCHONE

connection = None

sql = """SELECT NAME,ABBREV,PAYS FROM COMPANY"""

print("-" * 80)
print("|", "{:>40}".format("NAME"), " | ", "{:<10}".format("ABBREV"), " | ", "{:<10}".format("PAYS"), "|")
print("-" * 80)

try:
    connection = cx_Oracle.connect(
        co.username,
        co.passw,
        co.dsn,
        encoding=co.encoding,
        mode=cx_Oracle.SYSDBA)
    with connection.cursor() as cursor:
        cursor.execute(sql)
        while True:
            row = cursor.fetchone()
            if row is None:
                break
            print("|", "{:>40}".format(row[0]), " | ", "{:>10}".format(row[1]), " | ", "{:>10}".format(row[2]), "|")
    print("-" * 80)
    print("Oracle Version : ", connection.version)
except cx_Oracle.Error as err:
    print(err)
finally:
    if connection:
        connection.close()

print("-" * 80)
