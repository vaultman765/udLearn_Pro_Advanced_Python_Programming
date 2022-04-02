dict1 = {'one': {'a': 10}, 'two': {'b': 20}}
print("Original dict: ", dict1)

# Convert numbers to float using for loop
for (external_key, external_value) in dict1.items():
    for (internal_key, internal_value) in external_value.items():
        external_value.update({internal_key: float(internal_value)})

dict1.update({external_key: external_value})
print("Using for loop to change to float: ", dict1)