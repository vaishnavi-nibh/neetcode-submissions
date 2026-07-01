class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first initialize a frequency dictionary, we want to keep track of a number and its frequency

        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1 #if not a key value, add it and initialize its frequency to 1
            else:
                freq[num] += 1 #if exists as a value, increment its frequency count
        
        num_freq = list(freq.items())
        num_freq.sort(key = lambda pair: pair[1], reverse = True)

        elements = []
        for pair in num_freq[:k]: #the loop should only iterate through the top k frequent pairs in our ordered list
            elements.append(pair[0])
        
        return elements


