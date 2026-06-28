class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = [0]*(len(gain)+1)
        for i in range(1, len(gain)+1):
              ans[i] = ans[i-1] + gain[i-1]
        return max(ans)
