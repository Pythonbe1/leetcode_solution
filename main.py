# Two pointers
def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    left = 0
    right = len(s) - 1
    s = list(s)
    while left < right:
        while left <= len(s) and s[left].lower() not in vowels:
            left += 1
        while right >= 0 and s[right].lower() not in vowels:
            right -= 1
        if left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    print(s)
    return s





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reverseVowels('Hello')


