# FuncPy
FuncPy is a functional programming library for Python.
## Currying
Using @curry from funcpy.decorators.curry, one can turn regular python functions
into functions with currying. Note that what is actually implemented is partial
application, but practically, there is little difference. Note that FuncPy
assumes all functions are curried, and any functions not curried are automatically
given @curry.

## Pipeline
Use the | operator on curried functions to "pipe" an input into the function.
For example,

## Function Composition
Use the >> and << operators to compose two curried functions.
