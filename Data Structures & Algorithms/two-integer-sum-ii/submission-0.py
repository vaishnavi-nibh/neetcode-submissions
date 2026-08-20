class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #we are given that the array of integers is sorted in non-decreasing order (loosely, increasing order)

        #we want to return the 1-indexed indices

        #because the array is sorted, we can take advantage of relative ordering
        #start a pointer at one end and another pointer at the other end

        left = 0
        right = len(numbers) - 1

        while left <= right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1, right+1]

            if curr_sum < target: #we have to increase the left pointer because right is maximized and only way to increase sum is move the left to a higher number
                left += 1
            elif curr_sum > target:
                right -= 1 #we have to lower the right pointer to a smaller number
            

