#!/usr/bin/env python3

import os
import sys


def parse_args(argv):
    print(argv)
    
def main():
    # list of parent arguments
    parent_argv = ['list','stop','start','terminate','status']
    
    # get the argument
    args = sys.argv[1:]

    if len(args) == 0:
        print("Error")
        quit(1)
    elif args[0] not in parent_argv:
        print("Error: Invalid argument")
        quit(1)
    else:
        parse_args(args)

if __name__ == '__main__':
    main()