class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # Time Complexity: 
        # Bit Manipulation 
        N = len(nums)

        ans = [None] * N
        count = [0] * 32 
        current = 0 
        roll = 0 
        right = N - 1

        for left in range(N-1, -1, -1):
            for j in range(32):
                if (nums[left] & (1<<j)) > 0:
                    count[j] += 1
                    current |= (1 << j)
            roll |= nums[left]

            while current == roll and left <= right:
                for j in range(32):
                    if (nums[right] & (1<<j)) > 0:
                        count[j] -= 1
                        if count[j] == 0:
                            current ^= (1<<j)
                right -= 1
            
            ans[left] = right - left + 2 
        return ans


