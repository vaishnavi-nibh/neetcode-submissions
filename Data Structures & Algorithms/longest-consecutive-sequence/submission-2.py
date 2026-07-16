class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #but we dont care about duplicates in forming the longest consecutive sequence
        #this is because a consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous

        #for example: if we have 2, 3, 4, 4, 5 ==> we can disregard the second 4
        #the first 4 can still form a valid sequence: either 2,3,4 or 4,5 (where 2,3,4 is the bigger one)

        nums_set = set(nums)

        #remember, we want to avoid repeating the same elements of the subsequence...
        #so for example: if 2,3,4 is a subsequence that means 3 is part of the 2,3,4 subsequence
        #traversing 3,4 separately is therefore a redundant subsequence that adds additional time wastage

        #we have to consider the case where there is nothing in the set!!!
        max_subsequence = 0

        for num in nums_set:
            if num - 1 in nums_set:  #so that means that the subsequence can be started by some lower element
                continue
            
            #we want to store current = num because we dont want to change num for the outerloop iteration
            current = num

            '''NOTE: we initialize current sequence INSIDE the loop because it is handling
            the sequence length of our current iterations sequence'''
            curr_sequence = 1
            #we check for consecutive elements in the list
            while current + 1 in nums_set:
                curr_sequence += 1
                current = current+1

            if curr_sequence > max_subsequence:
                max_subsequence = curr_sequence
        
        return max_subsequence
            
            