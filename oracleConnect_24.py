import cx_Oracle
import configOracleEnc as Config


cree_par = "VTB42315"
statut = "execute"

sql = """SELECT CREE_PAR, DATE_PAIEMENT, MONTANT, STATUT
         FROM PAIEMENTS
         WHERE cree_par = :mid AND statut = :fn"""

connection = ''
cursor = ''

try:
    connection = cx_Oracle.connect(user=Config.username, password=Config.passw, dsn=Config.dsn, mode=Config.mode)

except cx_Oracle.DatabaseError as er:
    print("Connexion on database DBHA001 failed : ", er)
else:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, mid=cree_par, fn=statut)

        for error in cursor.getbatcherrors():
            print("Error", error.message, "at row offset", error.offset)

        connection.commit()

        print("-" * 49)
        print("| %-10s| %-10s| %-10s| %-10s|" % ("NAME", "DATE", "PRICE", "STATUS"))
        print("-" * 49)
        # Loop over the result set
        for name, date, price, status in cursor:
            print("| %-10s| %-10s| %-10s| %-10s|" % (name, date, price, status))
        print("-" * 49)

        print("Records updated successfully")

    except cx_Oracle.DatabaseError as eq:
        print("Query on database DBHA001 failed : ", eq)

    except Exception as ex:
        print('Exception Error:', ex)

    finally:
        if cursor:
            cursor.close()
finally:
    if connection:
        connection.close()
