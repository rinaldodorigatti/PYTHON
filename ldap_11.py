
from ldap3 import Server, Connection, ALL, SUBTREE, ALL_ATTRIBUTES, MODIFY_REPLACE, MODIFY_DELETE
from ldap3.core.exceptions import LDAPException, LDAPBindError, LDAPExceptionError


class Ldap3Main:
    LDAP_BASE = 'ou=unixgrp,o=espagne,dc=mydomain,dc=com'
    LDAP_USER = 'cn=Manager,dc=mydomain,dc=com'
    LDAP_PASS = 'lu48cie'
    # LDAP_SEARCH = '(cn={0}*)'
    OBJECT_CLASS = ['inetOrgPerson']
    LDAP_HOST = '192.168.122.150'

    def __init__(self):
        self.date = ''

    @staticmethod
    def ldap_server():
        server = ''
        try:
            server = Server(Ldap3Main.LDAP_HOST, get_info=ALL)
        except LDAPBindError as err:
            print("Error to bind server", err)
        return server

    def ldap_connexion(self):
        server = self.ldap_server()
        conn = Connection(server, user=Ldap3Main.LDAP_USER, password=Ldap3Main.LDAP_PASS)
        return conn

    @staticmethod
    def get_dn(getuser):
        user = 'cn={0},ou=unixgrp,o=espagne,dc=mydomain,dc=com'.format(getuser)
        return user

    @staticmethod
    def get_attributes(user, dep, givenname, car, cn, mail, mobile, uid, preferred, phone, sn):
        attrs = {
            'displayName': user,
            'departmentNumber': dep,
            'givenName': givenname,
            'carLicense': car,
            'cn': cn,
            'mail': mail,
            'mobile': mobile,
            'uid': uid,
            'preferredLanguage': preferred,
            'telephoneNumber': phone,
            'sn': sn
        }
        return attrs

    def find_ad_user(self, user4):
        with self.ldap_connexion() as c:
            LDAP_SEARCH = '(cn={0})'.format(user4)
            c.search(search_base=Ldap3Main.LDAP_BASE, search_filter=LDAP_SEARCH,
                     search_scope=SUBTREE, attributes=ALL_ATTRIBUTES, get_operational_attributes=True)

            j_son = c.response_to_ldif()
            return j_son

    def add_ad_user(self, user, dep, givenname, car, cn, mail, mobile, uid, preferred, phone, sn):
        with self.ldap_connexion() as c:
            attr = self.get_attributes(user, dep, givenname, car, cn, mail, mobile, uid, preferred, phone, sn)

            user_dn = self.get_dn(user)
            result = c.add(dn=user_dn, object_class=Ldap3Main.OBJECT_CLASS, attributes=attr)

            if not result:
                msg1 = "The user {0} was not created due to {1}".format(user, c.result.get('description'))
                raise Exception(msg1)

            print("User {0} successfully added".format(user))

    def replace_ad_datas(self, user):
        with self.ldap_connexion() as c:
            user_dn = self.get_dn(user)
            ldap_filtre = '(cn={0})'.format(user)

            resultat = c.search(search_base=Ldap3Main.LDAP_BASE, search_filter=ldap_filtre,
                                search_scope=SUBTREE, attributes=ALL_ATTRIBUTES, get_operational_attributes=False)
            if resultat:
                j_son = c.response_to_ldif()
                print(j_son)

                response2 = str(input("Which attributes do you want to change ? : "))
                response_value = str(input("And the value ? : "))

                try:
                    responseGiven = {response2: (MODIFY_REPLACE, [response_value])}
                    c.modify(user_dn, changes=responseGiven)
                    print("User {0} successfully modified with parms {1} and value {2}".format(
                        user, response2, response_value))

                except LDAPExceptionError as lerr:
                    print("Error exception error : ", lerr)

                except LDAPException as err:
                    print("Error exception : ", err)

                finally:
                    if c:
                        c.unbind()
                        print("Disconnected")
            else:
                print("User not found")

    def remove_attributes(self, user):
        with self.ldap_connexion() as c:
            user_dn = self.get_dn(user)
            ldap_filtre = '(cn={0})'.format(user)

            resultat2 = c.search(search_base=Ldap3Main.LDAP_BASE, search_filter=ldap_filtre,
                                 search_scope=SUBTREE, attributes=ALL_ATTRIBUTES, get_operational_attributes=False)

            if resultat2:
                j_son = c.response_to_ldif()
                print(j_son)

                response1 = str(input("Which attributes do you want to remove ? : "))
                response_value = str(input("Which value ? : "))

                try:
                    changeRemove = {response1: (MODIFY_DELETE, [response_value])}
                    c.modify(user_dn, changeRemove)
                    print("Attribute {0} for user {1} has been removed successfully with old value {2}".format(
                        response1, user, response_value))

                except LDAPExceptionError as lerr:
                    print("Error exception error : ", lerr)

                except LDAPException as err:
                    print("Error exception : ", err)

                finally:
                    if c:
                        c.unbind()
            else:
                print("User not found")

    @staticmethod
    def print_menu():
        msg2 = """
        ---------------- LDAP MENU --------------
        -----------------------------------------
         1) Find a user in LDAP
         2) Add a user in LDAP
         3) Replace attributes in LDAP
         4) Remove attributes in LDAP
         5) Quit
        """
        print(msg2)

    @staticmethod
    def get_infos_user():
        datas = []
        user5 = str(input("User ? : "))
        dep5 = str(input("Dep ? : "))
        givenname5 = str(input("Given ? : "))
        car5 = str(input("Car ? : "))
        cn5 = str(input("CN ? : "))
        mail5 = str(input("Mail ? : "))
        mobile5 = str(input("Mobile ? : "))
        uid5 = str(input("Uid ? : "))
        preferred5 = str(input("Language ? : "))
        phone5 = str(input("Phone ? : "))
        sn5 = str(input("SN ? : "))
        datas.append(user5)
        datas.append(dep5)
        datas.append(givenname5)
        datas.append(car5)
        datas.append(cn5)
        datas.append(mail5)
        datas.append(mobile5)
        datas.append(uid5)
        datas.append(preferred5)
        datas.append(phone5)
        datas.append(sn5)
        return datas

    def get_options(self, number):
        if number == 1:
            utilisateur3 = str(input("Give me the user : "))
            showUser = self.find_ad_user(utilisateur3)
            if showUser:
                print(showUser)
            else:
                print("User {0} not found".format(utilisateur3))
        elif number == 2:
            donnee = self.get_infos_user()
            self.add_ad_user(donnee[0], donnee[1], donnee[2], donnee[3], donnee[4],
                             donnee[5], donnee[6], donnee[7], donnee[8], donnee[9], donnee[10])
        elif number == 3:
            utilisateur = str(input("Give me the user : "))
            self.replace_ad_datas(utilisateur)
        elif number == 4:
            utilisateur2 = str(input("Give me the user : "))
            self.remove_attributes(utilisateur2)
        else:
            print("Wrong choice --- quit")
            exit(1)


ldap1 = Ldap3Main()
ldap1.print_menu()
response = int(input("Please give me your choice ? : "))
ldap1.get_options(response)
