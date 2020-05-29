def ft_map(function_to_apply, list_of_inputs):
    for x in list_of_inputs:
        yield (function_to_apply(x))


'''
import string
def ft_map(function_to_apply, list_of_inputs):
    listed = list()
    for x in list_of_inputs:
        listed.append(function_to_apply(x))
    return (listed)

listed = ['frf', 'rer', 'dede', 'fe', 'sfs']
def ft_tr(strind):
    return(strind.upper())

for x in ft_map(ft_tr, listed):
    print(x)
'''
