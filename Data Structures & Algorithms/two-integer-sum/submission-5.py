class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #when we are looking in the hashmap that preserves the numbers we've seen thus far and their indices, we want to easily access the value (to check if the complement exists).therefore, we will make the number the key and the index the corresponding value

        seen = {}

        #note, we are returning the answer with the smaller index first

        #let's iterate through nums and for each num, check if its complement (target - num) is in the seen dictionary. this is why the number being the key helps because we can easily look for the complement. we are assuming that every input has exactly one pair of indices i and j that satisfy the condition. therefore, once we find the complement, we get the index (the associated value with that key) and return the index and the current index. 
        #after visiting each num, we add it to the seen dictionary. this allows us to guarantee that the complement we are looking for has the smaller index, meeting the "return the answer with the smaller index first" condition

        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                comp_index = seen[complement] #getting the associated index
                return [comp_index, index]
            seen[num] = index