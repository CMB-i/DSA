class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix, suffix = 0, 0
        for i in range(0, len(nums)):
            suffix += nums[i]
        for i in range(0, len(nums)):
            suffix -= nums[i]
            if prefix == suffix:
                return i
            prefix +=nums[i]
        return -1
