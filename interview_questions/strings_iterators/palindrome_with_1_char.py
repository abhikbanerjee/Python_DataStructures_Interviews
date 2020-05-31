

def valid_palindrome(s: str) -> bool:
    if len(s) < 3:
        return True
    low = 0
    high = len(s) - 1
    has_seen_once = False
    while high > low:
        if s[low] == s[high]:
            low += 1
            high -= 1
        elif s[low + 1] == s[high] and not has_seen_once:
            low += 2
            high -= 1
            has_seen_once = True
        elif s[low] == s[high - 1] and not has_seen_once:
            low += 1
            high -= 2
            has_seen_once = True
        else:
            return False
    return True

str_palin = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"

print(valid_palindrome(str_palin))