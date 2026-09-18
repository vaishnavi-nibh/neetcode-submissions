class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            
            freq[num] += 1

            if freq[num] > len(nums) / 2:
                return num
