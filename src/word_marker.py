#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    line_length, *tokens = line.split(",")  # split line into words using comma as delimiter
    for word in tokens:
        print(1, word)

