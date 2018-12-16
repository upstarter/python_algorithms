class Tree(object):
    def __init__(self, val, children=[]):
        self.val = val;
        self.children = children;

    def __str__(self, level=0, depth=0):
        if depth == 0:
            depth = self.getDepth()
        ret = "\t" * level + repr(self.val) + ("____" * depth) + "\n"
        for child in self.children:
            if child is None:
                ret += ("\t" * (level+1)) + "|\n"
            else:
                ret += child.__str__(level + 1, depth-1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

    def setVal(self, val):
        self.val = val

    def getVal(self):
        return self.val

    def getDepth(self):
        d = 1
        if self.children is None:
            return d
        for c in self.children:
            if c is not None:
                d = max(d, c.getDepth()+1)
        return d

class BinaryTree(Tree):
    def __init__(self, val, left=None, right=None):
        super().__init__(val, [left, right])
        self.val = val;
        self.children = [left, right];

    def setLeft(self, left):
        if left is None:
            return
        if (len(self.children) == 2):
            self.children = [left, self.children[1]]
        else:
            self.children = [left]

    def setRight(self, right):
        if right is None:
            return;
        if (len(self.children) >= 1):
            self.children = [self.children[0], right]
        else:
            self.children = [None, right]

    def getLeft(self):
        if self.children is None or len(self.children) < 1:
            return None;
        return self.children[0]

    def getRight(self):
        if self.children is None or len(self.children) < 2:
            return None;
        return self.children[1]

    def array2BTree(arr, start=0, end=None):
        if end is None:
            end = len(arr)
        if (end <= start):
            return None
        mid = int((start + end) / 2)
        node = BinaryTree(arr[mid]);
        node.setLeft(array2BTree(arr, start, mid));
        node.setRight(array2BTree(arr, mid + 1, end));
        return node

tree = Tree(1, [Tree(2, [Tree(2.1, [Tree(2.15)]), Tree(2.2)]), Tree(3), Tree(4)])
print(tree)
