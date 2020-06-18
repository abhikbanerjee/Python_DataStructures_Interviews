from typing import List


# Generate all possible paranthesis combination given the number of paranthesis - LC 22
def generateParenthesis(n: int) -> List[str]:
	def gen_paran_helper(current_str: str, final_list: List[str], open_count, close_count, max_str):
		if len(current_str) == max_str * 2:
			final_list.append(current_str)
			return
		if open_count < max_str:
			gen_paran_helper(current_str + "(", final_list, open_count + 1, close_count, max_str)
		if close_count < open_count:
			gen_paran_helper(current_str + ")", final_list, open_count, close_count + 1, max_str)

	# return final_list

	final_list = []
	gen_paran_helper("", final_list, 0, 0, n)
	return final_list


print(generateParenthesis(3))