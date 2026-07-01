class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in groups:
                groups[key] = [] #adding the sorted word as a new key and initializing an empty list for it

            #add the current word to its sorted word's list

            groups[key].append(word) #retrieving the list associated with the sorted key and adding the word to that

        return list(groups.values()) #groups.values() obtains all the group lists formed
        #casting them to list() follows the return type 

