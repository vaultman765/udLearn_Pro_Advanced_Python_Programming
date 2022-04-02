dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

x = dict1.keys()
print("Dict keys: ", x)

x = dict1.values()
print("Dict values: ", x)

z = dict1.items()
print("Dict items: ", z)

new_dict_values = {k: v*2 for (k, v) in dict1.items()}
print("Dict comprehension for multiplying by 2: ", new_dict_values)

new_dict_keys = {k*2: v for (k, v) in dict1.items()}
print("New keys 'multiplying by 2': ", new_dict_keys)
