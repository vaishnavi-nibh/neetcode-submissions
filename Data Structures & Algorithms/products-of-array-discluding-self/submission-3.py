class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)

        #initializing the left product array
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        #initializing the right product array
        right[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        #making the output product array
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = left[i] * right[i]
        
        return output