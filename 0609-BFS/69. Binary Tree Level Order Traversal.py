class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """

    def levelOrder(self, root):
        result = []
        if root is None:
            return result
        q = [root]

        while len(q) > 0:
            new_q = []
            result.append([n.val for n in q])
            for i in q:
                if i.left is not None:
                    new_q.append(i.left)
                if i.right is not None:
                    new_q.append(i.right)
            q = new_q
        return result