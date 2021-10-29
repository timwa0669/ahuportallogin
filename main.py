#!/usr/bin/env python3

import argparse
from portal import *
from os import *
from sys import *
import errno

program_version = '1.1.4.1'
program_name = 'ahuportallogin'
program_description = 'Anhui University campus network login and logout script'


def main():
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
        if args.logout:
            portal.request_logout()
        else:
            portal.set_credentials(args.user, args.password)
            portal.request_login()
    except requests.exceptions.ConnectionError:
        print('Network is unreachable', file=stderr)
        exit(errno.ENETUNREACH)
    except requests.exceptions.ReadTimeout:
        print('Connection timed out', file=stderr)
        exit(errno.ETIMEDOUT)
    except IncompleteCredentialsError:
        print('Login credentials are incomplete', file=stderr)
        print('Both username and password are required when login', file=stderr, end=linesep + linesep)
        parser.print_help(file=stderr)
        exit(errno.EINVAL)
    except KeyboardInterrupt:
        exit(errno.EINTR)
    exit(0)


if __name__ == '__main__':
    main()