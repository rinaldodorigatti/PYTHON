import cx_Oracle
import configOracle as Config


# SCRIPT SIMPLE SELECT AS FETCHMANY

connection = None
batch_size = 10

sql = """SELECT NAME,ABBREV,PAYS FROM COMPANY"""

print("-" * 80)
print("|", "{:>40}".format("NAME"), " | ", "{:<10}".format("ABBREV"), " | ", "{:<10}".format("PAYS"), "|")
print("-" * 80)

try:
    with cx_Oracle.connect(
            Config.username,
            Config.passw,
            Config.dsn,
            encoding=Config.encoding,
            mode=cx_Oracle.SYSDBA) as connection:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            while True:
                rows = cursor.fetchmany(batch_size)
                if not rows:
                    break
                for row in rows:
                    print("|", "{:>40}".format(row[0]), " | ", "{:>10}".format(row[1]), " | ", "{:>10}".format(row[2]), "|")
        print("-" * 80)
        print("Oracle Version : ", connection.version)
except cx_Oracle.Error as err:
    print(err)

print("-" * 80)
