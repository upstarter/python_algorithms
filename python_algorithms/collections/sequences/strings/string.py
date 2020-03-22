from pprint import pprint

# Useful Python String Methods:

# len() – Returns the length of the string
# s1 in s2 – Is s1 a substring of s2
# index(s1) – Returns the index of s1 in the string
# list(s1) – Converts s1 into a character array
# s1[i:j] – Get  the substring of s1 from i to j

x = "Cake"
y = "Cookie"

# concat
x + " & " + y

# Repeat
x * 2

print(x.index("k"))
# => 2

# Range Slicing
print(x[2:])  # index 2 and up
# => 'ke'

print(x[::-1])  # reversed
# => 'ekaC'

print(x[::2])  # step=3, every 3rd char
# =>  'Ck'

print(x[-1])  # last char
# => 'e'

print(x[1:4])  # substring from i=2 to i=5
# => 'ake'

# Slicing
z2 = y[0] + y[1]

print(z2)

str1 = "Cake 4 U"
str2 = "404"
len(str1)  # OFF BY ONE FOR ITER!
print(str1.isdigit())
# False
print(str2.isdigit())
# True
print(str1.replace("4 U", str2))
# => 'Cake 404'
print(str1.upper())
# => 'CAKE 4 U'
print(str1.lower())
# => 'cake 4 u'


# substrings
str1 = "I got you a cookie"
str2 = "cook"
print(str1.find(str2))
