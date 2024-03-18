import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        

        Arrays.sort(candidates);
        
        final List<List<Integer>> result = new ArrayList<>();
        
        // Recursively find the unique combinations that add up to the target
        class Recurse {
            void recurse(int i, int currentSum, ArrayList currentCombination) {
                // Terminal success state
                if (currentSum == target) {
                    result.add(new ArrayList(currentCombination));             
                    return;
                }

                // Terminal failure state
                if (i == candidates.length || currentSum > target) {
                    return;
                }
                
                // Include the current element and potentially more
                currentCombination.add(candidates[i]);
                recurse(i + 1, currentSum + candidates[i], currentCombination);
                currentCombination.remove(currentCombination.size() - 1);

                while (i < candidates.length - 1 && candidates[i] == candidates[i + 1]) {
                    i += 1;
                }

                recurse(i + 1, currentSum, currentCombination);
                return;
            }
        }

        Recurse recursion = new Recurse();
        recursion.recurse(0, 0, new ArrayList());
        return result;
    }
}