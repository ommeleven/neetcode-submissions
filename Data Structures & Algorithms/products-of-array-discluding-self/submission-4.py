class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = []
        max_product = 1
        
        for index1 in range(len(nums)):
            product = 1
            for index2 in range(len(nums)):
                if index1 != index2:
                    product *= nums[index2]
            
            ans.append(product)
        return ans
            
        
        
