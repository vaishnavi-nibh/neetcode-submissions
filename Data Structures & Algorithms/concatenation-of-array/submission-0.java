class Solution {
    public int[] getConcatenation(int[] nums) {
        int numsLength = nums.length; //first index for new numbers
        int[] newNums = new int[2 * numsLength];
        for (int i = 0; i < nums.length; i++) { //this copies over the numbers from 0 to numsLength-1
            newNums[i] = nums[i];
        }
        for (int j = 0; j < nums.length; j++) {
            newNums[numsLength] = nums[j];
            numsLength++;
        } 
        return newNums;
    }
}