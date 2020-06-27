

# Find the Least Common Ancestor in a Binary Search Tree - LC:235
def lowest_common_ancestor_bst(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    parent_val = root.val
    pval = p.val
    qval = q.val
    if pval >parent_val and qval >parent_val:
        # move to the right subtree
        return self.lowestCommonAncestor(root.right, p, q)
    elif pval <parent_val and qval <parent_val:
        # move to the left subtree
        return self.lowestCommonAncestor(root.left, p, q)
    else:
        # We have found the split point
        return root
