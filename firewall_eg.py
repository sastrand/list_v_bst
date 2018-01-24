#!/usr/bin/python3
# Copyright (c) 2018 Sascha Strand
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE for the source
# distribution of this software for license terms

from sys import argv
from ipaddress import ip_address
from time import time

class BST(object):
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None

    def __str__(self):
        return '({}, {}, {})'.format(self.l, self.val, self.r)

def insert(val, parent):
    if val == parent.val: return
    if val < parent.val:
        if parent.l:
            insert(val, parent.l)
        else:
            parent.l = BST(val)
    else:
        if parent.r:
            insert(val, parent.r)
        else:
            parent.r = BST(val)

def search(val, parent):
    if val == parent.val: return True
    if val < parent.val:
        if parent.l:
            return search(val, parent.l)
        else:
            return None
    else:
        if parent.r:
            return search(val, parent.r)
        else:
            return None

def ip_reader(fp):
    buf = fp.readlines()
    ret = []
    for ip in buf:
        ip = int(ip_address(ip.rstrip()))
        ret.append(ip)
    return ret

with open(argv[1], 'r') as f:
    traf = ip_reader(f)

with open(argv[2], 'r') as f:
    wl = ip_reader(f)

t0 = time()
ret = 0
for ip in traf:
    if ip in wl:
        ret+=1
t1 = time()
 
print("IPs matches in list:{}. Time: {} seconds".format(ret, t1-t0))

root = BST(wl.pop())
[insert(x, root) for x in wl]

t2 = time()
ret = 0
for ip in traf:
    if search(ip, root):
        ret+=1
t3 = time()

print("IPs matched in tree:{}. Time: {} seconds".format(ret, t3-t2))

