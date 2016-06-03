dict_acl = {
    "eigrp":"88",
    "eisp":"50",
    "nos":"not supported",
    "pcp":"not supported",
    "precedence":"not supported"
}


dict_route_map = {
    "pop":"not supported",
    "push":"not supported",
    "where":"not supported",
    "length":"not supported",
    "mac-list":"not supported",
    "route-type":"metric-type",     # only supports type-1/type-2 
    "external":"not supported",     #match route-type ?
    "internal":"not supported",     #match route-type ?
    "level-1":"not supported",      #match route-type ?
    "level-2":"not supported",      #match route-type ?
    "local":"not supported",        #match route-type ?
    "nssa-external":"not supported" #match route-type ?
}

dict_class_map = {
    "pop":"not supported",
    "push":"not supported",
    "where":"not supported",
    "network-qos":"not supported",
    "queuing":"not supported",
    "match-any":"match-all", 
    "access-group":"not supported",
    "cos":"not supported",
    "dscp":"not supported",
    "precedence":"not supported"
}


dict_policy_map = {
    "pop":"not supported",
    "push":"not supported",
    "where":"not supported",
    "coop-s-default":"not supported",
    "police":"not supported"
}

dict_interfaces = {
    "mgmt":"management",
    "beacon":"not supported", # for interfaces
    "cdp":"not supported",
    "untagged":"not supported",
    "pop":"not supported",     
    "push":"not supported",
    "where":"not supported",
    "duplex":"not supported",
    "delay":"not supported",
    "hardware":"not supported",
    "lacp":"not supported",
    "link-state-trap":"not supported",
    "negotiate":"not supported",
    "speed":"not supported"
}

