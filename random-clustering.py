#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:03:08 2020

@author: behnood
"""

from string import ascii_uppercase
from itertools import repeat
import random
import pandas as pd

patterns = []
pattern = ''
for letter in ascii_uppercase:
    pattern += letter
    patterns.append(pattern)
    patterns.extend(repeat(patterns[0],2))
    random_patterns = random.sample(patterns, len(patterns))
print(random_patterns)

# output:
# ['ABCDEFGHIJKL', 'A', 'A', 'A', 'ABCDEFGHIJ', 'A', 'A', 'A', 'A', 'ABCDEFGHI', 'ABCDEFGHIJKLMNOPQRS', 'A', 'ABCDEFGHIJKLMNOPQRST', 'A', 'A', 'A', 'A', 'ABCDEFG', 'A', 'ABCDEFGH', 'A', 'A', 'ABCDEFGHIJKLMNOPQR', 'ABCDEFGHIJKLMNOPQRSTU', 'A', 'A', 'ABCDEF', 'A', 'ABCDE', 'ABCDEFGHIJKLMNO', 'A', 'ABCDEFGHIJKLMNOPQRSTUVWXY', 'A', 'A', 'A', 'A', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLM', 'A', 'ABCDEFGHIJKLMNOP', 'A', 'ABCD', 'AB', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'ABCDEFGHIJKLMNOPQRSTUVWX', 'A', 'A', 'A', 'A', 'ABCDEFGHIJKLMNOPQRSTUVW', 'A', 'A', 'A', 'A', 'A', 'ABCDEFGHIJKLMNOPQ', 'A', 'A', 'A', 'ABCDEFGHIJKLMN', 'A', 'A', 'ABCDEFGHIJK', 'ABCDEFGHIJKLMNOPQRSTUV', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'ABC']

patterns_index = list(range(len(random_patterns)))

d = { 'index': patterns_index, 'list': random_patterns }

df = pd.DataFrame(d)
