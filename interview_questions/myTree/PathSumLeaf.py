from interview_questions.myTree.TreeNode import MyTreeNode


def has_path_sum(self, root: MyTreeNode, sum_value: int) -> bool:
	if not root:
		return False
	left_found, right_found = False, False
	if root.left:
		left_found = self.hasPathSum(root.left, sum_value - root.val)
	if root.right:
		right_found = self.hasPathSum(root.right, sum_value - root.val)
	# check if its the leaf node
	if root.left is None and root.right is None and root.val == sum_value:
		return True
	return left_found or right_found
