from typing import List


# Generate Pascal's triangle for a given number of rows - LC:118
def generate_pascal_traingle(numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result_set = []
        rows = [1]
        result_set.append(rows)
        for i in range(1, numRows):
            curr_row = []
            curr_row.append(1)
            prev_row = result_set[i-1]
            for j in range(1,i):
                curr_row.append(prev_row[j]+prev_row[j-1])
            curr_row.append(1)
            result_set.append(curr_row)
        return result_set


print(generate_pascal_traingle(7))