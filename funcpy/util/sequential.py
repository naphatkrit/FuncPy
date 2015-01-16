from funcpy.decorators.curry import curry

_map = map
_reduce = reduce

@curry
def map(transform, sequence):
    return _map(transform, sequence)

@curry
def reduce(combine, base, sequence):
    return _reduce(combine, sequence, base)

@curry
def map_reduce(transform, combine, base):
    return (map (transform)) >> (reduce(combine) (base))
