import argparse
from portal import *
import os
import sys

version = '1.1.2'
program_name = 'ahuportallogin'
program_description = 'Anhui University campus network login and logout script'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog=program_name,
        description=program_description
    )
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + version)
    parser.add_argument('-u', '--user', nargs='?', type=str, help='login username')
    parser.add_argument('-p', '--password', nargs='?', type=str, help='login password')
    parser.add_argument('--logout', action='store_true', help='logout of the campus network')
    args = parser.parse_args()
    try:
        portal = Portal()
    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
        print('Network is unreachable', file=sys.stderr)
        exit(51)
    else:
        if args.logout:
            portal.request_logout()
        else:
            try:
                portal.set_credentials(args.user, args.password)
            except IncompleteCredentialsError:
                print('Login credentials are incomplete', file=sys.stderr)
                print('Both username and password are required when login', file=sys.stderr, end=os.linesep + os.linesep)
                parser.print_help(file=sys.stderr)
                exit(1)
            else:
                portal.request_login()
    exit(0)


