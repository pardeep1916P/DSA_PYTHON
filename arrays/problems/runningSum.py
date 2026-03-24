class Solution:

    """
    Running Sum of 1D Array — In-Place Prefix Sum (Optimal Solution)

    Approach:
    - Traverse the array from index 1 to end.
    - For each index i:
          • Add the previous value nums[i-1] to nums[i].
    - This converts the array into its running sum in-place.

    Example:
        nums = [1,2,3,4]
        → [1,3,6,10]

    Time  : O(n) — single pass
    Space : O(1) — in-place modification

    Note:
    - More space-efficient than creating a new array.
    - Modifies input directly (allowed in this problem).
    """

    def runningSum(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):

            if i != 0:
                nums[i] = nums[i] + nums[i - 1]

        return nums