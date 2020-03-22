s1 = "doingProgramming"
s2 = "DoingProgramming"
s3 = "doingprogramming"

# Iterative Search String
def find_uppercase_iter(s):
    for i in range(len(s)):
        if s[i].isupper():
            return s[i]
    return "No uppercase character found"


# Recursive Search String
def find_uppercase_recursive(s, idx=0):
    if s[idx].isupper():
        return s[idx]
    if idx == len(s) - 1:
        return "No uppercase character found"
    return find_uppercase_recursive(s, idx + 1)


print(find_uppercase_iter(s1))
print(find_uppercase_iter(s2))
print(find_uppercase_iter(s3))

print(find_uppercase_recursive(s1))
print(find_uppercase_recursive(s2))
print(find_uppercase_recursive(s3))
