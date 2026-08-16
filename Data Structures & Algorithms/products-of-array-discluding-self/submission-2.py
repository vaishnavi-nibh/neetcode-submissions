class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #break it into a left and right and then multiply these together
        #left maintains the product of everything to the left of the current index
        left = [0] * len(nums)
        #right maintains the product of everything to the right of the current index
        right = [0] * len(nums)

        #there is nothing to the left of the first element in nums, so index 0 in left is 1
        left[0] = 1
        #there is nothing to the right of the last index
        right[len(nums) - 1] = 1

        #instantiating left:
        #start at index 1 in the left array (not 0) and start at nums index 1
        for index in range(1, len(nums)):
            left[index] = nums[index-1] * left[index-1]
        

        #creating the right array:
        #start at len(nums) -2 because we already set len(nums) - 1th element to 1:
        for index in range(len(nums) - 2, -1, -1):
            right[index] = nums[index+1] * right[index+1]

        #now calculating the product 
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = left[i] * right[i] 
            #left array has product of everything to the left of the number and right array   has product of everything to the right of the number, so by multiplying them we get the overall product of everything but that element

        return output