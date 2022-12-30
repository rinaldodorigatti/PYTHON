import sqlite3
from sqlite3 import Error


def createconnexion(db_file):
    """Create a database connexion on sqlit3"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as err:
        print("Error occured : ", err)
    finally:
        if conn:
            conn.close()


def createconnexion2(db_file):
    """Create a database connexion on sqlit3"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as err:
        print("Error occured : ", err)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_datas(conn):
    """Insert datas in project table"""

    print("------------------------------ INSERT DATA ------------------------------")

    name = str(input("Project name : "))
    start_date = str(input("Start date : "))
    end_date = str(input("End date : "))

    sql_insert_data = """ INSERT INTO projects (name,begin_date,end_date) 
        VALUES (?, ?, ?); """

    try:
        cur = conn.cursor()
        cur.execute(sql_insert_data, (name, start_date, end_date,))
        conn.commit()

    except Error as ex:
        print("Error : ", ex)
    else:
        # print(cur.lastrowid)
        cur2 = conn.cursor()
        cur2.execute("SELECT * FROM PROJECTS")
        allrecords = cur2.fetchall()
        print("")
        print(("-" * 28) + " Records list " + ("-" * 27))
        for i in allrecords:
            print("| %-5s| %-25s| %-15s| %-15s|" % (i[0], i[1], i[2], i[3]))
        print(("-" * 28) + " Records list " + ("-" * 27))
        print("")
    finally:
        print("-------------------------------- END DATA -------------------------------")


def insert_project(conn):
    """Insert new project"""

    print("--------------------- INSERT PROJECT ---------------------")

    name = str(input("Project name : "))
    start_date = str(input("Start date : "))
    end_date = str(input("End date : "))

    sql = """INSERT INTO projects (name,begin_date,end_date) VALUES (?, ?, ?)"""
    project = (name, start_date, end_date)

    try:
        cur3 = conn.cursor()
        cur3.execute(sql, project)
        conn.commit()
        print("Data inserted successfully")
    except Error as err:
        print("Error to insert values : ", err)
    finally:
        print("----------------------- END PROJECT ----------------------")
        if conn:
            conn.close()


def get_record(conn, record_num):
    """Get record after update"""

    sql_check = """SELECT id, name, begin_date, end_date FROM projects WHERE id = ?"""
    cur6 = ''

    try:
        cur6 = conn.cursor()
        cur6.execute(sql_check, (record_num,))
        conn.commit()
    except Error as error:
        print("Error to find record :", error)
    except ValueError as verr:
        print("Value error :", verr)
    finally:
        row = cur6.fetchone()
        if row is None:
            print("No record found with number : ", record_num)
        else:
            print(("-" * 28) + " New Record " + ("-" * 29))
            print("| %-5s| %-25s| %-15s| %-15s|" % (row[0], row[1], row[2], row[3]))
            print("-" * 69)


def update_record(conn):
    """Update record in database db.sqlite3"""

    print("---------------------------- UPDATE RECORD ----------------------------")

    record_num = int(input("Please give the record number : "))
    sql_check = """SELECT id, name, begin_date, end_date FROM projects WHERE id = ?"""
    cur5 = ''

    try:
        cur5 = conn.cursor()
        cur5.execute(sql_check, (record_num,))
        conn.commit()
    except Error as error:
        print("Error to find record :", error)
    except ValueError as verr:
        print("Value error :", verr)
    finally:
        row = cur5.fetchone()
        if row is None:
            print("Record not found with number :", record_num)
        else:
            print(("-" * 28) + " Old Record " + ("-" * 29))
            print("| %-5s| %-25s| %-15s| %-15s|" % (row[0], row[1], row[2], row[3]))
            print("-" * 69)

    if row is None:
        print("New record found, update not executed")
    else:
        start_date = str(input("Start date : "))
        end_date = str(input("End date : "))

        sql = """UPDATE projects
        SET begin_date = ?,
        end_date = ?
        WHERE id = ?"""
        update = (start_date, end_date, record_num)

        try:
            cur4 = conn.cursor()
            cur4.execute(sql, update)
            conn.commit()
            print("Data updated")
        except Error as err:
            print("Error to update record :", err)
        finally:
            get_record(conn, record_num)
            print("------------------------------- END RECORD -----------------------------")
            if conn:
                conn.close()


def delete_row(conn):
    """Delete one row method"""

    print("--------------------- DELETE PROJECT ---------------------")

    id_num = int(input("Give me the record id : "))
    sql_select = """SELECT id FROM projects WHERE id = ?"""
    sql_del = """DELETE FROM projects WHERE id = ?"""

    cur7 = ''

    try:
        cur7 = conn.cursor()
        cur7.execute(sql_select, (id_num,))
        conn.commit()
        print("Selected record => ")
    except Error as err:
        print("Error select record not found", err)
    finally:
        row = cur7.fetchone()
        if row is None:
            print("Select failed not record found for id :", id_num)
        else:
            try:
                cur8 = conn.cursor()
                cur8.execute(sql_del, (id_num,))
                conn.commit()
                print("Record %s deleted !!!" % id_num)
            except Error as terr:
                print("Error to delete record %s :" % terr)
            except ValueError as verr:
                print("Value error during the delete :", verr)
            finally:
                print("----------------------- END DELETE----------------------- ")
                if conn:
                    conn.close()


def delete_all_row(conn):
    """Delete all row of table projects"""

    sql_remove = """DELETE FROM projects"""

    yesno = str(input("Are you sure to remove all data in projects (Y/N) ? : "))
    if yesno == 'N' or yesno == 'n':
        print("Your choice is NO")
        exit(1)
    else:
        try:
            cur9 = conn.cursor()
            cur9.execute(sql_remove)
            conn.commit()
            print("All records removed")
        except Error as aerr:
            print("Remove all record failed :", aerr)
        finally:
            print("All records removed !!! the table is empty !!!")
            if conn:
                conn.close()


def startproject(conn):
    """start project connexion"""
    sql_create_project = """ CREATE TABLE IF NOT EXISTS projects (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            begin_date text,
                                            end_date text
                                        ); """

    if conn is not None:
        create_table(conn, sql_create_project)
    else:
        table = "Projects"
        print("Error to create table :", table)


def main():
    database = r'FILES/db.sqlite3'
    conn = createconnexion2(database)
    startproject(conn)

    # MENU
    print("")
    print("|" + ("-" * 26) + " MENU " + ("-" * 26) + "|")
    print("|" + ("-" * 58) + "|")
    print("| 1) Insert datas" + (" " * 42) + "|")
    print("| 2) insert_project" + (" " * 40) + "|")
    print("| 3) update_record" + (" " * 41) + "|")
    print("| 4) delete_row" + (" " * 44) + "|")
    print("| 5) delete_all_row" + (" " * 40) + "|")
    print("| 6) Quit" + (" " * 50) + "|")
    print("|" + ("-" * 58) + "|")
    print("|", end='')
    choice = int(input(" Please give your choice : "))

    if choice == 1:
        insert_datas(conn)
    elif choice == 2:
        insert_project(conn)
    elif choice == 3:
        update_record(conn)
    elif choice == 4:
        delete_row(conn)
    elif choice == 5:
        delete_all_row(conn)
    elif choice == 6:
        exit(0)
    else:
        print("Choice not found, please try again")


if __name__ == '__main__':
    main()
