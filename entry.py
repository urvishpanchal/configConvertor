# -*- coding: utf-8 -*-
# Copyright (c) 2016 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

"""
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import imp
import os
import argparse
import arista

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--configfile', nargs='*', help=('Full path of the Running config that you want to convert to EOS config'))
    parser.add_argument('-o','--os',help=('The OS from which you want to convert the configs'))
    parser.add_argument('-p','--part',help=('Specify which part of the config needs to be converted. Example : access-list, policy-map, route-map or the "complete" for the complete config. Note: Complete config is not supported yet'))
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
    #print(args.configfile[0])
    if args.configfile[0]:
        parsed_file = parse_file(args.configfile[0])
    #print(args.part)
    if args.part=='access-list' and args.os=='nxos':
        converted_list = arista.get_access_list(parsed_file)

    for acl in converted_list:
        print(acl)


if __name__ == '__main__':
    main()
