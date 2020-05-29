def ft_reduce(function_to_apply, list_of_inputs):
    inc = 0
    tot = 0
    if (len(list_of_inputs) > 0):
        for inputs in list_of_inputs:
            if inc == 0:
                tot = inputs
            else:
                tot = function_to_apply(tot, inputs)
            inc += 1
        return(tot)
    else:
        raise TypeError("reduce() of empty sequence with no initial value")


'''
scores = []

import operator
import functools

print(ft_reduce(operator.mul, scores))
print(functools.reduce(operator.mul, scores))
'''
