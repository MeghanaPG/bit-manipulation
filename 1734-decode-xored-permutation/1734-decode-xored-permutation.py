class Solution:
    def decode(self, A: List[int]) -> List[int]:
        first = reduce(ixor, A[::-2] + list(range(len(A) + 2)))
        return list(accumulate([first] + A, ixor))