class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = []
        max_product = 1
        
        for num in nums:
            max_product *= num
            
        
        for index in range(len(nums)):
            ans.append(max_product/nums[index])

        return ans 
