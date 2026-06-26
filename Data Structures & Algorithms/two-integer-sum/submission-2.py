class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #iterate through nums and for each value in the list, compute target-value

        #we may assume that every input has exactly one pair of indices i and j that satisfy

        #maintain a dictionary (hash map) with each visited element and its index
        seen = {}

        for i, num in enumerate(nums):
            val = target - num

            #if the value is already in seen, we've already traversed it and stored its index
            #therefore, its index is smaller than the index of num (because num came after)
            if val in seen:
                return [seen[val], i]
            
            seen[num] = i

        


        