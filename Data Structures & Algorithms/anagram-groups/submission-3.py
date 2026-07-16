class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a dictionary of the sorted words
        groups = {}

        for word in strs:
            word_sorted = "".join(sorted(word)) #this will serve as the key
            '''when we sort the word, we obtain a list of characters, we then join them
            using an empty string (no space) to put them next to each other, to form
            the sorted representation of the word'''
            if word_sorted not in groups: #this is a better more efficient way of doing it
                groups[word_sorted] = [] #make a new key because the sorted representation is a new one
            groups[word_sorted].append(word) #adding the word to its identifying key
            
        return list(groups.values())