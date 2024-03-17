import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] twoSum(int[] nums, int target) {   
        int result[] = new int[2];
        HashMap<Integer, Integer> indices = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
        
            if (indices.containsKey(target - nums[i])) {
                result[0] = i;
                result[1] = indices.get(target - nums[i]);
            }
            indices.put(nums[i], i);
        }
        return result;
    }
}