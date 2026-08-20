class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #midpoint is half of the array's length
        left = 0
        right = len(nums) - 1

        #we are given that the array is sorted, so we can directly compare values
        
        while left <= right: 
            midpoint = left + (right - left) // 2
            #or you can just do standard midpoint formula ==> left + right // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                left = midpoint + 1
            elif nums[midpoint] > target:
                right = midpoint - 1
        
        #if the loop is done and we haven't returned yet, return -1
        return -1