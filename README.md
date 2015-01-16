# FuncPy
FuncPy is a functional programming library for Python.
## Currying
Using @curry from funcpy.decorators.curry, one can turn regular python functions
into functions with currying. Note that what is actually implemented is partial
application, but practically, there is little difference. Note that FuncPy
assumes all functions are curried, and any functions not curried are automatically
given @curry.

```
@curry
def add(x, y, z):
  return x + y + z

add(1)(2)(3) # 6
add1 = add(1)
add1(2)(3) # 6
add3 = add1(2)
add3(3) # 6
```

## Pipeline
Use the | operator on curried functions to "pipe" an input into the function.
For example,

```
@curry
def increment(x):
  return x + 1
  
1 | increment # 2
1 | increment | increment # 3
```

## Function Composition
Use the >> and << operators to compose two curried functions.

```
@curry
def f(x):
  ...
  
@curry
def g(x):
  ...

k = f >> g
k(x) # = g(f(x))
k = f << g
k(x) # = f(g(x))
```
## Memoization
FuncPy provides a generic @memoize decorator in funcpy.decorators.memoize. 
Inputs to the arguments must be hashable (must be able to serve as dictionary keys).
Memoization optimizes recursive functions by saving results in a dictionary.

Here is how a memoized fibonacci function would look like:
```
@memoize
def fib(n):
  return fib(n-1) + fib(n-2)
```
