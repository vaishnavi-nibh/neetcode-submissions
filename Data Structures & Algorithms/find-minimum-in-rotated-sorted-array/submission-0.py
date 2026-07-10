class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        #while the window is valid and the pointers don't cross each other
        while left < right:
            #calculate the midpoint for the window
            mid = left + (right - left) // 2

            #compare the midpoint value to the rightmost value in the window
            '''case 1: nums[mid] is greater than nums[right] ==> this means that
            somewhere in the window, there is a decrease. it doesnt necessarily mean
            that nums[mid] is the max, but for example something to the right of 
            nums[mid] could be the absolute maximum and then the minimum is to the right
            of that. therefore if nums[mid] > nums[right], we should explore the right window'''
            if nums[mid] > nums[right]:
                left = mid + 1
                
            '''case 2: nums[mid] is less than nums[right] ==> because the array is in sorted order, 
            if nums[right] is greater than nums[mid], that means there is only increasing behavior between
            the midpoint and the right most value. therefore, there is no chance for the midpoint to 
            exist in this window. so we have to explore the left window'''
            if nums[mid] <= nums[right]:
                right = mid

        return nums[left]

        