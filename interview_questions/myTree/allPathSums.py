from typing import List
from interview_questions.myTree.TreeNode import MyTreeNode


def pathSum(self, root: MyTreeNode, sum: int) -> List[List[int]]:
    if root is None:
        return []
    final_list = []

    def path_sum_list(node :MyTreeNode, sum: int, running_list: List[int]):
        if node is None:
            return
        path_sum_list(node.left, sum -node.val, running_list + [node.val])
        path_sum_list(node.right, sum -node.val, running_list + [node.val])
        if node.left is None and node.right is None and node.val == sum:
            # leaf node and the sum matches we append to the final list
            final_list.append(running_list[: ] +[node.val])

    path_sum_list(root, sum, [])
    return final_list