#!/usr/bin/python3

if __name__ == "__main__":
  """print arguments number and list args"""
  import sys
  
  counter = len(sys.argv)
  if counter == 0:
    print(0. arguments)
  elif counter == 1:
    print(1. arguments)
  else:
     print("{} arguments:".format(counter))
    for i in range(counter):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
