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


# 557. Reverse Words in a String III
def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    word_lists = s.split(' ')
    result=[]
    for word in word_lists:
        temp = list(word)
        l = 0
        r= len(temp) - 1
        while l<r:
            temp[l], temp[r] = temp[r], temp[l]
            l+=1
            r-=1
        result.append(''.join(temp))
    print(' '.join(result))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "God Ding"
    reverseWords(s)
