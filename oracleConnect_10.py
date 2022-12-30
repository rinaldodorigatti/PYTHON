import cx_Oracle

# SCRIPT SIMPLE SELECT AS FETCHONE, WITH CLASS


class MyConnection(cx_Oracle.Connection):

    def __init__(self, user1: str = "rickyd", passw1: str = 'lu48cie', dsn1: str = '192.168.122.205:1521/DBHA001'):
        super(MyConnection, self).__init__()
        print("Connecting to the database")
        self.user1 = user1
        self.passw1 = passw1
        self.dsn1 = dsn1

        connection = cx_Oracle.connect(user=self.user1, password=self.passw1, dsn=self.dsn1)
        print("Connecting to database")

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

cur.execute("SELECT COUNT(*) FROM python WHERE id = :bv", (10,))
count, = cur.fetchone()
print("Number of rows:", count)
