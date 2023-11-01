#!/usr/bin/python3
# 100-print_tebahpla.py

for i in range(122, 96, -1):
    if i % 2:
        i = i - 32
    print("{:c}".format(i), end="")
