class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #making a frequency dictionary
        freq = {}

        #iterating through the nums list and updating the frequency dictionary
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        #after we have the updated frequency dictionary, we want to sort by the values in the frequency array (because note, the key corresponds to the number, the freq value corresponds to the frequency). 

        #we are making a list with the frequency values, and then sorting this. this is being stored in sorted_frequencies
        sorted_frequencies = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        #sorted_frequencies is a list, now we want to extract the top k most frequent elements. we said reverse = True, so that means the sorted_frequencies list is in a non-increasing order.
        output = []
        for i in range(k):
            output.append(sorted_frequencies[i][0])
        
        return output