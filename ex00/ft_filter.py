def ft_filter(function_to_apply, list_of_inputs):
	if function_to_apply is None:
		for inputs in list_of_inputs:
			yield (inputs)
	else:
		for inputs in list_of_inputs:
			if (function_to_apply(inputs) is True):
				yield (inputs)


'''
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

for x in ft_filter(None, scores):
	print(x)

for x in filter(None, scores):
	print(x)
'''