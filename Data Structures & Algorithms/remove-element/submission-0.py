class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #we use two pointers
        #i searches through the array
        #j maintains the place where the next non-val should go
        #essentially, everything to the left of j is a "valid" window, in the sense that it will ultimately contain the non-vals
        #therefore the value of j represents the number of non-vals
        j = 0
        for i, num in enumerate(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        
        return j
            
            

            
            