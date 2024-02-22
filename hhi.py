# libs
import requests
import sys
import argparse
from func import *

def main():
    # argparse setup
    parser = argparse.ArgumentParser(
        prog='HHI',
        description='host header injection automation basic tool',
        usage='%(prog)s -u target')
    parser.add_argument('-u', dest='url', metavar='URL', action='store', help='Target URL (e.g. "http://www.site.com")')
    parser.add_argument('-l', dest='list', metavar='FILEPATH', help='target list of urls')
    parser.add_argument('-r', dest='head', help='add custom host header')
    args = parser.parse_args()

    # check the target url or list
    if not args.url and not args.list:
        print("Error: Either -u/--url or -l/--list option is required.")
        parser.print_help()
        sys.exit(1)

    # main code here
    if args.url:
            url(args.url, args.head)
    elif args.url and args.head:
        url(args.url, args.head)
    else:
        print("Error: Either -u/--url or -l/--list option is required.")
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
