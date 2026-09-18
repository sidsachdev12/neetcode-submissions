public class Solution {
    public void BackTrack(int index, int sum, List<int> arr, int[] nums, int target, List<List<int>> res) {
        if (index >= nums.Count() || sum > target) {
            return;
        } 

        if (sum == target) {
            List<int> copy = new(arr);
            res.Add(copy);
            return;
        }

        arr.Add(nums[index]);
        this.BackTrack(index, sum + nums[index], arr, nums, target, res);

        arr.RemoveAt(arr.Count - 1);
        this.BackTrack(index + 1, sum, arr, nums, target, res);

        return;
    }
    public List<List<int>> CombinationSum(int[] nums, int target) {
        List<List<int>> res = new();
        List<int> arr = new();
        // int sum = 0;

        this.BackTrack(0, 0, arr, nums, target, res);

        return res;
    }
}
