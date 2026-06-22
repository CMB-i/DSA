class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size = max(len(word1), len(word2))
        ans = []
        for i in range(size):
            if i<len(word1):
                ans.append(word1[i])
            else:
                pass
            if i<len(word2):
                ans.append(word2[i])
            else:
                pass
        return "".join(ans)
        

#alt 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = ''
        i=j=0
        while i<len(word1) or j<len(word2):
            if i < len(word1):
                r+=word1[i]
                i+=1
            if j<len(word2):
                r+=word2[j]
                j+=1
        return r

# we never use and in the while condiiton as it stop sht eloop at hte smaller sized string