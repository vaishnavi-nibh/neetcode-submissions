class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #seen maintains all the elements we've seen so far IN THE SAME ORDER TOO (lists preserve order)
        seen = []

        for index, num in enumerate(nums):
            #this means an element we've explored already plus the current number = target
            if target - num in seen:
                return [seen.index(target - num), index]
            seen.append(num)
            
        