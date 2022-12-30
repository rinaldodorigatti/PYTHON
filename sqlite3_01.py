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

    sql_insert_data = """ INSERT INTO projects (name,begin_date,end_date) 
    VALUES ('Project UBP 37', '01.08.2022', '02.08.2022'); """

    try:
        cur = conn.cursor()
        cur.execute(sql_insert_data)
        conn.commit()

    except Error as ex:
        print("Error : ", ex)
    else:
        # print(cur.lastrowid)
        cur2 = conn.cursor()
        cur2.execute("SELECT * FROM PROJECTS")
        allrecords = cur2.fetchall()
        for i in allrecords:
            print(i[0], i[1], i[2], i[3])
    finally:
        print("All OK")


def insert_project(conn):
    """Insert new project"""

    sql = """INSERT INTO projects (name,begin_date,end_date) VALUES (?, ?, ?)"""
    project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')

    try:
        cur3 = conn.cursor()
        cur3.execute(sql, project)
        conn.commit()
        print("Data inserted successfully")
    except Error as err:
        print("Error to insert values : ", err)
    finally:
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
            print("Old Record : ", row[0], "\t", row[1], "\t", row[2], "\t", row[3])


def update_record(conn):
    """Update record in database db.sqlite3"""

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
            print("Old Record : ", row[0], "\t", row[1], "\t", row[2], "\t", row[3])

    if row is None:
        print("New record found, update not executed")
    else:
        sql = """UPDATE projects
        SET name = ?,
        begin_date = ?,
        end_date = ?
        WHERE id = ?"""
        update = ('C++ project terminé', '10.10.2018', '10.09.2022', record_num)

        try:
            cur4 = conn.cursor()
            cur4.execute(sql, update)
            conn.commit()
            print("Data updated")
        except Error as err:
            print("Error to update record :", err)
        finally:
            get_record(conn, record_num)
            if conn:
                conn.close()


def delete_row(conn):
    """Delete one row method"""

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
    # insert_datas(conn)
    # insert_project(conn)
    # update_record(conn)
    delete_row(conn)


if __name__ == '__main__':
    main()
