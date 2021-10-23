import argparse
from portal import *
import os

version = '1.1.1'
program_name = 'ahuportallogin'
program_description = 'AnHui University wifi portal login&logout script'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog=program_name,
        description=program_description
    )
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + version)
    parser.add_argument('-u', '--user', nargs='?', type=str, help='login username')
    parser.add_argument('-p', '--password', nargs='?', type=str, help='login password')
    parser.add_argument('--logout', action='store_true', help='logout of ahu.portal')
    args = parser.parse_args()
    portal = Portal()
    if args.logout:
        portal.request_logout()
    else:
        try:
            portal.set_credentials(args.user, args.password)
        except ValueError:
            print('Login credentials are incomplete', file=os.sys.stderr)
            print('Both username and password are required when login', file=os.sys.stderr, end=os.linesep + os.linesep)
            parser.print_help(file=os.sys.stderr)
            exit(1)
        else:
            portal.request_login()
    exit(0)


