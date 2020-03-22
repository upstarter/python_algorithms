## Complexity of BST
h = height of tree

- **insert()**
  - O(h) time
- **find_min()** - go to left until hit a leaf
  - in BST its O(h) complexity
  - note: in a minHeap implementation you can pop the first item in constant time
- **next_layer()**
  - O(h) time, but could be O(n) without balanced binary search tree

## General Tree Traversals
The code will be the same for each with the difference being where we make our recursive call.

### in_order (Left, Root, Right)
If your BST contains all numbers, an in-order traversal of the tree will return a list of all the numbers in the tree, sorted. Inorder traversal gives nodes in non-decreasing order. To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal reversed can be used.

```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
```

### pre_order (Root, Left, Right)
Preorder traversal is used to create a copy of the tree. Preorder traversal is also used to get prefix expression on of an expression tree. Please see http://en.wikipedia.org/wiki/Polish_notation to know why prefix expressions are useful.

```python
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
```

### post_order (Left, Right, Root)
Postorder traversal is used to delete the tree. Please see the question for deletion of tree for details. Postorder traversal is also useful to get the postfix expression of an expression tree. Please see http://en.wikipedia.org/wiki/Reverse_Polish_notation to for the usage of postfix expression.

```python
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
```
