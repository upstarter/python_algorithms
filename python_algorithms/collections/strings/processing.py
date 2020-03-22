# is string a palindrome, read forward and backward the same
s = "Was it a cat I saw?"

# solution not space efficient, uses space proportional to size of string "s", (linear space)
# s = ''.join([i for i in s if i.isalpha()]).replace(" ", "").lower()
# print(s == s[::-1])

# Iterative, does not use linear space, just linear time
def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True


# print is_palindrome(s)

# add opening to a list
# whenever we get a closing, it should be closer for last element in list
# if last is not same type as closing or no last opening symbol at all (empty list), can stop - unbalanced
# else we can remove last opening symbol in the list because we have got its counterpart
# we keep track of unclosed parens
def balanced_parens(chars):
    stack = []
    opens = ["(", "[", "{"]
    closes = [")", "]", "}"]

    for c in chars:
        if c in opens:
            stack.insert(0, c)
        elif c in closes:
            pos = closes.index(c)
            if (len(stack) > 0) and (opens[pos] == stack[0]):
                stack.pop(0)
            else:
                return False
    if not stack:
        return True
    else:
        return False


print(balanced_parens("()[]{}") == True)
print(balanced_parens("{[]{()}}") == True)
print(balanced_parens("(()") == False)
print(balanced_parens(")[](") == False)
print(balanced_parens(")[]()") == False)
