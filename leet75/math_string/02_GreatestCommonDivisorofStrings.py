class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        a = []
        size = max(m, n)
        if str1+str2 == str2+str1:
            for i in range(1,size+1):
                if m%i == 0 and n%i == 0:
                    a.append(i)
            L = max(a)
            return str1[0:L]
        else:
            return ''

from math import gcd
class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        else:
            return str1[0:gcd(len(str1), len(str2))]


#learned how to place hte right indentations
#gcd resucrive way

def gcd_recursive(a, b):
    if b==0:
        return a
    return gcd_recursive(b, a%b)