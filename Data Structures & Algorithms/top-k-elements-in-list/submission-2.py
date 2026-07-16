class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #initialize a dictionary that will maintain frequencies
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        #this gives us the values as the frequencies and the key as the numbers
        '''now, we want to sort based on frequency (ie, sort the values) BUT we need to keep
        the numbers (keys) associated, because at the end we need to extract the top k most
        frequent numbers (keys). Therefore, we sort the keys and values together.'''
        
        items = list(freq.items()) #this extracts the key and value pairs in the dictionary and saves them as a list
        '''each key-value pair from the dictionary becomes a tuple. for ex:
        {2:2,...} becomes (2,2). we want to sort based on the value (the frequency), so in 
        the tuple representation that is the second element of the tuple. we also want to sort
        in reverse order (instead of ascending ==> descending because we want the top elements at the top)'''
        items.sort(key = lambda x : x[1], reverse = True) 

        #items is now sorted
        result = []
        for element in items[:k]:
            result.append(element[0])
        
        return result


