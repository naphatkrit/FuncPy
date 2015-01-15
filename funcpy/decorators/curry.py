def _get_args_count(f):
    import inspect
    (args, _, _, _) = inspect.getargspec(f)
    return len(args)

class _CurriedFunc:
    ''' 
    Got idea from 
    https://mtomassoli.wordpress.com/2012/03/29/pipelining-in-python/ 
    '''
    def __init__(self, func, args = ()):
        self.__func = func
        self.__args = args

    def __call__(self, *args):
        if len(args) is 0:
            # the case where no args is needed
            return self.__func(*self.__args)
        args = args[0] if len(args) == 1 else args
        args = self.__args + (args,)
        if len(self.__args) < _get_args_count(self.__func) - 1:
            return _CurriedFunc(self.__func, args)
        else:
            return self.__func(*args)

    def is_same_curry(self, other):
        return self.__func is other.__func

def is_curry_function(f):
    '''
    Returns True if f is the result of applying curry() to a function
    '''
    return isinstance(f, _CurriedFunc)

def curry(f):
    '''
    A curried function takes one argument and either return a new function
    or returns an answer. 

    @curry
    def add(x, y): return x + y

    add(1)(2) # 3
    add1 = add(1)
    add1(5) # 6
    add1(6) # 7
    '''
    return _CurriedFunc(f) if not is_curry_function(f) else f

@curry
def is_same_curry_function(f1, f2):
    '''
    Returns True if f1 and f2 are originally from the same function
    '''
    assert(is_curry_function(f1))
    assert(is_curry_function(f2))
    return f1.is_same_curry(f2)
