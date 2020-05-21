

def is_palindrome(s: str) -> bool:
    if len(s) < 2:
        return True
    s = s.lower()
    low = 0
    high = len(s) - 1
    while low < high:
        # check if chars are alphanumeric
        while not s[low].isalnum():
            low += 1
        while not s[high].isalnum():
            high -= 1
        print(low, high, s[low], s[high])
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True


my_str = "A man, a plan, a canal: Panama"
print(is_palindrome(my_str))
