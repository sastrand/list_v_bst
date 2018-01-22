#!/usr/bin/python3
# Copyright (c) 2018 Sascha Strand
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE for the source
# distribution of this software for license terms

from sys import argv
from ipaddress import ip_address
from time import time

# takes a file pointer to file of ip address 
# and returns a list of those ip addresses as Ints
def ip_reader(fp):
    buf = fp.readlines()
    ret = []
    for ip in buf:
        ip = int(ip_address(ip.rstrip()))
        ret.append(ip)
    return ret

# Node class of a BST
# Create a root node for use with insert and search with
#   root = BST(ip_int)
class BST(object):
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None

    def __str__(self):
        return '({}, {}, {})'.format(self.l, self.val, self.r)

def insert(val, parent):
    pass

def search(val, parent):            
    pass


# Code block to time list
# var wl is the whitelist
# var traf is the list of all intercepted IPs
t0 = time()
ret = 0
for ip in traf:
    if ip in wl:
        ret+=1
t1 = time()
 
print("IPs matches in list:{}. Time: {} seconds".format(ret, t1-t0))

# Code block to time BST
# var root is the root node of the BST
t2 = time()
ret = 0
for ip in traf:
    if search(ip, root):
        ret+=1
t3 = time()

print("IPs matched in tree:{}. Time: {} seconds".format(ret, t3-t2))

