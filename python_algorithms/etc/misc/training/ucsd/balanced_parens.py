# add opening to a list
# whenever we get a closing, it should be closer for last element in list if
# last is not same type as closing or no last opening symbol at all (empty
# list), can stop - unbalanced else we can remove last opening symbol in the
# list because we have got its counterpart we keep track of unclosed parens
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
