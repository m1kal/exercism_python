import re

def digit(input):
  return 10 if input=='X' else int(input)

def is_valid(isbn):
    clean = re.sub(r'-','',isbn)
    if not re.match(r'^\d{9}[\dX]$', clean):
        return False
    return sum(digit(i)*j for i,j in zip(clean, range(10, 0, -1))) % 11 == 0

