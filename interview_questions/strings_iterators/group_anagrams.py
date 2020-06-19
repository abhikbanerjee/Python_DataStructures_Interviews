
# Group Anagrams together from a list of strings - LC:49
def group_anagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        import collections
        anagrams_dicti = dict()
        for word in strs:
            sorted_str = "".join(sorted(word))
            if sorted_str not in anagrams_dicti.keys():
                # insert a list of this word in the values of the dict
                str_values = list()
                str_values.append(word)
                anagrams_dicti[sorted_str] = str_values
            else:
                str_values = anagrams_dicti[sorted_str]
                str_values.append(word)
                anagrams_dicti[sorted_str] = str_values
        return list(anagrams_dicti.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))




