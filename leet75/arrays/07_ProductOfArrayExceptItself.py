class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            ans.append(product)
        return ans

# version 2 reduced tc--0(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = 1
        suffix[len(nums)-1] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])
        return ans

'''
- Division-free product trick: `answer[i] = prefix[i] * suffix[i]` — splits the multiplication instead of dividing out `nums[i]`. Handles zeros naturally, unlike total-product÷element.
- `return` inside a loop exits immediately — can't use it to "hold onto" a value mid-loop.
- Can't assign to an index of an empty list (`x[0] = 1` fails on `x = []`) — pre-size with `[0]*n` or use `.append()`.
- `[] * n` is still `[]` — repeating nothing gives nothing; need `[0] * n` for actual placeholder slots.
- `range(a, b)` excludes `b` — `range(len(nums))` already covers every index automatically; you rarely need to manually type `-1`.
- Backward ranges**: `range(start, stop, -1)` stops *before* `stop` — to include `0`, stop must be `-1`, not `0`.
- Base cases sit at opposite ends**: `prefix[0] = 1` (nothing before start), `suffix[last] = 1` (nothing after end) — can't build both in one forward loop.
- LeetCode doesn't enforce "soft" constraints like "without division" — it only checks correctness/speed. Accepted ≠ "followed the rules."
- Recursion ≠ recurrence — a recurrence relation (`prefix[i]` depends on `prefix[i-1]`) is just reusing prior loop results; no function is calling itself.
'''