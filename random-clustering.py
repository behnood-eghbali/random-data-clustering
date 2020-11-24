#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:03:08 2020

@author: behnood
"""

from string import ascii_uppercase
from itertools import repeat
import random

patterns = []
pattern = ''
for letter in ascii_uppercase:
    pattern += letter
    patterns.append(pattern)
    patterns.extend(repeat(patterns[0],2))
    random_patterns = random.sample(patterns, len(patterns))
print(random_patterns)
