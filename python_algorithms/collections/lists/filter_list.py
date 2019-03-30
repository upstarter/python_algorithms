mylist = [4, 9, -8, 15, -6, 1, 3, -4]

# might produce large in memory structure if input large, see generators
[n for n in mylist if n > 0]
#=> [1, 4, 9, 15, 3]
# generator
pos = (n for n in mylist if n > 0)
#=> <generator object <genexpr> at 0x1006a0eb0>
for x in pos:
    print(x)

# For filtering exception handling or some other complicated detail,
# put the filtering code into its own function and use the built-in
# filter() function

values = ['10', '12', '-8', '-', '20', 'N/A', '1']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)
# Outputs ['1', '2', '-3', '4', '5']
