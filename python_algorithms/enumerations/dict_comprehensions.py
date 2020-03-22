#### Dict Comprehension

my_dict = {"a": 1, "b": 2, "c": 3}

# Map keys and values sequentially
result = {k + "_key": v * 2 for k, v in my_dict.items()}
print(result)
# => {'b_key': 4, 'a_key': 2, 'c_key': 6}

print(result.keys())
# => ['b_key', 'a_key', 'c_key']
print(result.values())
# => [4, 2, 6]
print(result.items())
# => [('b_key', 4), ('a_key', 2), ('c_key', 6)]

# transform array to map while capitalizing values
fruits = ["apple", "mango", "banana", "cherry"]

f1 = {f: f.capitalize() for f in fruits}

print(f1)
# => {'cherry': 'Cherry', 'mango': 'Mango', 'apple': 'Apple', 'banana': 'Banana'}

# Delete key:value pairs in a dictionary
# keys to be removed
remove_this = {"apple", "cherry"}
#
f2 = {key: f1[key] for key in set(f1.keys()) - remove_this}
print(f2)
# #=> {'banana': 'Banana', 'mango': 'Mango'}
