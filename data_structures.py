# Compare the two binary trees, return True if they are equal else return false
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Are the trees structurally identical? return true if so, else return false
def compare(a, b):
    if a is None and b is None:
        return True
    if a is not None and b is not None:
        return ((a.val == b.val) and
                compare(a.left, b.left) and compare(a.right, b.right))
        return True

    return False


# Let's compare the value in the tree nodes
a_node = TreeNode(1)
b_node = TreeNode(1)

a_node.left = TreeNode(2)
a_node.right = TreeNode(3)

a_node.left.left = TreeNode(4)
a_node.left.right = TreeNode(5)

b_node.left = TreeNode(2)
b_node.right = TreeNode(3)

b_node.left.left = TreeNode(4)
b_node.left.right = TreeNode(5)

if compare(a_node, b_node):
    print("Both trees are identical")
else:
    print("Trees are not identical")

if compare(a_node.right, b_node.right):
    print("True")
else:
    print("False")

if compare(a_node.left, b_node.left):
    print("True")
else:
    print("False")
if compare(a_node.left.left, b_node.left.left):
    print("True")
else:
    print("False")