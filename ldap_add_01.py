
import ldap
import ldap.modlist as modlist


def main():
    ldap_host = "ldap://192.168.122.150"
    ldappass = "lu48cie"
    ldap_bind = "cn=Manager,dc=mydomain,dc=com"
    dn = "uid=es555555,ou=zosteam,o=espagne,dc=mydomain,dc=com"

    attrs = {
        'objectclass': [b'top', b'person', b'organizationalPerson', b'inetOrgPerson'],
        'sn': b'Benoit',
        'cn': b'Strub Benoit',
        'userPassword': b'lu48cie',
        'description': b'User Strub Benoit',
        'businessCategory': b'167',
        'displayName': b'Strub Benoit',
        'employeeNumber': b'230230',
        'employeeType': b'EMP',
        'homePhone': b'031 435 65 67',
        'mobile': b'079 485 65 35',
        'uid': b'es555555',
        'preferredLanguage': b'FR'
    }


    print("---------- Start Add ------------")
    try:
        ldap_conn = ldap.initialize(ldap_host)
    except ldap.SERVER_DOWN:
        print("LDAP server is DOWN")
        exit(4)

    try:
        ldap_conn.simple_bind_s(ldap_bind, ldappass)
    except ldap.INVALID_CREDENTIALS as err:
        print("Invalid credentials", err)
        exit(1)

    try:
        ldif = modlist.addModlist(attrs)
        ldap_conn.add_s(dn, ldif)
    except TypeError as terr:
        print("Type Err : ", terr)

    ldap_conn.unbind_s()

    print("ADD Successfully done")
    print("------------ End modify --------------")


if __name__ == '__main__':
    main()
