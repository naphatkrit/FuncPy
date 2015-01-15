import sys

sys.path.append('..')

from funcpy.decorators.curry import curry

@curry
def add(x, y):
    return x + y

add1 = add(1)
add2 = add(2)

add3 = add1 << add2

def print_test(x):
    print x

def make_str(x):
    return str(x)

print_add = add1 >> make_str >> print_test

assert( add3(1) == 4)

