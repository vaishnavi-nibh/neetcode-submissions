class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #make a dictionary of the sorted words
        sorted_words = {}

        for word in strs:
            word_sorted = "".join(sorted(word))
            '''when we sort the word, we obtain a list of characters, we then join them
            using an empty string (no space) to put them next to each other, to form
            the sorted representation of the word'''
            if word_sorted in sorted_words: #this checks if it is a key
                sorted_words[word_sorted].append(word)
            else: #if the sorted representation is not an existing key, it is a unique sorted representation
                sorted_words[word_sorted] = [word]
        
        return list(sorted_words.values())