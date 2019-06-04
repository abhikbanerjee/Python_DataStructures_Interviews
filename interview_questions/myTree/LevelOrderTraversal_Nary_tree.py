from typing import List
from collections import deque


# level order traversal for a N-ary Tree
def levelOrder(root: 'Node') -> List[List[int]]:
    if root is None:
        return []
    result = []
    level_queue = deque()
    level_queue.append(root)
    while len(level_queue)>0:
        level_reset_queue = []
        for i in range(0, len(level_queue)):
            elem_node = level_queue.popleft()
            level_reset_queue.append(elem_node.val)
            for child in elem_node.children:
                level_queue.append(child)
        result.append(level_reset_queue)
    return result