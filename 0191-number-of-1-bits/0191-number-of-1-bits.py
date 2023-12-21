class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time Complexity: O(32) -> O(1)
        res = 0 

        while n:
            res += n % 2 
            # shift by 1 
            n = n >> 1 
        return res 
