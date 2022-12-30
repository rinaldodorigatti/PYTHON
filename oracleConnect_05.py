import cx_Oracle
import configOracle as co


# SCRIPT SIMPLE SELECT AS FETCHALL AND BIND VARIABLES


print("-" * 76)
print("| ", "{:<10}".format("ID"), " | ", "{:<10}".format("DATE"), " | ", "{:<10}".format("DATE EXEC"),
    " | ", "{:<10}".format("MONTANT"), " | ", "{:<10}".format("MONAY"), " |")
print("-" * 76)

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
        sql = 'SELECT ID,SAISIE,DATE_PAIEMENT,MONTANT,MONNEY FROM PAIEMENTS WHERE MONTANT > :mont ORDER BY MONTANT'
        cur.execute(sql, {'mont': 1000})
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print("| ", "{:<10}".format(row[0]), " | ", "{:<10}".format(row[1]), " | ",
                "{:<10}".format(row[2]), " | ", "{:<10}".format(row[3]), " | ", "{:<10}".format(row[4]), " |")
        print("-" * 76)
        version = con.version[:4]
        print("Oracle Version : ", version)
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
print("-" * 76)
