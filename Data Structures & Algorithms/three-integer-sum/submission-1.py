class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array/list:
        nums.sort() #in place sorting
        output = []

        for i in range(len(nums)):
            #handling the case where the outer value is a duplicate (no need to rediscover the same tuple)
            if i > 0 and nums[i] == nums[i-1]:
                continue #go to the next outer iteration of i

            #defining the target
            target = -1 * nums[i]
            #defining search space, start one pointer the left of current/fixed element and another at the end of the list
            left = i + 1
            right = len(nums) - 1

            #while they don't cross each other
            while left < right:
                if nums[left] + nums[right] == target:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target: 
                    left += 1 
                else:
                    right -= 1
                
        return output

            
            
