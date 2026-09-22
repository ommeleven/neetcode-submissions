class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = []
        max_product = 1
        
        for num in nums:
            max_product *= num
            
        
        for index in range(len(nums)):
            if nums[index] != 0:
                ans.append(max_product//nums[index])
            else:
                ans.append(0)

        return ans 
