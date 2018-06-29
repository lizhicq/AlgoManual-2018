class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:

    def serialize(self, root):
        """
        @param root: An object of TreeNode, denote the root of the binary tree.
        This method will be invoked first, you should design your own algorithm
        to serialize a binary tree which denote by a root node to a string which
        can be easily deserialized by your own "deserialize" method later.
        """
        if root == None:
            return "{}"
        que = [root]
        for i in range(len(que)):
            if que[i] != None:
                que.append(que[i].left)
                que.append(que[i].right)
        ser = ""
        for x in range(len(que)):
            ser += "#" if que[x] is None else "{}".format(que[x].val)
            if x != len(que) - 1:
                ser += ","
        return "{" + ser + "}"

    def deserialize(self, data):
        """
        @param data: A string serialized by your serialize method.
        This method will be invoked second, the argument data is what exactly
        you serialized at method "serialize", that means the data is not given by
        system, it's given by your own serialize method. So the format of data is
        designed by yourself, and deserialize it here as you serialize it in
        "serialize" method.
        """
        if data == "{}":
            return None
        data = data[1:-1].split(',') # remove {
        root = TreeNode(data[0])
        que = [root]
        index = 0
        is_left = True
        for i in range(1, len(data)):
            if data[i] != '#':
                node = TreeNode(data[i])
                if is_left:
                    que[index].left = node
                else:
                    que[index].right = node
                que.append(node)
            if is_left is False:
                index += 1
            is_left = not is_left
        return root


from collections import deque
