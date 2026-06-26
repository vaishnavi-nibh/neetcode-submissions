class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #true is if the array nums does contain duplicates
        #false is if the array nums does not contain duplicates

        #we can use the set() function to convert the list to a set, because a set removes duplicates
        #if the length of the set is = to the length of the list: return false
        #if the length of the set is not equal to the length of the list (aka) the list is longer
        #return true, because that means the list contains duplicates the set doesn't have

        return len(set(nums)) != len(nums)