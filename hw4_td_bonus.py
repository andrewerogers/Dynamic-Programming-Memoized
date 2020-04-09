## Author: Andrew Rogers
## Description: This program inputs an integer and outputs f(n)
## defined recursively in the homework.

_memo = {}

## Methods:

def function(n):
    var = 0

    if n in _memo:
        return _memo[n]

    ## Establish base case
    if int(n) < 2:
        if int(n) == 0:
            return 1
        if int(n) == 1:
            return 2
    else:
        ## Calculate sum i = 2 to n of f(i-1)*f(i-2)
        for i in range(2, int(n)+1):
            var += function(i-1)*function(i-2)

        _memo[n] = 2*var + 1
        return 2*var + 1

## Main:

print("Program written by: Andrew Rogers")
_inputsize = input("Please enter an integer: ")
_functionoutput = function(_inputsize)
print(f"f({_inputsize}) = {_functionoutput}")
        
