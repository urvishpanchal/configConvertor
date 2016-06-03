# -*- coding: utf-8 -*-
# Copyright (c) 2016 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

"""
"""

import imp
import os
import argparse
import arista
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--filename', nargs='*', help=('Full path of the Running config file that you want to convert to EOS config'))
    parser.add_argument('-o','--os',help=('The venodor OS from which you want to convert the configs. Example: nxos,ios,junos'))
    parser.add_argument('-p','--part',help=('Specify which part of the config needs to be converted. Example : access-list, policy-map, route-map or "complete" for the complete config. Note: Complete config is not supported yet'))
    return parser.parse_args()

def parse_file(filepath):
    """
    input: file path for the file that we want to convert
    returns: a string array object
    """
    parsed_file = []
    data = open(filepath).read()
    for line in [x.rstrip() for x in data.splitlines()]:
        parsed_file.append(line)

    return parsed_file

    return
def main():
    """Main routing. provides entry point hook to conversion tools"""
    args = parse_args()

    if args.filename is None:   # if filename is not given
        print('Filename not given. Example: -f /opt/test.txt')
        sys.exit()
    if args.os is None:
        print('Vendor OS not given. Example: -o nxos')
        sys.exit()
    if args.part is None:
        print('The part of config that you want to convert is not specified. Example: -p access-list, -p route-map or -p complete')
        sys.exit()

    #print(args.configfile[0])
    if args.configfile[0]:
        parsed_file = parse_file(args.configfile[0])
    #print(args.part)
    if args.part=='access-list' and args.os=='nxos':
        converted_list = arista.get_access_list(parsed_file)
    elif args.part=='route-map' and args.os=='nxos':
        converted_list = arista.get_route_map(parsed_file)
    elif args.part=='class-map' and args.os=='nxos':
        converted_list = arista.get_class_map(parsed_file)

    for acl in converted_list:
        print(acl)


if __name__ == '__main__':
    main()
