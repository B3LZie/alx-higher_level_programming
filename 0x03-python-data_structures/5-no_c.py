#!/usr/bin/python3
def no_c(my_string):
    j = 0
    new_string = list(my_string)
    for i in my_string:
        if i == 'c' or i == 'C':
            new_string[j] = ""
        j += 1
    return "".join(new_string)
