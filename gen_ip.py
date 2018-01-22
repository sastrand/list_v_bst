#!/usr/bin/python3
# Copyright (c) 2018 Sascha Strand
# [This program is licensed under the "MIT License"]
# Please see the file LICENSE for the source
# distribution of this software for license terms

# Write two files of random IPv4 address
# Takes three CL params: 
#   the file name for all random addresses
#   the file name for a subset of those addresses
#   the power of two quantity of addresses in the first file

import random
from sys import argv

t = 2**int(argv[3])

f_all = open(argv[1], 'w')
f_wht = open(argv[2], 'w')
d = []

for i in range(t):
    ip = ".".join(map(str, [random.randint(0,255) for _ in range(4)]))
    f_all.write('{}\n'.format(ip))
    if i % t**(0.5) == 0:
        f_wht.write('{}\n'.format(ip))

for ip in d:
    f_all.write('{}\n'.format(ip))

print("Intercepted datagrams: {}".format(t))
print("Expected approved datagrams: {}".format(t**(0.5)))
