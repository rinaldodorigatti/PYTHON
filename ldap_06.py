from ldap3 import Server, Connection, ObjectDef, AttrDef, Reader, Writer, ALL

server = Server('192.168.122.150', get_info=ALL)
conn = Connection(server, 'cn=Manager,dc=mydomain,dc=com', 'lu48cie')
conn.bind()
sinfo = server.info
sschema = server.schema
cconn = conn.extend.standard.who_am_i()

dep = 'departmentNumber'
depval = '000333'

cmp = conn.compare('cn=es111111,ou=ubpteam,o=espagne,dc=mydomain,dc=com', dep, depval)
if cmp:
    print("Departement Number = 000333")
else:
    print("Departement Number != 000333")

obj_inetorgperson = ObjectDef('inetOrgPerson', conn)
r = Reader(conn, obj_inetorgperson, 'cn=es111111,ou=ubpteam,o=espagne,dc=mydomain,dc=com')
print("--------------------- r --------------------")
print(r)
print("-------------- r.search() ------------------")
testr = r.search()
if not testr:
    print("Pas d'enregistrement")
else:
    print(testr)

print("Entry DN  :", testr[0].entry_dn)
print("Entry UID :", testr[0].uid)
print("Mobile    :", testr[0].mobile)
print("Name      :", testr[0].displayName)
print("Mail      :", testr[0].mail)
print("--------- PRINT AS LDIF -----------")
print(r[0].entry_to_ldif())

objinetorgperson = ObjectDef('inetOrgPerson', conn)
v = Reader(conn, objinetorgperson, 'ou=ubpteam,o=espagne,dc=mydomain,dc=com', 'uid:=es111111')

print(v)
testv = v.search()
print("UID :", testv[0].uid)

v.search()
w = Writer.from_cursor(v)
w[0].employeeType = 'Type employé 4'
# w[0].employeeType += ['Smith', 'Johnson']     to add multiple values
# w[0].employeeType = 'Type employé 4'    to add new emplyeeType entry
w.commit()

# r[0].entry_attributes
# r[0].entry_attributes_as_dict
# r[0].entry_mandatory_attributes
# r[0].entry_to_json(include_empty=False)
