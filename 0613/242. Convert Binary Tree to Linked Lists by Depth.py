
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if root is None:
            return []
        from collections import deque
        deck = deque()
        deck.appendleft(root)
        res = []
        dummy = ListNode(-1)
        while len(deck) > 0:
            size = len(deck)
            tmp = dummy
            for i in range(size):
                node = deck.pop()
                tmp.next = ListNode(node.val)
                tmp = tmp.next
                if node.left:
                    deck.appendleft(node.left)
                if node.right:
                    deck.appendleft(node.right)
            res.append(dummy.next)
        return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print Solution().binaryTreeToLists(root)