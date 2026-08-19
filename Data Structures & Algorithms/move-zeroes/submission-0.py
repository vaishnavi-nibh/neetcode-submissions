class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        #2 pointer approach
        i = 0
        #both the pointers start at the beginning of nums
        
        for j in range(len(nums)):
            #if j is at a non-zero and i is at a zero 
            if nums[j] != 0 and nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            #if j is at a zero --> j just proceeds ahead (action is only taken when j is a non-zero). this proceeding ahead is managed by the for loop. 
            if nums[i] != 0:
                i += 1
        
        return nums