

# Valid Palindrome with just 1 character being different - LC:680
def valid_palindrome(s: str) -> bool:
    if len(s) < 3:
        return True

    def is_palin_helper(palin: str, i: int, j: int) -> bool:
        while i <= j:
            if palin[i] != palin[j]:
                return False
            i += 1
            j -= 1
        return True

    low = 0
    high = len(s) - 1
    while low <= high:
        if s[low] != s[high]:
            return is_palin_helper(s, low + 1, high) or is_palin_helper(s, low, high - 1)
        low += 1
        high -= 1
    return True


str_plain = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
str_plain2 = "ebcbbececabbacecbbcbe"
print(valid_palindrome(str_plain))
print(valid_palindrome(str_plain2))