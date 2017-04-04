import sys

def ljust(string, length):
    count_length = 0
    for char in string:
        if ord(char) <=255:
            count_length += 1
        else:
            count_length += 2

    return string + (length-count_length) * ' '

