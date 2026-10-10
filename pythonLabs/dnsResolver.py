#!/usr/bin/python
import os
import sys

with open('/etc/resolv.conf', 'r') as f:
    for line in f:
        if line.startswith('nameserver'):
            print(line.split()[1])
            break
