class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we want to return the indices for which the corresponding numbers = the target

        #maintain a dictionary that maintains each number we've seen
        seen = {}

        #we want to check, is the target - the current number (value) present in our dictionary
        #we want the numbers (value) to be the key
        #we want the index to be the corresponding dictionary value

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            