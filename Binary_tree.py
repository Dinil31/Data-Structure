class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp_val = self._min_value_node(root.right)
            root.val = temp_val.val
            root.right = self._delete(root.right, temp_val.val)
        
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        res = []
        self._inorder_traversal(self.root, res)
        return res

    def _inorder_traversal(self, root, res):
        if root:
            self._inorder_traversal(root.left, res)
            res.append(root.val)
            self._inorder_traversal(root.right, res)

    def preorder_traversal(self):
        res = []
        self._preorder_traversal(self.root, res)
        return res

    def _preorder_traversal(self, root, res):
        if root:
            res.append(root.val)
            self._preorder_traversal(root.left, res)
            self._preorder_traversal(root.right, res)

    def postorder_traversal(self):
        res = []
        self._postorder_traversal(self.root, res)
        return res

    def _postorder_traversal(self, root, res):
        if root:
            self._postorder_traversal(root.left, res)
            self._postorder_traversal(root.right, res)
            res.append(root.val)

# Example usage:
bt = BinaryTree()
bt.insert(50)
bt.insert(30)
bt.insert(20)
bt.insert(40)
bt.insert(70)
bt.insert(60)
bt.insert(80)

print("Inorder traversal:", bt.inorder_traversal())
print("Preorder traversal:", bt.preorder_traversal())
print("Postorder traversal:", bt.postorder_traversal())

bt.delete(20)
print("Inorder traversal after deleting 20:", bt.inorder_traversal())

bt.delete(30)
print("Inorder traversal after deleting 30:", bt.inorder_traversal())

bt.delete(50)
print("Inorder traversal after deleting 50:", bt.inorder_traversal())
