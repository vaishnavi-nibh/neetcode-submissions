class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = [] 
            groups[sorted_word].append(word)
        
        #once we have the anagrams and their sublists in the groups dictionary,lets add them to the output dictionary

        output = []
        for val in groups.values():
            output.append(val)
        
        return output