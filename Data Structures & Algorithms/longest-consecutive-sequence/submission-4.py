class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #inputs: nums, an array of integers
        #output: the longest consecutive sequence of elements that can be formed

        #elements do not have to be consecutive in the original array -> order does not need to be maintained
        #we want to ignore duplicates because we are only worried about consecutive elements
        """for example, if there are two 4's, only one of those is relevant to forming a consecutive sequence. therefore, we can remove duplicates by converting the list to a set"""
        nums_set = set(nums) 
        max_sequence = 0 #no elements in the array -> the max sequence length is 0

        for num in nums_set:
            #we dont want the outer loop to iterate through numbers that are part of the sequence, this is redundant and adds unnecessary time complexity
            #sets enable easy lookup
            if num-1 in nums_set:
                continue
            
            curr_sequence = 1 #the list is not empty because we are in the loop
            current = num 
            #discovering the sequence
            while current+1 in nums_set:
                curr_sequence+=1
                current = current+1
            
            if curr_sequence > max_sequence:
                max_sequence = curr_sequence
            
        return max_sequence

