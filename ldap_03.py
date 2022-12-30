
import ldap

server = "ldap://192.168.122.150"
who = "cn=Manager,dc=mydomain,dc=com"
cred = "lu48cie"
keyword = "es033022"


def main():

    def my_search(lconnect1, keyword1):
        base = "ou=cmoechcre,o=espagne,dc=mydomain,dc=com"
        # base = "dc=mydomain,dc=com"
        scope = ldap.SCOPE_SUBTREE
        # filter = "uid=" + "*" + keyword + "*"
        filter1 = "uid=" + keyword1
        # retrieve_attributes = ['cn','mail','telephonenumber','description']
        retrieve_attributes = []
        count = 0
        result_set = []
        timeout = 0
        
        try:
            result_id = lconnect1.search(base, scope, filter1, retrieve_attributes)
            result_type, result_data = lconnect.result(result_id, timeout)
            if not result_data:
                print("result_data is empty")
            else:
                if result_type == ldap.RES_SEARCH_ENTRY:
                    result_set.append(result_data)
            if len(result_set) <= 0:
                print("No result")
                return
            else:
                print("------------- QUERY RESULT -------------")
                for i in range(len(result_set)):
                    for entry in result_set[i]:
                        try:
                            name = entry[1]['uid'][0].decode("utf-8") 
                            email = entry[1]['mail'][0].decode("utf-8") 
                            phone = entry[1]['telephoneNumber'][0].decode("utf-8") 
                            desc = entry[1]['description'][0].decode("utf-8") 
                            count = count + 1
                            print("Record : %d\nUID: %s\nDescription: %s\nE-mail: %s\nPhone: %s\n" 
                                  % (count, name, desc, email, phone))
                        except KeyError as error1:
                            print("Key error : ", error1)
                print("-------------- END RESULT --------------")
        except ldap.LDAPError as error:
            print("Error", error)
                
    try:
        lconnect = ldap.initialize(server)
        lconnect.simple_bind_s(who, cred)
        print("successfully bound to the server")
        print("Searching....")
        my_search(lconnect, keyword)
    except ldap.LDAPError as err:
        print("Couldn not connect to the server %s :" % err)


if __name__ == '__main__':
    main()
