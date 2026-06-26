class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //making the blank Hashmap, which will contain sorted version of words, and list of the actual words
        java.util.HashMap<String, List<String>> wordMap = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            char[] charArray = strs[i].toCharArray(); //we convert each word in the string array to an array of characters, so that we can sort it
            java.util.Arrays.sort(charArray); //now we can sort the charArray (a word)
            String stringKey = new String(charArray);
            if (!wordMap.containsKey(stringKey)) { //if the sorted word doesn't exist as a Key, that marks a new anagram type
                wordMap.put(stringKey, new ArrayList<>());
            }
            //and then we add the current word we're looking at to the list for that key
            wordMap.get(stringKey).add(strs[i]);
        }
        return new ArrayList<>(wordMap.values());
    }
}
