class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Time Complexity: O(N * log M), where N is the length of nums and M is the maximum value in nums.
        if nums == [0]:
            return 0
        count = 0 
        double = 0
        for x in nums:
            cd = 0 
            while x > 0:
                if x % 2 == 1:
                    count += 1 
                x //= 2 
                cd += 1
            double = max(cd, double)
        return count + (double - 1)