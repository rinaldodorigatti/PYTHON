
from ldap3 import Server, Connection, ALL_ATTRIBUTES, SUBTREE, MODIFY_REPLACE, ALL, MODIFY_DELETE
from ldap3.core.exceptions import LDAPException, LDAPExceptionError


def main():

    LDAP_BASE = 'ou=unixgrp,o=espagne,dc=mydomain,dc=com'
    LDAP_USER = 'cn=Manager,dc=mydomain,dc=com'
    LDAP_PASS = 'lu48cie'
    LDAP_SEARCH = '(cn={0}*)'
    OBJECT_CLASS = ['inetOrgPerson']
    LDAP_HOST = '192.168.122.150'

    def ldap_server():
        server = Server(LDAP_HOST, get_info=ALL)
        return server

    def ldap_connection():
        server = ldap_server()
        connection = Connection(server, user=LDAP_USER, password=LDAP_PASS)
        connection.bind()
        return connection

    def get_dn(username1):
        user = 'cn={0},ou=unixgrp,o=espagne,dc=mydomain,dc=com'.format(username1)
        return user

    def get_attributes(username1, dep1, forename1, car1, cn1, mail1, mobile1, uid1, preferred1, phone1, sn1):
        attrs = {
            'displayName': username1,
            'givenName': forename1,
            'carLicense': car1,
            'cn': cn1,
            'mail': mail1,
            'mobile': mobile1,
            'uid': uid1,
            'preferredLanguage': preferred1,
            'telephoneNumber': phone1,
            'departmentNumber': dep1,
            'sn': sn1
        }
        return attrs

    def find_ad_users(username1):
        with ldap_connection() as c:
            c.search(search_base=LDAP_BASE, search_filter=LDAP_SEARCH.format(username1), search_scope=SUBTREE,
                     attributes=ALL_ATTRIBUTES, get_operational_attributes=True)
            json_l = c.response_to_json()
            return json_l

    def create_ad_user(username1, dep1, forename1, car1, cn1, mail1, mobile1, uid1, preferred1, phone1, sn1):
        with ldap_connection() as c:
            attributes1 = get_attributes(username1, dep1, forename1, car1, cn1, mail1,
                                         mobile1, uid1, preferred1, phone1, sn1)
            user_dn = get_dn(username1)
            result = c.add(dn=user_dn, object_class=OBJECT_CLASS, attributes=attributes1)

            if not result:
                msg = "Error user {0} was not created {1}".format(username1, c.result.get("description"))
                raise Exception(msg)

            print("User {0} successfully added".format(username1))
            try:
                employeeN = {'employeeNumber': (MODIFY_REPLACE, ['030303'])}
                employeeT = {'employeeType': (MODIFY_REPLACE, ['Utilisateur lambda'])}
                c.modify(user_dn, changes=employeeN)
                c.modify(user_dn, changes=employeeT)
                print("User {0} successfully modified".format(username1))
            except LDAPExceptionError as lerr:
                print("Error Exception error : ", lerr)
            except LDAPException as lexc:
                print("Error Exception : ", lexc)
            finally:
                if c:
                    c.unbind()

    def insert_ad_datas():
        username = str(input("Username ? : "))
        dep = str(input("Department Number ? : "))
        forename = str(input("Given Name ? : "))
        car = str(input("Car ? : "))
        cn = str(input("cn ? : "))
        mail = str(input("Mail ? : "))
        mobile = str(input("Mobile ? : "))
        uid = str(input("Uid ? : "))
        preferred = str(input("Language ? : "))
        phone = str(input("Phone ? : "))
        sn = str(input("SN ? : "))
        create_ad_user(username, dep, forename, car, cn, mail, mobile, uid, preferred, phone, sn)

    print(find_ad_users('ux222222'))
    insert_ad_datas()


if __name__ == '__main__':
    main()
