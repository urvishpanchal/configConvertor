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

def parse_args():
    parser = argparse.ArgumentParser(prog="configConvertor")
    arg = parser.add_argument
    arg('-c','configfile', nargs='*', help=('Full path of the Running config that you want to convert to EOS config'))
    arg('-o','OS',help=('The OS from which you want to convert the configs'))
    arg('-')
    return parser.parse_args()

def parse_file(filepath):
    """
    input: file path for the file that we want to convert
    returns: a string array object
    """
    for line in [x.rstrip() for x in data.splitlines()]:



    return
def main():
    """Main routing. provides entrypoint hook to setuputils"""
    args = parse_args()
    if args.configfile:
        parsed_file = parse_file(args.configfile)

if __name__ == '__main__':
    main()
