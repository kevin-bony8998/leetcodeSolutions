from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        store = defaultdict(list)
        target = 0
        res = set()
        for idx1 in range(len(nums)):
            num1 = nums[idx1]
            for idx2 in range(idx1 + 1, len(nums)):
                num2 = nums[idx2]
                total = num1 + num2
                store[target - total].append([idx1, idx2])
        # print(store)
        for idx3 in range(len(nums)):
            num3 = nums[idx3]
            if store.get(num3) != None:
                for pair in store[num3]:
                    if pair[0] != idx3 and pair[1] != idx3:
                        res.add(tuple(sorted([nums[pair[0]], nums[pair[1]], num3])))
        return res