import argparse
from portal import *

version = '1.0.0'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='ahuportallogin',
        description='AnHui University wifi portal login&logout script'
    )
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + version)
    parser.add_argument('-u', '--user', nargs='?', type=str, help='login username')
    parser.add_argument('-p', '--password', nargs='?', type=str, help='login password')
    parser.add_argument('--logout', action='store_true', help='logout of ahu.portal')
    args = parser.parse_args()
    if args.logout is True:
        logout = Portal()
        logout.request_logout()
        del logout
    elif args.user is not None and args.password is not None:
        login = Portal()
        if login.is_logged_in():
            del login
        else:
            login.set_credentials(args.user, args.password)
            result = login.request_login()
            del login
    else:
        parser.error('Unexpected arguments. Try -h or --help for detailed usage.')
