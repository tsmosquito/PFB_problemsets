#!/usr/bin/env python3

import sys
min_cent = int(sys.argv[1])
max_cent = int(sys.argv[2])

centurion = [cent for cent in range(min_cent, max_cent) if cent % 2 == 1]

print(centurion)