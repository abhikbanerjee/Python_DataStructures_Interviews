from typing import List


# Remove All Adjacent Duplicates in String - LC:1047
def remove_duplicates(S: str) -> str:
        if len(S) < 2:
            return S
        str_stk = []
        for ch in S:
            if len(str_stk) > 0 and str_stk[-1] == ch:
                # pop the last element because its duplicate
                str_stk.pop()
            else:
                # append the element to the list
                str_stk.append(ch)
        return "".join(str_stk)


s = "abbaca"
print(remove_duplicates(s))
