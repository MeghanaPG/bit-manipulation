class Solution:
    def numSteps(self, s: str) -> int:
        # we will keep performing the below operations 
        # until we get decimal number 1 
        # read str from right to left 
        decimal_num = int(s,2)
        steps = 0

        while decimal_num != 1:
            if decimal_num % 2 == 0:
                decimal_num //= 2 
                steps += 1
            else:
                decimal_num += 1 
                steps += 1  
        return steps 

