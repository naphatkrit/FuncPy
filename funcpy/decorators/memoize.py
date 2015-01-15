import curry

def memoize(func):
    '''
    Optimize a function using a dictionary to remember its outputs. Inputs
    must be hashable (must be able to serve as keys to a dictionary).
    All memoized functions are automatically curried
    '''
    func = curry.curry(func) 
    memo = dict()
    @curry.curry
    def helper(x):
        key = x
        if key not in memo:
            answer = func(x)
            if curry.is_curry_function(answer) and curry.is_same_curry_function(func)(answer):
                answer = memoize(answer)
            memo[key] = answer
        return memo[key]
    return helper
