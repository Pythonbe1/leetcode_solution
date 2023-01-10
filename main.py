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
    result = []
    for word in word_lists:
        temp = list(word)
        l = 0
        r = len(temp) - 1
        while l < r:
            temp[l], temp[r] = temp[r], temp[l]
            l += 1
            r -= 1
        result.append(''.join(temp))
    print(' '.join(result))


# 832. Flipping an Image

def flipAndInvertImage(image):
    """
    :type image: List[List[int]]
    :rtype: List[List[int]]
    """
    for i in range(len(image)):
        left = 0
        right = len(image[i]) - 1
        while left < right:
            image[i][left], image[i][right] = image[i][right], image[i][left]
            left += 1
            right -= 1
    for j in range(len(image)):
        for k in range(len(image[j])):
            if image[j][k] == 0:
                image[j][k] = 1
            else:
                image[j][k] = 0
    print(image)
    return image

# 2108. Find First Palindromic String in the Array
def firstPalindrome(words):
    """
    :type words: List[str]
    :rtype: str
    """
    for word in words:
        temp = list(word)
        left, right = 0, len(temp)-1
        while left < right:
            temp[left], temp[right] = temp[right], temp[left]
            left += 1
            right -= 1
        if word == ''.join(temp):
            print(word)
            return word
            break
    return ''

# 2000. Reverse Prefix of Word

def reversePrefix(word, ch):
    """
    :type word: str
    :type ch: str
    :rtype: str
    """
    word = list(word)
    left = 0
    try:
        right = word.index(ch)
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        print(''.join(word))
        return ''.join(word)

    except ValueError:
        print(''.join(word))
        return ''.join(word)




if __name__ == '__main__':
    # s = "God Ding"
    # reverseWords(s)
    # image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    # flipAndInvertImage(image)
    # words = ["abc", "car", "ada", "racecar", "cool"]
    # firstPalindrome(words)
    word = "abcdefd"
    ch = "d"
    reversePrefix(word, ch)
