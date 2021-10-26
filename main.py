#!/usr/bin/env python3

import argparse
from portal import *
from os import *
from sys import *

program_version = '1.1.4'
program_name = 'ahuportallogin'
program_description = 'Anhui University campus network login and logout script'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog=program_name,
        description=program_description
    )
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + program_version)
    parser.add_argument('-u', '--user', nargs='?', type=str, help='login username')
    parser.add_argument('-p', '--password', nargs='?', type=str, help='login password')
    parser.add_argument('--logout', action='store_true', help='logout of the campus network')
    args = parser.parse_args()
    try:
        portal = Portal()
    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
        print('Network is unreachable', file=stderr)
        exit(51)
    else:
        if args.logout:
            portal.request_logout()
        else:
            try:
                portal.set_credentials(args.user, args.password)
            except IncompleteCredentialsError:
                print('Login credentials are incomplete', file=stderr)
                print('Both username and password are required when login', file=stderr, end=linesep + linesep)
                parser.print_help(file=stderr)
                exit(22)
            except KeyboardInterrupt:
                exit(0)
            else:
                portal.request_login()
    exit(0)


