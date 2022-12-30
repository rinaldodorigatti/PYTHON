import cx_Oracle
import configOracle as co


# SCRIPT SIMPLE UPDATE, BIND VARIABLES


try:
    con = cx_Oracle.connect(
        co.username,
        co.passw,
        co.dsn,
        encoding=co.encoding,
        mode=cx_Oracle.SYSDBA)

except cx_Oracle.DatabaseError as er:
    print("Connexion on database DBHA001 failed : ", er)
else:
    try:
        cur = con.cursor()
        str_version = str(input("Input version : "))
        int_id = int(input("Input ID : "))
        statement = "UPDATE python SET version = :v WHERE id = :n"
        cur.execute(statement, {'v': str_version, 'n': int_id})

        for error in cur.getbatcherrors():
            print("Error", error.message, "at row offset", error.offset)

        con.commit()

        print("Records updated successfully")

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
