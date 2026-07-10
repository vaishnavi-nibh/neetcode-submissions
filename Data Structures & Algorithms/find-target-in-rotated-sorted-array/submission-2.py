class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            '''use the understanding of the rotation point (where it goes from max to min)
            to treat one side of the array as sorted, and the other side of the array as unsorted
            (because the unsorted side includes the rotation)'''

            #case where we identified the target
            if target == nums[mid]:
                return mid
            
            #case where the right subarray is sorted:
            if nums[mid] <= nums[right]:
                #if the number is confirmed in this range (between mid and right boundary)
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                #if target is outside of the range of this boundary
                else: #not in this component, means its in the other component
                    right = mid - 1
            
            #case where the left subarray is sorted, and not the right:
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                #if target is not between this range
                else: #not in the sorted range, so again in the other component
                    left = mid+1

        return -1          
