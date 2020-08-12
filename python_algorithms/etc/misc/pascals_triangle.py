
'''
Pascal's triangle

1
1 1
1 2 1
1 3 3  1
1 4 6  4  1
1 5 10 10 5 1

'''

# A O(n^2) time and O(1) extra space method for Pascal's Triangle
def printPascal(n):
    for line in range(1, n + 1):
        C = 1; # used to represent C(line, i)
        for i in range(1, line + 1):

            # The first value in a
            # line is always 1
            print(C, end = ' ')
            C = int(C * (line - i) / i)
        print("");

printPascal(5);

def pascal(n):
    """Prints out n rows of Pascal's triangle.
    It returns False for failure and True for success."""
    row = [1]
    k = [0]
    for x in range(max(n,0)):
        print(row)
        row=[l+r for l,r in zip(row+k,k+row)]
    return n>=1

pascal(5)
