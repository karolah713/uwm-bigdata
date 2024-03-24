#!/usr/bin/env python
import sys

counter = {}

for line in sys.stdin:
    count, word = line.split()
    count = int(count)
    if word in counter:
        counter[word] += count
    else:
        counter[word] = count

for word, count in counter.items():
    print(word, count)




