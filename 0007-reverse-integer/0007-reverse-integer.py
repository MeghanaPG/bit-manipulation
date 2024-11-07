class Solution:
    def reverse(self, x: int) -> int:
        res = 0 
        if x > 0:
            num = str(x)
            rev_num = int(num[::-1])
            res =  rev_num
        else:
            num = str(abs(x))
            rev_num = int(num[::-1])
            res = - rev_num
        
        if res > -2 ** 31 and res < 2**31:
            return res
        else:
            return 0 


            