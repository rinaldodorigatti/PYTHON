
from ldap3 import Server, Connection, ALL

server = Server('192.168.122.150', get_info=ALL)
conn = Connection(server, 'cn=Manager,dc=mydomain,dc=com', 'lu48cie', auto_bind=True)
sinfo = server.info
sschema = server.schema
cconn = conn.extend.standard.who_am_i()

dep = 'departmentNumber'
depval = 'DEV'

cmp = conn.compare('cn=es111111,ou=ubpteam,o=espagne,dc=mydomain,dc=com', dep, depval)
if cmp:
    print("Departement Number = 000333")
else:
    print("Departement Number != 000333")

groupse = conn.search('o=espagne,dc=mydomain,dc=com', '(ou=ubpteam)',
                      attributes=['ou', 'objectClass'])

uidse = conn.search('ou=ubpteam,o=espagne,dc=mydomain,dc=com', '(uid=es111111)',
                    attributes=['uid', 'sn', 'displayName', 'mobile'])

try:
    if groupse:
        print("Group found not added")
    else:
        conn.add('ou=ubpteam,o=espagne,dc=mydomain,dc=com', 'organizationalUnit')
except Exception as err:
    print("Error to add container", err)
else:
    try:
        if uidse:
            print("Record found not added")
        else:
            conn.add('cn=es111111,ou=ubpteam,o=espagne,dc=mydomain,dc=com', 'inetOrgPerson',
                     {
                         'givenName': 'Beatrix',
                         'sn': 'Young',
                         'departmentNumber': '000333',
                         'telephoneNumber': '+41 21 894 58 67',
                         'displayName': 'Beatrix Aline',
                         'employeeNumber': '243567',
                         'mail': 'aline.beatrix@gmail.com',
                         'mobile': '+41 79 480 99 88',
                         'uid': 'es111111',
                         'preferredLanguage': 'FR',
                         'carLicense': 'Yes',
                     })
    except Exception as errr:
        print("Error to add container", errr)
    else:
        if uidse:
            print("User not added because the user already exists")
        else:
            print("User added in the database")
finally:
    uidse = conn.search('ou=ubpteam,o=espagne,dc=mydomain,dc=com', '(uid=es111111)',
                        attributes=['uid', 'sn', 'displayName', 'mobile'])

    if groupse:
        print("OU not added because the group already exists")
    else:
        print("OU added in the database")

    if not uidse:
        print("Record not found")
        exit(1)
    else:
        centri = conn.entries[0]
        centriuid = centri.uid
        centrisn = centri.sn
        centridisplayname = centri.displayName
        centrimobile = centri.mobile
        users = {
            'UID': centriuid,
            'SN': centrisn,
            'DisplayName': centridisplayname,
            'Mobile': centrimobile
        }

        for k, v in users.items():
            print('Key : %-15s Value : %-15s' % (k, v))

# print(centri)
# print(sinfo)
# print(sschema)
# print(conn.entries[0].entry_to_ldif())
# print(entry.entry_to_json())
"""
searchParameters = { 
    'search_base': 'dc=demo1,dc=freeipa,dc=org',
    'search_filter': '(objectClass=Person)',
    'attributes': ['cn', 'givenName'],
    'paged_size': 5 }
    
    conn.search(**searchParameters)
    
    create container
    conn.add('ou=ubpteam,o=espagne,dc=mydomain,dc=com', 'organizationalUnit')
    
    create user
    conn.add('cn=es111111,ou=ubpteam,o=espagne,dc=mydomain,dc=com', 'inetOrgPerson',
        {'givenName': 'Beatrix', 'sn': 'Young', 'departmentNumber': 'DEV', 'telephoneNumber': 1111})
    
    Modify user
    conn.modify_dn('cn=es111111,ou=ubpteam,o=espagne,dc=mydomain,dc=com', 'cn=es222222')
    
    Move user
    conn.add('ou=moved, ou=ubpteam,o=espagne,dc=mydomain,dc=com', 'organizationalUnit')
    
    conn.modify_dn('cn=es111111,ou=ubpteam,o=espagne,dc=mydomain,dc=com', 'cn=es111111',
        new_superior='ou=moved, ou=ubpteam,o=espagne,dc=mydomain,dc=com')
        
    Change entry
    conn.modify('cn=es111111,ou=ubpteam,o=espagne,dc=mydomain,dc=com', {'sn': [(MODIFY_ADD, ['es333333'])]})
    
    Delete old entry
    conn.modify('cn=es111111,ou=ubpteam,o=espagne,dc=mydomain,dc=com', {'sn': [(MODIFY_DELETE, ['Young'])]})
    
    Combined query
    conn.modify('cn=es111111,ou=ubpteam,o=espagne,dc=mydomain,dc=com',
        {'sn': [(MODIFY_ADD, ['Young', 'Johnson']), (MODIFY_DELETE, ['Smith'])],
            'givenname': [(MODIFY_REPLACE, ['Mary', 'Jane'])]})
    
    Compare entry
    conn.compare('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'departmentNumber', 'DEV')
"""
