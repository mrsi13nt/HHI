# libs
import requests
import os
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
    parser.add_argument('-k', dest='cookie', metavar='COOKIE', help='add custom cookies')
    args = parser.parse_args()

    # check the target url or list
    if not args.url and not args.list:
        print("Error: Either -u/--url or -l/--list option is required.")
        parser.print_help()
        sys.exit(1)

    # single url
    if args.url: # url only
            url(args.url, args.head,None)
    elif args.url and args.head: # url and host header
        url(args.url, args.head,None)
    elif args.url and args.cookie: # url and cookies
        url(args.url,None,args.cookie)
    elif args.url and args.head and args.cookie: # url and host header and cookies
        url(args.url,args.head,args.cookie)
    # list of urls
    elif args.list: # list of urls only
        file_p = args.list
        if check_file_existence(file_p): # check if the file exist
            with open(file_p, 'r') as file:
                lines = [line.strip() for line in file]
                for line in lines:
                    url(line,None,None)
        else:
            print(f"the file {file} not exist\n please try again with full path")
    elif args.list and args.head: # list of urls and host header
        file_p = args.list
        if check_file_existence(file_p): # check if the file exist
            with open(file_p, 'r') as file:
                lines = [line.strip() for line in file]
                for line in lines:
                    url(line,args.head,None)
        else:
            print(f"the file {file} not exist\n please try again with full path")
    elif args.list and args.cookie: # list of urls and cookies
        file_p = args.list
        if check_file_existence(file_p): # check if the file exist
            with open(file_p, 'r') as file:
                lines = [line.strip() for line in file]
                for line in lines:
                    url(line,None,args.cookie)
        else:
            print(f"the file {file} not exist\n please try again with full path")
    elif args.list and args.head and args.cookie: # list of urls and host header and cookies
        file_p = args.list
        if check_file_existence(file_p): # check if the file exist
            with open(file_p, 'r') as file:
                lines = [line.strip() for line in file]
                for line in lines:
                    url(line,args.head,args.cookie)
        else:
            print(f"the file {file} not exist\n please try again with full path")
    else:
        print("Error: Either -u/--url or -l/--list option is required.")
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
