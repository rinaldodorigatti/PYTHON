from flask import request, session, Response
from ldap3 import Server, Connection, SIMPLE, SYNC, ALL
from ldap3.core.exceptions import LDAPException, LDAPBindError, LDAPExceptionError
from functools import wraps
import logging

auth_logger = logging.getLogger('verbose')


def ldap_authenticate(request, username, password, groups_allowed=True):
    id_name = "uid"
    ldap_host = "192.168.122.150"
    ldap_port = "389"
    bind_dn = "cn=Manager,dc=mydomain,dc=com"
    bind_pass = "lu48cie"
    user_base = "ou=unixgrp,o=espagne,dc=mydomain,dc=com"

    s = Server(ldap_host, port=int(ldap_port), get_info=ALL)
    c = Connection(
        s,
        authentication=SIMPLE,
        user=bind_dn,
        password=bind_pass,
        check_names=True,
        lazy=False,
        client_strategy=SYNC,
        raise_exceptions=False)
    c.open()
    c.bind()
    if c.bound:
        c.search(user_base, '(%s=%s)' % (id_name, username), attributes=['cn', 'mail'])
        c.unbind()
        try:
            cn_name = c.entries[0].cn
            cn_mail = c.entries[0].mail
            print("CN : ", cn_name)
            print("ML : ", cn_mail)
        except LDAPException as lerr:
            print("user cn cannot be found", lerr)
            auth_logger.error("user cn cannot be found")

        session['username'] = username
        return True
    else:
        auth_logger.debug('ldap bind failed')
        c.unbind()
        return False


def ldap_authenticate_01(username):
    id_name = "uid"
    ldap_host = "192.168.122.150"
    ldap_port = "389"
    bind_dn = "cn=Manager,dc=mydomain,dc=com"
    bind_pass = "lu48cie"
    user_base = "ou=unixgrp,o=espagne,dc=mydomain,dc=com"

    s = Server(ldap_host, port=int(ldap_port), get_info=ALL)
    try:
        c = Connection(
            s,
            authentication=SIMPLE,
            user=bind_dn,
            password=bind_pass,
            check_names=True,
            lazy=False,
            client_strategy=SYNC,
            raise_exceptions=False)
        c.open()
        c.bind()
    except LDAPBindError as berr:
        print("Error to bind server : ", berr)
    else:
        if c.bound:
            c.search(user_base, '(%s=%s)' % (id_name, username),
                     attributes=['uid', 'cn', 'mail', 'carLicense', 'displayName', 'mobile', 'departmentNumber'])
            try:
                cn_all = c.entries[0]
                cn_uid = cn_all.uid
                cn_cn = cn_all.cn
                cn_mail = cn_all.mail
                cn_car = cn_all.carLicense
                cn_dname = cn_all.displayName
                cn_mobile = cn_all.mobile
                cn_dep = cn_all.departmentNumber

                if cn_car[0] == 'No':
                    cn_car = 'Oui j''ai une voiture'

                if cn_mail[0].startswith('sara.dorigatti@gmail.com'):
                    cn_mail = 'lucca' + '.dorigatti@gmail.com'

                if cn_dep[0] == '111222':
                    cn_dep = 'Departement : 689'

                user = {
                    'UID': cn_uid,
                    'CN': cn_cn,
                    'MAIL': cn_mail,
                    'CAR': cn_car,
                    'NAME': cn_dname,
                    'MOBILE': cn_mobile,
                    'DEP': cn_dep
                }
                print("")
                print("--------------------------- User ---------------------------")
                for k, v in user.items():
                    print("%-15s %-15s" % (k, v))
                print("------------------------------------------------------------")

            except LDAPException as lerr:
                print("user cn cannot be found", lerr)
                auth_logger.error("user cn cannot be found")

            return True
        else:
            auth_logger.debug('ldap bind failed')
            c.unbind()
            return False


def auth_401():
    return Response('You have to login with proper credentials', 401,
                    {'WWW-Authenticate': 'Basic realm="Input ldap USER and PASSWORD"'})


def ldap_protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # this can be configured and taken from elsewhere
        # path, method, groups_allowed (users in Allowed Users group will be allowed to access / with a GET method)
        authorization_config = {
            "/": {
                "GET": ["Allowed Users"]
            }
        }

        auth_endpoint_rule = authorization_config.get(request.url_rule.rule)
        if auth_endpoint_rule is not None:
            groups_allowed = auth_endpoint_rule.get(request.method) or True
        else:
            groups_allowed = True

        auth = request.authorization
        if not ('username' in session):
            if not auth or not ldap_authenticate(request, auth.username, auth.password, groups_allowed):
                return auth_401()
        else:
            auth_logger.debug("%s calling %s endpoint" % (session['username'], f.__name__))
        return f(*args, **kwargs)

    return decorated


ldap_authenticate_01('ux222222')
