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
import consts

def get_access_list(parsed_file):
    converted_list = []
    for line in parsed_file:
        line = line.strip()
        if  "ip access-list" in line or "ipv6 access-list" in line:
            #print("inside first if")
            converted_list.append(line)
        elif line and line[0].isdigit():
            for key,value in consts.dict_acl.iteritems():
                if key in line and value != "not supported":
                    #print("inside third if")
                    line = line.replace(key,value)
                    break
                    #converted_list.append(line)
                elif key in line and value == "not supported":
                    line = "#Command not supported on arista:" + line
                    break
            converted_list.append(line)

    return converted_list
