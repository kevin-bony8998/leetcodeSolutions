class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productsFromLeft = [1]
        productsFromRight = []
        res = []
        prodFromLeft = 1
        prodFromRight = 1
        
        for idx in range(len(nums)):
            prodFromLeft *= nums[idx]
            productsFromLeft.append(prodFromLeft)
        
        for idx in range(len(nums) - 1, -1, -1):
            prodFromRight *= nums[idx]
            productsFromRight.append(prodFromRight)
        
        productsFromRight = productsFromRight[::-1]
        productsFromRight.append(1)
        
        for idx in range(len(nums)):
            num = nums[idx]
            ans = productsFromLeft[idx] * productsFromRight[idx + 1]
            res.append(ans)
        return res