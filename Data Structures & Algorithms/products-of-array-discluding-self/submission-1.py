class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        #lets make left array first
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1] 
            '''the product calculation for the previous element did not include THAT element
            as per the problem constraints. likewise, the product calculation for this element
            does not include THIS element. however, we still need to include the previous element'''

        #now that the left array is done we will make the right array --> start at the end
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        #now that we have obtained left and right, multiply them together to find the product
        product = []
        for i in range(len(nums)):
            product.append(left[i] * right[i])
        
        return product
        
        