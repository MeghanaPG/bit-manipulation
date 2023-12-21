class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        
        return res 
