
import ldap


lconnect = ldap.initialize("ldap://192.168.122.150")

try:
    lconnect.protocol_version = ldap.VERSION3
    lconnect.set_option(ldap.OPT_REFERRALS, 0)
 
    bind = lconnect.simple_bind_s("uid=es033011,ou=cmochcrm,o=espagne,dc=mydomain,dc=com", "lu48cie")
 
    base = 'dc=mydomain,dc=com'
    criteria = "mail=es033011@mydomain.com"
    attributes = ['uid', 'cn']
    result = lconnect.search_s(base, ldap.SCOPE_SUBTREE, criteria, attributes)
 
    results = [entry for dn, entry in result if isinstance(entry, dict)]
    print(*results[0]['uid'], *results[0]['cn'])
    print(result)
finally:
    lconnect.unbind()
