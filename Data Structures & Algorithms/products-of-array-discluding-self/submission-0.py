class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #first we want to compute the left product arrays and right product arrays
        #once we compute these, we iterate through the nums array
        #for each element of the nums array, we retrieve the corresponding element
        #(aka whats at the same index) in the left and right arrays
        #these represent the product of everything to the left of the number
        #and the product of everything to the right of the number
        #we multiply these two, and that is inherently the product of everything BUT
        #the number

        left = [1] * len(nums)
        for i in range(1, len(nums)): #start at index 1 because we already initialized index 0 to be 1 
            left[i] = left[i - 1] * nums[i - 1]
        
        right = [1] * len(nums)
        right[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = left[i] * right[i]
        
        return output
            