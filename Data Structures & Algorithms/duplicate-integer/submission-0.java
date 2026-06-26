class Solution {
    public boolean hasDuplicate(int[] nums) {
        //Java Generics don't allow primitive types -- so use wrapper class
        java.util.Set<Integer> setNums = new java.util.HashSet<>(); //we cannot just pass in nums, that's not how it works
        for (int num : nums) {
            if (setNums.contains(num)) {
                return true;
            }
            else {
                setNums.add(num);
            }
        }

        return false;
    }
}
