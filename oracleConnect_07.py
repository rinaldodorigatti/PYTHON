import cx_Oracle
import configOracle as config
import datetime


# SCRIPT SIMPLE SELECT AS FETCHALL, ORACLE PARAMETERS


sql = "SELECT NAME,TYPE,VALUE FROM V$PARAMETER"

datetj = datetime.datetime.now()
datej = datetj.strftime("%x")

print("*" * 126)

print("*            ORACLE SLES15 PARAMETERS", " " * 70,  f"{datej}" + "        *")
print("*" * 126)
print("-" * 126)
print("| ", "{:<50}".format("NAME"),
" | ", "{:<5}".format("TYPE"),
" | ", "{:<55}".format("VALUE"),
" |")
print("-" * 126)

try:
    with cx_Oracle.connect(
            config.username,
            config.passw,
            config.dsn,
            encoding=config.encoding,
            mode=cx_Oracle.SYSDBA) as connection:

        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            if rows:
                for name,type,value in rows:
                    print("| ", "{:<50}".format(name),
                    " | ", "{:<5}".format(type),
                    " | ", "{:<55}".format(str(value)),
                    " |")
            print("-" * 126)
            version = connection.version[:4]
            print("|" + "-" * 10, "Oracle Version : ", version, "-" * 90 + "|")
except cx_Oracle.Error as error:
    print(error)


print("-" * 126)
