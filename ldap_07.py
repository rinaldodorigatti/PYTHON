from ldap3 import Server, Connection, ObjectDef, AttrDef, Reader, Writer, ALL
import ldap3
from ldap3.core.exceptions import LDAPBindError, LDAPInvalidCredentialsResult


LDAP_SERVER = "192.168.122.150"
LDAP_USER = "cn=Manager,dc=mydomain,dc=com"
LDAP_PASSWORD = "lu48cie"
LDAP_FILTER = "(uid=es033066)"
LDAP_ATTRS = ["cn", "uid", "sn", "givenName", "carLicense", "employeeType", "postalCode", "postalAddress"]
LDAP_BASE = "ou=networkteam,o=espagne,dc=mydomain,dc=com"


def main():
    server = Server(LDAP_SERVER, get_info=ALL)

    try:
        conn = Connection(server, LDAP_USER, LDAP_PASSWORD, raise_exceptions=True)
        conn.bind()
        print('LDAP Bind Successful.')
        conn.search(LDAP_BASE, LDAP_FILTER, attributes=LDAP_ATTRS)

        for entry in conn.entries:
            print("UID             : %-20s" % entry.uid)
            print("Canonical Name  : %-20s" % entry.cn)
            print("S Name          : %-20s" % entry.sn)
            print("Given Name      : %-20s" % entry.givenName)
            print("Car License     : %-20s" % entry.carLicense)
            print("Empl Type       : %-20s" % entry.employeeType)
            print("Postal Code     : %-20s" % entry.postalCode)
            print("Postal Address  : %-20s" % entry.postalAddress)

    except LDAPBindError as e:
        print('LDAP Bind Failed: ', e)

    except LDAPInvalidCredentialsResult as r:
        print('LDAP Bind Failed: ', r)
    finally:
        conn.unbind()

    def autreserver():

        LDAP_BASE1 = 'ou=ubpteam,o=espagne,dc=mydomain,dc=com'
        server1 = Server(LDAP_SERVER, get_info=ALL)
        conn1 = Connection(server1, LDAP_USER, LDAP_PASSWORD, raise_exceptions=True)
        conn1.bind()

        cn = str(input("Donner-moi le CN de l'utilisateur : "))
        QUERY = "(uid=" + cn + ")"

        existOrNot = conn1.search(LDAP_BASE1, QUERY, attributes=LDAP_ATTRS)

        if existOrNot:
            phone = str(input("Donner le nouveau numéro mobile : "))

            objinetorgperson1 = ObjectDef('inetOrgPerson', conn1)
            a = Reader(conn1, objinetorgperson1, 'ou=ubpteam,o=espagne,dc=mydomain,dc=com', 'cn=' + cn)
            a.search()
            wtt = Writer.from_cursor(a)
            wtt[0].mobile = phone
            wtt.commit()
            conn1.unbind()
            print("Record updated successfuly")
        else:
            print("The record not found")
    autreserver()


if __name__ == '__main__':
    main()
