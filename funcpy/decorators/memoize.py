def memoize(func):
    import inspect
    from curry import curry, is_curry_function, is_same_curry_function
    func = curry(func) 
    memo = dict()
    def helper(x):
        key = hash(x)
        if key not in memo:
            print 'Cache miss for ' + str(key)
            answer = func(x)
            if is_curry_function(answer) and is_same_curry_function(func)(answer):
                answer = memoize(answer)
            memo[key] = answer
        return memo[key]
    return helper

@memoize
def fib(n):
    if n is 1 or n is 2:
        return 1
    return fib(n-1) + fib(n-2)

@memoize
def test(n, k):
    return fib(n) + fib(k)
