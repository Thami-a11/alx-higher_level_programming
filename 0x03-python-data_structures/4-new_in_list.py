#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)
    elif idx > len(my_list) - 1:
         return(my_list)
    newlist = my_list
    newlist[idx] = element
    return(newlist)
