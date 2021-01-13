# Node Depth
# Example:
# Tree:
#         10
#      4     15
#    2  3  13  22
#
# Sum of levels = 10

# ==============================================================

# O(N) Time | O(H) Space

def nodeDepth(tree):
    stack = [{"node": tree, "depth": 0}]
    depthSum = 0
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        depthSum += depth
        stack.append({"node": node.left, "depth": depth+1})
        stack.append({"node": node.right, "depth": depth+1})
    return depthSum

# ==============================================================

# O(N) Time | O(H) Space

def nodeDepth(tree, depth=0):
    if tree is None:
        return 0
    return depth + nodeDepth(tree.left, depth+1) + nodeDepth(tree.right, depth+1)
