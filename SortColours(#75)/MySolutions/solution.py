from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        idx = 0
        keys = [0, 1, 2]
        for key in keys:
            while counts[key] != 0:
                nums[idx] = key
                counts[key] -= 1
                idx += 1