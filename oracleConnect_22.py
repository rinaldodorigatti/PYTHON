import cx_Oracle
import configOracle as Config

# SCRIPT SIMPLE SELECT AS FETCHONE, WITH CLASS


class MyConnection(cx_Oracle.Connection):

    def __init__(self):
        print("Connecting to database")
        # return super(MyConnection, self).__init__(co.username, co.passw, co.dsn)
        super(MyConnection, self).__init__(Config.username, Config.passw, Config.dsn)

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


con = ''
cur = ''

try:
    con = MyConnection()

except cx_Oracle.DatabaseError as er:
    print("Connexion on database DBHA001 failed : ", er)
else:
    try:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM python WHERE id = :bv", (8,))
        count, = cur.fetchone()
        print("Number of rows:", count)

        for error in cur.getbatcherrors():
            print("Error", error.message, "at row offset", error.offset)

        con.commit()

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
