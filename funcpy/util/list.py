'''
Common algorithms involving lists
'''

from funcpy.decorators.curry import curry
from sequential import map, reduce, map_reduce

'''
flattens a list of lists
'''
flatten = reduce (lambda x,y: x + y) ([])

