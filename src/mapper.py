#!/usr/bin/env python
import sys

for line in sys.stdin:
    line_length = len(line)

    line = line.strip()
    line = line.replace(',', '').replace('.', '')    # remove commas
    words = line.split(' ')        # split line into words
    tokens = [str(line_length), *words]
    #sys.stdout.write(line)
    joined_words = ",".join(tokens)  # join words with comma
    print(joined_words)




