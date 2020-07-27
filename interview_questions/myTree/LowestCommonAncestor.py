from interview_questions.myTree import TreeNode

def lowest_common_ancestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

	# base case if root is None
	if root is None:
		return None

	# If either p or q matches with root's key, report
	#  the presence by returning root (Note that if a key is
	#  ancestor of other, then the ancestor key becomes LCA
	if root.val == p.val or root.val == q.val:
		return root

	# Look for keys in left and right subtrees
	left_lca = lowest_common_ancestor(root.left, p, q)
	right_lca = lowest_common_ancestor(root.right, p, q)

	# If both of the above calls return Non - NULL, then one key
	# is present in one subtree and other is present in other,
	# So this node is the LCA
	if left_lca and right_lca:
		return root

	# Otherwise check if left subtree or right subtree is LCA
	return left_lca if left_lca is not None else right_lca

root = TreeNode()
lowest_common_ancestor(root, root.left, root.right)