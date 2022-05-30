#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print(f"1 argument:\n1: {sys.argv[1]}")
else:
    print(f"{len(sys.argv)} arguments:")
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
