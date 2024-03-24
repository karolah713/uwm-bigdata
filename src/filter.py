#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
    # print("Usage: filter.py <word>")
    # sys.exit(1)
    raise ValueError("You have to provide exactly one argument")

word = sys.argv[1]

for line in sys.stdin:
    if word in line:
        line = line.strip()
        print(line)

word = 'she'

for line in sys.stdin:
    if word in line:
        line = line.strip()
        print(line)

        # line_length, *tokens = line.split(",")  # split line into words using comma as delimiter
        # print(line_length, tokens)



