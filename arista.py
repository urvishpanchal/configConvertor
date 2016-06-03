# -*- coding: utf-8 -*-
# Copyright (c) 2016 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

"""
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import re
import os
import argparse
import consts

def get_access_list(parsed_file):
    converted_acl = []
    pattern_1 = re.compile(r"^(ip access-list|ipv6 access-list).*$")
    pattern_2 = re.compile(r"^[1-9].*(permit|deny).*$")
    for line in parsed_file:
        line = line.strip()
        if  pattern_1.search(line) or pattern_2.match(line):
            for key,value in consts.dict_acl.iteritems():
                if key in line and value != "not supported" and pattern_2.match(line):
                    line = line.replace(key,value)
                    break
                elif key in line and value == "not supported":
                    line = "#Command not supported on arista:" + line
                    break
            converted_acl.append(line)

    return converted_acl

def get_route_map(parsed_file):
    converted_route_map = []
    pattern_1 = re.compile(r"^route-map.*(permit|deny).*$")
    pattern_2 = re.compile(r"^match.*(ip|as-path|community).*$")
    for line in parsed_file:
        line = line.strip()
        if pattern_1.search(line) or pattern_2.match(line):
            for key,value in consts.dict_route_map.iteritems():
                if key in line and value != "not supported":
                    line = line.replace(key,value)
                    break
                elif key in line and value == "not supported":
                    line = "#Command not supported on arista:" + line
                    break
            converted_route_map.append(line)

    return converted_route_map
