class Solution:
    def validStrings(self, n: int) -> List[str]:
        # Recursion
        result = []
    
        def backtrack(current):
            if len(current) == n:
                result.append(current)
                return
            
            # Always try adding '1'
            backtrack(current + "1")
            
            # Only add '0' if the last character is not '0'
            if not current or current[-1] != '0':
                backtrack(current + "0")
        
        backtrack("")
        return result