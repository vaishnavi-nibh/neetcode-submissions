class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #maintain the list of elements we already saw
        seen = set()

        #iterate through the list
        for num in nums:
            #for each num, check if we've "seen it" already by checking if its seen (seen does not have duplicates because it is a set)
            if num not in seen:
                seen.add(num)
            else: #if the num is in seen, that means it is a duplicate
                return True
        
        return False