from typing import List


# Find H-Index such that there are x citations that have atleast h citations and other X-h papers have
# less than h citations  - LC:274
def h_index(citations: List[int]) -> int:
        if citations is None or len(citations) < 1:
            return citations
        if len(citations) < 2:
            return citations[0]
        citations = sorted(citations)
        max_h_index = -1
        for i in reversed(range(0,len(citations))):
            if i!=0 and citations[i] >= len(citations)-i and citations[i] > citations[i-1]:
                max_h_index = citations[i]
        return max_h_index

inp = [3,0,6,1,5]
print(h_index(inp))