#!/usr/bin/python3

if __name__ == "__main__":
  """Add all interger from args"""
  import sys
  n = 0
  for i in range(len(sys.argv)):
    n += int(sys.argv[i + 1])
  print(n)
