class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #think of the target as 0
        #we iterate through the nums array: then for each index, we see does -1 * times that element exist
        '''in other words, we break it down to a two sum problem: 
        so for each number we are observing, we check, what is -1* that number: this becomes the target
        we then check if in the rest of the array for the two numbers that equal that target'''

        output = []
        #edge case: if the length of nums is less than 3 than there is inherently no valid triplet
        if len(nums) < 3:
            return output

        #note: we are returning VALUES not indices: therefore, we dont need to preserve position/order
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue #go to the next iteration of the loop

            left = i+1 #representing everything to the right of i
            target = -1 * sorted_nums[i]
            right = len(sorted_nums) - 1 
            #it helps to define the right pointer so we can use the strat of narrowing our search window by moving pointers
            
            '''consider the case where we are in the last iteration of i: so for nums length 4
            i = 3, then left = 4 (which is technically out of bounds), but right = 4-1 = 3, so the 
            while loop never even iterates which is why we dont get an error because we dont attempt to
            access something out of bounds'''

            while left < right:
                if sorted_nums[right] + sorted_nums[left] == target:
                    output.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    #but we still need to increment it anyways
                    left += 1
                    right -= 1
                    '''skip the duplicate number:
                    in the case that both sides are duplicates, rest of subwindow stays exactly the same lol unnecessary
                    in the case that only one side is duplicate, well we already found the corresponding solution that = target for that number
                    so if there isnt a duplicate on the other side, that means no other number is viable with this number''' 
                    while left < right and sorted_nums[left] == sorted_nums[left-1]:
                        left += 1 
                    while left < right and sorted_nums[right] == sorted_nums[right+1]:
                        right -= 1
                elif sorted_nums[right] + sorted_nums[left] < target:
                    left += 1
                else:
                    right -= 1
            
        return output

