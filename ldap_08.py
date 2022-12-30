import ldap
from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError
import ldap.modlist as modlist


def main():
    def connect_ldap_server():
        connection = ''
        try:
            server_ldap = "192.168.122.150"
            server = Server(server_ldap, get_info=ALL)

            connection = Connection(server, user="cn=Manager,dc=mydomain,dc=com", password="lu48cie")
            connection.bind()

            bind_response = connection.bind()
        except LDAPBindError as berr:
            print("Errno from LDAP bind error : ", berr)

        return connection

    def get_ldap_users():
        search_base = 'ou=ubpteam,o=espagne,dc=mydomain,dc=com'
        search_filter = '(cn=es111111)'

        ldap_conn = connect_ldap_server()
        try:
            ldap_conn.search(search_base=search_base,
                             search_filter=search_filter,
                             attributes=['cn', 'sn', 'uid', 'mobile', 'objectClass'])
            results = ldap_conn.entries[0]
            cn = results.cn
            sn = results.sn
            uid = results.uid
            mobile = results.mobile
            cclass = results.objectClass

            users = {
                'CN': cn,
                'SN': sn,
                'UIO': uid,
                'Mobile': mobile,
                'Class': cclass
            }

            for k, v in users.items():
                print("Key : %-20s - Value : %-20s" % (k, v))

            ldap_to_ldif = ldap_conn.response_to_ldif()
            fldif = open('FILES/es111111.ldif', 'w')
            fldif.write(ldap_to_ldif)
            fldif.close()
            print("Datas recorded in the file es111111.ldif successfully")
            # print(ldap_to_ldif)

        except LDAPException as e:
            print("Errno LDAP Exception : ", e)

    def add_ldap_group():
        ldap_attrs = {
            'objectClass': ['top', 'organizationalUnit'],
            'description': 'Unix et Linux support'
        }

        ldap_conn = connect_ldap_server()

        groupse = ldap_conn.search('o=espagne,dc=mydomain,dc=com', '(ou=unixgrp)',
                                   attributes=['ou', 'objectClass'])

        if groupse:
            print("Error the group unixgrp exists")
        else:
            try:
                ldap_conn.add('ou=unixgrp,o=espagne,dc=mydomain,dc=com', attributes=ldap_attrs)
                print("Group unixgrp added successfuly")
            except LDAPException as lderr:
                print("Error ldap exception : ", lderr)

            ldap_conn.unbind()
            # return response

    def add_new_user_to_group():

        ldap_attr = {
            'givenName': 'Rinaldo',
            'sn': 'Rickyd',
            'departmentNumber': '000666',
            'telephoneNumber': '+41 21 625 92 51',
            'displayName': 'Rinaldo Dorigatti',
            'employeeNumber': '666666',
            'mail': 'rinaldo.dorigatti@gmail.com',
            'mobile': '+41 79 480 99 88',
            'uid': 'es666666',
            'preferredLanguage': 'FR',
            'carLicense': 'Yes',
        }

        ldap_conn = connect_ldap_server()

        userse = ldap_conn.search('ou=unixgrp,o=espagne,dc=mydomain,dc=com', '(uid=es666666)',
                                  attributes=['uid', 'displayName'])

        user_dn = "cn=es666666,ou=unixgrp,o=espagne,dc=mydomain,dc=com"

        if userse:
            print("Error User already exists not added")
        else:
            try:
                ldap_conn.add(dn=user_dn, object_class='inetOrgPerson', attributes=ldap_attr)
                print("User added successfully")
            except LDAPException as adde:
                print("Error LDAP add : ", adde)
            ldap_conn.unbind()

    def delete_user():

        print(" --- You are in progress to delete a user ---")
        yesNo = str(input("Are you sure ? (Yy/Nn) : "))
        if yesNo in ["N", "n"]:
            print("You decide to quit without remove the user")
        else:
            ldap_conn = connect_ldap_server()

            try:
                ldap_conn.delete(dn='cn=es666666,ou=unixgrp,o=espagne,dc=mydomain,dc=com')
            except LDAPException as dele:
                print("Error to delete user : ", dele)
            ldap_conn.unbind()

    def add_user_to_exisitng_group():
        ldap_attr = dict()
        ldap_attr['uid'] = b'ux222222'
        ldap_attr['cn'] = b'ux222222'
        ldap_attr['carLicense'] = b'No'
        ldap_attr['departmentNumber'] = b'111222'
        ldap_attr['displayName'] = b'Sara Dorigatti'
        ldap_attr['givenName'] = b'Sara'
        ldap_attr['mail'] = b'sara.dorigatti@gmail.com'
        ldap_attr['mobile'] = b'+41 78 890 76 79'
        ldap_attr['preferredLanguage'] = b'FR'
        ldap_attr['sn'] = b'La Ciolette'
        ldap_attr['telephoneNumber'] = b'+41 21 364 56 57'
        ldap_attr['objectClass'] = [b'top', b'inetOrgPerson']

        conn = ldap.initialize('ldap://192.168.122.150', bytes_mode=False)
        conn.simple_bind_s('cn=Manager,dc=mydomain,dc=com', 'lu48cie')
        dn_new = 'cn=ux222222,ou=unixgrp,o=espagne,dc=mydomain,dc=com'
        ldif = modlist.addModlist(ldap_attr)
        try:
            # conn.add_s(dn_new, ldif)
            print("User ux222222 added successfully")
            response = conn.add_s(dn_new, ldif)
        except ldap.LDAPError as ldaperr:
            print("Error ldap :", ldaperr)
        finally:
            conn.unbind()
        return response

    get_ldap_users()
    # add_ldap_group()
    # add_new_user_to_group()
    # delete_user()
    # res = add_user_to_exisitng_group()
    # print(res)


if __name__ == '__main__':
    main()
