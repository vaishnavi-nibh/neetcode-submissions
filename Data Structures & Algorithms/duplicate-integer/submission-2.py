class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #alternative solution
        distinct_elements = set()
        
        for num in nums:
            if num in distinct_elements:
                return True
            distinct_elements.add(num)
        
        return False