class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        i, j = 0, len(l)-1
        while j>i:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        return " ".join(l)

# .Split() carry absolutely: .split() return the args wihtout all the whitespaces:
# It splits on whitespace, automatically discards leading/trailing spaces, and collapses multiple consecutive spaces into single separators
# GOAT .split()

#now without split
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = 0
        n = len(s)
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
            start = i
            while i < n and s[i] != ' ':
                i += 1
            words.append(s[start:i])
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        return " ".join(words)