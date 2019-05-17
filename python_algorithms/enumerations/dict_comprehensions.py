#### Dict Comprehension


my_dict = {'a': 1, 'b': 2, 'c': 3}
result = {k + '_key': v * 2 for k,v in my_dict.items()}
print(result)
print(result.keys())
print(result.values())
print(result.items())

fruits = ['apple', 'mango', 'banana','cherry']
f1 ={f:f.capitalize() for f in fruits}
# keys to be removed
remove_this = {'apple','cherry'}
# dict comprehension example to delete key:value pairs in a dictionary
{key:f1[key] for key in f1.keys() - remove_this}
#=> {'banana': 'Banana', 'mango': 'Mango'}
