class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we want to update the pointer pointing to the shorter wall
        #because this is the true constraint on the area
        #the larger wall is not the constraint on the area

        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            current_area = min(heights[left], heights[right]) * (right - left)
            if current_area > max_area:
                max_area = current_area
            
            if heights[left] <= heights[right]:
                left += 1
            else: 
                right -= 1

        return max_area