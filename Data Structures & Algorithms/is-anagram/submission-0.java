class Solution {
    public boolean isAnagram(String s, String t) {
        int[] freqArray = new int[28];

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int index = c - 'a';
            freqArray[index]++;
        }

        //then we subtract for the characters in string t
        for (int j = 0; j < t.length(); j++) {
            char c = t.charAt(j);
            int index = c - 'a';
            freqArray[index]--;
        }

        for (int k = 0; k < freqArray.length; k++) {
            if (freqArray[k] != 0) {
                return false;
            }
        }
        return true;
    }
}
