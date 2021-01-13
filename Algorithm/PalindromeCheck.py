# Palindrome Check
# Example:
# String: "abcdcba"
# Answer: True

# ==============================================================

# O(N^2) Time (because string concatenation) | O(N) Space

def isPalindromeCheck_1(string):
    reversedString = ""
    for char in reversed(range(len(string))):
        reversedString += string[char]
    return string == reversedString

# ==============================================================

# O(N) Time | O(N) Space

def isPalindromeCheck_2(string):
    reversedString = []
    for char in reversed(range(len(string))):
        reversedString.append(string[char])
    return string == "".join(reversedString)

# ==============================================================

# O(N) Time | O(N) Space

def isPalindromeCheck_3(string, leftIdx = 0):
    rightIdx = len(string) - 1 - leftIdx
    return True if leftIdx > rightIdx else string[leftIdx] == string[rightIdx] and isPalindromeCheck_3(string, leftIdx+1)

# ==============================================================

# Tail Recursion (but python doesn't support Tail Recursion)
# O(N) Time | O(1) Space (reduce calls in call stack to 1 by replaceing previous call with the new one)

def isPalindromeCheck_4(string, leftIdx = 0):
    rightIdx = len(string) - 1 - leftIdx
    if leftIdx > rightIdx:
        return True
    if string[leftIdx] != string[rightIdx]:
        return False
    return isPalindromeCheck_4(string, leftIdx+1)

# ==============================================================

# O(N) Time | O(1) Space

def isPalindromeCheck_5(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True

print(isPalindromeCheck_5("abcdcba"))
