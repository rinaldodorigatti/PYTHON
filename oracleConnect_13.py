import cx_Oracle

connection = cx_Oracle.connect(user="rickyd", password="lu48cie",
                               dsn="192.168.122.205:1521/DBHA001")

print("Inserting data...")
cursor2 = connection.cursor()

cursor2.execute("truncate table PTAB")

longString = ""

for i in range(5):
    char = chr(ord('a'))
    longString += char
    cursor2.execute("INSERT INTO PTAB values (:1, :2)",
                    ("String data " + longString, i + 1))

connection.commit()

print("Querying data...")
cursor2.execute("SELECT * FROM PTAB WHERE myid = :id", {'id': 1})

(idd, clob) = cursor2.fetchone()

print("CLOB length:", clob)

clobdata = clob

print("CLOB data:", clobdata)


class MyConnection(cx_Oracle.Connection):
    def __init__(self):
        print("Connecting to database")
        """return super(MyConnection, self).__init__(user="rickyd", password="lu48cie",
        dsn="192.168.122.205:1521/DBHA001")"""
        super(MyConnection, self).__init__(user="rickyd", password="lu48cie", dsn="192.168.122.205:1521/DBHA001")

    def cursor(self):
        return MyCursor(self)


class MyCursor(cx_Oracle.Cursor):

    def execute(self, statement, args):
        print("Executing:", statement)
        print("Arguments:")
        for argIndex, arg in enumerate(args):
            print("  Bind", argIndex + 1, "has value", repr(arg))
            return super(MyCursor, self).execute(statement, args)

    def fetchone(self):
        print("Fetchone()")
        return super(MyCursor, self).fetchone()


con = MyConnection()
cur = con.cursor()

cur.execute("select count(*) from emp where deptno = :bv", (10,))
count, = cur.fetchone()
print("Number of rows:", count)
