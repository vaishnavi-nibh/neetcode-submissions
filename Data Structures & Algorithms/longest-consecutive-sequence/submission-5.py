class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums) #set removes duplicates and enables easy look ups

        #we want to initialize the max_sequence length to 0, for example, in the case our array has no elements
        max_sequence = 0

    
        for num in nums:
            #check if the preceding element to this element is in the array, then don't start the search from this element --> converting to a set lets us do this easy "in" look-up
            if num - 1 in nums:
                continue
                #skip this element
            
            curr_seq = 1 #because there is at least one element in the array because we are here
            current = num
            while current+1 in nums:
                curr_seq += 1
                current += 1
            
            if curr_seq > max_sequence:
                max_sequence = curr_seq
        
        return max_sequence
