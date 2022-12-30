import cx_Oracle
import configOracle as config


# SCRIPT SIMPLE SELECT AS FETCHALL, BIND VARIABLES, FORMAT


def recherche_banque_par_lieu(lieu):

    sql = ('SELECT GROUPE,SIEGE,VALABLE,ADRESSE,NPA,LIEU,PHONE FROM BANKS WHERE LIEU LIKE :lieu_q')

    customer_name = None

    print("-" * 126)
    print("| ", "{:<10}".format("GROUP"),
    " | ", "{:<10}".format("SIEGE"),
    " | ", "{:<19}".format("VALABLE"),
    " | ", "{:<16}".format("ADRESSE"),
    " | ", "{:<10}".format("NPA"),
    " | ", "{:<10}".format("LIEU"),
    " | ", "{:<15}".format("PHONE"),
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
                cursor.execute(sql, lieu_q=lieu)
                rows = cursor.fetchall()
                if rows:
                    customer_name = rows[0]
                    for groupe,siege,valable,adresse,npa,lieu,phone in rows:
                        print("| ", "{:<10}".format(groupe),
                        " | ", "{:<10}".format(siege),
                        " | ", "{:<10}".format(str(valable)),
                        " | ", "{:<16}".format(str(adresse)),
                        " | ", "{:<10}".format(npa),
                        " | ", "{:<10}".format(lieu),
                        " | ", "{:<10}".format(phone),
                        " |")
                print("-" * 126)
                version = connection.version[:4]
                print("|" + "-" * 10, "Oracle Version : ", version, "-" * 90 + "|")
    except cx_Oracle.Error as error:
        print(error)

    return customer_name


recherche_banque_par_lieu('Vaduz')

print("-" * 126)
