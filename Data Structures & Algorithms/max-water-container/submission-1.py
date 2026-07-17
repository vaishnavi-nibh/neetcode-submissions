class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            if heights[left] <= heights[right]:
                area = heights[left] * width
                left += 1
            else:
                area = heights[right] * width
                right -= 1
            
            if area > max_area:
                max_area = area
        
        return max_area
            