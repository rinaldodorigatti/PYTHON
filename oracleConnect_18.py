import cx_Oracle
import configOracleSys as Config

# Establish the database connection
connection = cx_Oracle.connect(user=Config.username, password=Config.passw, dsn=Config.dsn, mode=Config.mode)

# Obtain a cursor
cursor = connection.cursor()

# Data for binding
cree_par = "VTB42315"
statut = "execute"

# Execute the query
sql = """SELECT CREE_PAR, DATE_PAIEMENT, MONTANT, STATUT
         FROM PAIEMENTS
         WHERE cree_par = :mid AND statut = :fn"""

cursor.execute(sql, mid=cree_par, fn=statut)

print("-" * 49)
print("| %-10s| %-10s| %-10s| %-10s|" % ("NAME", "DATE", "PRICE", "STATUS"))
print("-" * 49)
# Loop over the result set
for name, date, price, status in cursor:
    print("| %-10s| %-10s| %-10s| %-10s|" % (name, date, price, status))
print("-" * 49)
