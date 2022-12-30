import cx_Oracle
import configOracle as co

# SCRIPT SIMPLE SELECT AS FETCHONE AND BIND VARIABLES

connection = None

sql = "SELECT NAME,ABBREV,PAYS FROM COMPANY WHERE ABBREV = :ABBREV2"

print("-" * 80)
print("|", "{:>40}".format("NAME"), " | ", "{:<10}".format("ABBREV"), " | ", "{:<10}".format("PAYS"), "|")
print("-" * 80)

try:
    with cx_Oracle.connect(
            co.username,
            co.passw,
            co.dsn,
            encoding=co.encoding,
            mode=cx_Oracle.SYSDBA) as connection:
        with connection.cursor() as cursor:
            cursor.prepare(sql)
            cursor.execute(sql, {'ABBREV2':'LEON      '})
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                print("|", "{:>40}".format(row[0]), " | ", "{:>10}".format(row[1]), " | ", "{:>10}".format(row[2]), "|")
        print("-" * 80)
        print("Oracle Version : ", connection.version)
except cx_Oracle.Error as err:
    print(err)

print("-" * 80)
