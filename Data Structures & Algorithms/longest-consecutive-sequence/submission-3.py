class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #we don't even need to sort it!!! because we can use set membership to check if the consecutive elements are making up a sequence

        #convert the list to a set
        set_nums = set(nums)
        max_length = 0

        for num in set_nums:
            if num - 1 in set_nums:
                continue #we only want to start a sequence from its lowest value element
            
            current = num
            curr_length = 1 #it is at least one number (num)
            while current + 1 in set_nums:
                curr_length +=1
                current = current + 1 #exploring the rest of the sequence
            
            if curr_length > max_length:
                max_length = curr_length
        
        return max_length

