#!/usr/bin/python3
# Copyright (c) 2018 Sascha Strand
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE for the source
# distribution of this software for license terms

from time import time


class BST(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return '({}, {}, {})'.format(self.left, self.val, self.right)

    def insert(self, val):
        pass

    def search(self, val):
        pass


def ip_reader(fp):
    buf = fp.readlines()
    ret = []
    for ip in buf:
        ret.append(ip.rstrip())
    return ret


def time_list(traf, wl):
    t0 = time()
    ret = 0
    for ip in traf:
        if ip in wl:
            ret += 1
    t1 = time()
    print("IPs matches in list: {}. Time: {} seconds".format(ret, t1 - t0))


def time_bst(traf, wl):
    root = BST(wl[0])
    [root.insert(x) for x in wl]
    t2 = time()
    ret = 0
    for ip in traf:
        if root.search(ip):
            ret += 1
    t3 = time()
    print("IPs matched in tree: {}. Time: {} seconds".format(ret, t3 - t2))


def time_set(traf, wl):
    wl_set = set(wl)
    t4 = time()
    ret = 0
    for ip in traf:
        if ip in wl_set:
            ret += 1
    t5 = time()
    print("IPs matched in set:  {}. Time: {} seconds".format(ret, t5 - t4))


if __name__ == "__main__":

    with open("./data/traffic_test.txt", 'r') as f:
        traf = ip_reader(f)

    with open("./data/whitelist_test.txt", 'r') as f:
        wl = ip_reader(f)

    time_list(traf, wl)
    time_bst(traf, wl)
    time_set(traf, wl)
