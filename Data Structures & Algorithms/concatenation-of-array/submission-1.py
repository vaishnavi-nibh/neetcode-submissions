class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        nums_copy = nums

        ans = nums + nums_copy
        return ans