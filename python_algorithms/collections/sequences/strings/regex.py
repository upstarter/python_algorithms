import sys
import re

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
# m[0] is shortcut for .group(1)
print(m[0])  # The entire match
# "Isaac Newton"
print(m[1])  # The first parenthesized subgroup.
# "Isaac"
print(m[2])  # The second parenthesized subgroup.
# "Newton"
print(m.group(1, 2))  # Multiple arguments give us a tuple.
# ("Isaac", "Newton")


# Suppose you are writing a poker program where a player’s hand is represented as
# a 5-character string with each character representing a card, “a” for ace, “k”
# for king, “q” for queen, “j” for jack, “t” for 10, and “2” through “9”
# representing the card with that value.


def displaymatch(match):
    if match is None:
        return None
    return "<Match: %r, groups=%r>" % (match.group(), match.groups())


# To see if a given string is a valid hand, one could do the following:
valid = re.compile(r"^[a2-9tjqk]{5}$")
displaymatch(valid.match("akt5q"))  # Valid.
# "<Match: 'akt5q', groups=()>"

displaymatch(valid.match("akt5e"))  # Invalid.
displaymatch(valid.match("akt"))  # Invalid.
displaymatch(valid.match("727ak"))  # Valid.
# "<Match: '727ak', groups=()>"

# That last hand, "727ak", contained a pair, or two of the same valued cards. To
# match this with a regular expression, one could use backreferences as such:

pair = re.compile(r".*(.).*\1")
displaymatch(pair.match("717ak"))  # Pair of 7s.
# "<Match: '717', groups=('7',)>"
displaymatch(pair.match("718ak"))  # No pairs.
displaymatch(pair.match("354aa"))  # Pair of aces.
# "<Match: '354aa', groups=('a',)>"

# To find out what card the pair consists of, one could use the group() method of
# the match object in the following manner:

pair = re.compile(r".*(.).*\1")
pair.match("717ak").group(1)
# '7'

# Error because re.match() returns None, which doesn't have a group() method:
try:
    pair.match("718ak").group(1)
except:
    print("Nope")
# Traceback (most recent call last):
#   File "<pyshell#23>", line 1, in <module>

try:
    re.match(r".*(.).*\1", "718ak").group(1)
except:
    print("Nope again")
# AttributeError: 'NoneType' object has no attribute 'group'

pair.match("354aa").group(1)
# 'a'

thismodule = sys.modules[__name__]

# find all functions in current module matching a pattern
funcRegex = re.compile(r".*_to_.*")
funcs = filter(funcRegex.search, dir())
print(funcs)
