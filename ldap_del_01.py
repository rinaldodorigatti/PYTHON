
import ldap


ldap_host = "ldap://192.168.122.150"
ldappass = "lu48cie"
ldap_bind = "cn=Manager,dc=mydomain,dc=com"
deleteDN = "uid=es344344,ou=zosteam,o=espagne,dc=mydomain,dc=com"


print("---------- Start Delete ------------")
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

ask = input("Are you sure to want to delete user [yes/no] : ")
if ask == "yes":
    try:
        ldap_conn.delete_s(deleteDN)
    except ldap.LDAPError as e:
        print("Ldap error : ", e)
        exit(5)
    finally:
        print("LDAP user delete successfully")
else:
    print("Youre choice is to quit")
    exit(0)

print("------------ End modify --------------")