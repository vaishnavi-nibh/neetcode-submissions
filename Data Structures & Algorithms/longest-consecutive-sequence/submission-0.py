class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) #turn it into a set to remove duplicates, we nly care ab relationship
        max_length = 0

        for num in nums_set:
            subsequence = 1
            if num - 1 in nums_set:
                continue

            current_num = num
            while current_num + 1 in nums_set:
                subsequence += 1
                current_num = current_num+1

            if subsequence > max_length: 
                max_length = subsequence

        return max_length

