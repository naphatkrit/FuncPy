import sys

sys.path.append('..')

from funcpy.decorators.curry import curry

@curry
def add(x, y):
    return x + y

add1 = add(1)

assert( (1 | add1 | add1) == 3)
