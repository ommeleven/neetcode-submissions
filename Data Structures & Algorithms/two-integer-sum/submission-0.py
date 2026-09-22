class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indexes = {}

        for index in range(len(nums)):
            indexes[nums[index]] = index


        for index in range(len(nums)):
            y = target - nums[index]
            
            if y in nums: 
                return [index, indexes[y]]
