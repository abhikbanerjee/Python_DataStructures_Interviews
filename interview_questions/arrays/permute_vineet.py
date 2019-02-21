

def permute(A, i, diff_perm):
	if i == len(A):
		diff_perm.append(''.join(A))
	else:
		for k in range(i, len(A)):
			A[i], A[k] = A[k], A[i]
			permute(A, i+1, diff_perm)
			A[i], A[k] = A[k], A[i]
	return


diff_perm = []
permute(list("abx"),0, diff_perm)
print(len(diff_perm))