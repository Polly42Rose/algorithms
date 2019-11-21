# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.depth = 0

class Solution:
    def bfs(self, nodes, target, node, i):
        if not node:
            return 0

        num_max_depth = 0

        if not node.left and not node.right:
            if node in nodes:
                num_max_depth = 1
        else:
            if node.left:
                i += 1
                left = self.bfs(nodes, target, node.left, i)
                try:
                    num_max_depth += left
                except TypeError:
                    return left
            if node.right:
                i += 1
                right = self.bfs(nodes, target, node.right, i)
                try:
                    num_max_depth += right
                except TypeError:
                    return right
        if num_max_depth == target:
            return node
        return num_max_depth

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        max_depth = 0
        que = [(root, 0)]
        count = 0
        while count < len(que):
            curr = que[count][0]
            curr_depth = que[count][1]
            if curr.left:
                que.append((curr.left, curr_depth + 1))
            if curr.right:
                que.append((curr.right, curr_depth + 1))
            if curr_depth > max_depth:
                max_depth = curr_depth
            count += 1

        num_max_depth = 0
        max_depth_node = set()
        for el in que[::-1]:
            if el[1] == max_depth:
                num_max_depth += 1
                max_depth_node.add(el[0])
            else:
                break

        return self.bfs(max_depth_node, num_max_depth, root, 0)