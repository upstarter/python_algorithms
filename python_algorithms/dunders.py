# CORE
# __add__  # maps to + operator
# __getitem__  # access by index in list, or key in dict
# __len__  # get length with len
#
#
# # ITERATORS
# __iter__  # returns an Iterator like `self` in `MyIterableClass`
# __next__  # must raise exception StopIteration when no more items to return
#

# CAN ALIAS
# set in class
class Word:
    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return self.word

    def __add__(self, other_word):
        return Word("%s %s" % (self.word, other_word))

    # needs to be after definition of add
    concat = __add__


a = Word("the")
b = Word("words")


print(a + b)
# => the words
print(a.concat(b))
# => the words

print(Word.__add__ == Word.concat)
# => True
