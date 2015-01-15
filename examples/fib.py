import sys

sys.path.append('..')

from funcpy.decorators.memoize import memoize

@memoize
def fib(n):
    ''' A regular fibonacci function with memoization '''
    if n is 1 or n is 2:
        return 1
    return fib(n-1) + fib(n-2)

@memoize
def test(n, k):
    ''' Shows the memoization works well with currying '''
    return fib(n) + fib(k)
