#!/usr/bin/python3

def element_at(my_list, idx):
  if idx < 0:
    return null
  elif idx > len(my_list):
    return null
  print("Element of {} is {}".format(idx,my_list[idx])
