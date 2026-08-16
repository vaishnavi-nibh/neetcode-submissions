class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #each anagram should be identified by its "canonical" representation, which is the sorted version of each word
        #lets maintain a dictionary, where each unique key in the dictionary is the sorted version of each word. for each word in the list, sort it, check if its in the dict, if it is add the word to that sorted representation's values, if its not make a new key and add the current word there

        groups = {}
        for word in strs:
            sorted_word = "".join(sorted(word)) #recall, strings are immutable, so you can't just sort it in place. call sorted(words) and then join back the individually sorted characters
            if sorted_word not in groups:
                groups[sorted_word] = []
            
            groups[sorted_word].append(word)

        #at this point, we have the groups and their corresponding lists
        output = []
        for val in groups.values():
            output.append(val)
        
        return output