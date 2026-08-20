class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #one level of duplication where in the outer loop, we use the same element as the candidate for starting a triplet (this is managed by the outer loop (for loop))
        #another level of duplication is if there are repeats within the subwindow ()
        #so first we sort nums
        nums.sort() #this is sorting it in place, so we don't re-store it
        #define an output list, which is what we return
        output = []
        #outer for loop handles the current element we are looking at, we are attempting to find all valid triplets that can be formed from this current element with the subwindow to its right
        for i, num in enumerate(nums):
            #skipping revisiting the same candidate numbers which we are using to discovery triplets
            #remember it is sorted
            if i > 0 and num == nums[i-1]:
                continue #go to the next element

            #if it is not the same number, we can begin exploring for that number, other numbers that form valid triplets

            current_elem = num
            target = -1 * current_elem

            #defining the search window using two pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == target:
                    output.append([num, nums[left], nums[right]])

                    #updating the search window
                    left += 1
                    right -= 1

                    #but now we have to handle the potential for duplicates within the search window
                    while left < right and nums[left] == nums[left - 1]:
                        #skip it because we already explored it via the prev left
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        #if its the same, skip it because we already epxlored this via the prev right
                        right -= 1
                
                #now handling the case where it doesn't sum to the target: 
                if nums[left] + nums[right] < target:
                    left += 1 #left is the smaller side so increase that
                
                elif nums[left] + nums[right] > target:
                    right -=1 #right is the larger side, so decrease that

        return output
            