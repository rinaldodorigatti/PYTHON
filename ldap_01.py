
import ldap
import sys


def try_ldap_connect(ldap_host, ldap_pass):
    try:
        ldap_conn = ldap.initialize(ldap_host)
    except ldap.SERVER_DOWN:
        print("LDAP server is DOWN")
        exit(4)

    ldap_conn = ''
    try:
        ldap_conn.simple_bind_s("cn=Manager,dc=mydomain,dc=com", ldap_pass)
    except ldap.INVALID_CREDENTIALS as err:
        print("Invalid credentials", err)
        sys.exit(3)
    print("Authentication successfully")
    
    result = ldap_conn.search_s('dc=mydomain,dc=com', ldap.SCOPE_SUBTREE, 'uid=es033011', ['uid'])
    print(result)
    print(result[0][0])
    print(result[0][1]['uid'][0])
    

host = "ldap://192.168.122.150"
ldappass = "lu48cie"
try_ldap_connect(host, ldappass)

