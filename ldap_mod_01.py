import ldap
import ldap.modlist as modlist

ldap_host = "ldap://192.168.122.150"
ldappass = "lu48cie"
ldap_bind = "cn=Manager,dc=mydomain,dc=com"
dn = "uid=es033022,ou=cmoechcre,o=espagne,dc=mydomain,dc=com"
old_text = b"C''est un user lenart"
new_text = b"Utilisateur du groupe cmoechcre"
old = {"description":[old_text]}
new = {"description":[new_text]}

print("---------- Start modify ------------")
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
    ldif = modlist.modifyModlist(old, new)
    ldap_conn.modify_s(dn, ldif)
except TypeError as terr:
    print("Type Err : ", terr)

ldap_conn.unbind_s()

print("DN : ", dn, " modifications")
print("Old : ", old_text.decode('UTF-8'))
print("New : ", new_text.decode('UTF-8'))
print("Successfully done")
print("------------ End modify --------------")