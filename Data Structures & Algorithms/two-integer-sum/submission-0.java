class Solution {
    public int[] twoSum(int[] nums, int target) {
        java.util.HashMap<Integer, Integer> dict = new java.util.HashMap<>(); 
        //we are making a hash map, where the key is the number
        //the value is the index of the number

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int numToCheck = target - num;
            if (dict.containsKey(numToCheck)) {
                int index = dict.get(numToCheck); //getting the value (index) at that key
                if (i <= index) {
                    return new int[] {i, index};
                }
                else {
                    return new int[] {index, i};
                }
            }
            dict.put(num, i);
        }

        return null;
    }
}
