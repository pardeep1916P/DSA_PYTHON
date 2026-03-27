class Solution:

    """
    Find Pivot Index — Prefix Sum (Optimal Solution)

    Approach:
    - Compute total sum of the array.
    - Maintain a running left sum (l).
    - For each index i:
          • Right sum = total - nums[i] - l
          • If left sum == right sum → pivot found
    - Update left sum as you move forward.

    Time  : O(n) — single pass after sum
    Space : O(1) — constant extra space

    Note:
    - Avoids using extra arrays (prefix/suffix).
    - Most efficient approach for this problem.
    """

    def pivotIndex(self, nums: List[int]) -> int:

        if len(nums) == 0: return -1

        total = sum(nums)
        l = 0  # left sum

        for i in range(len(nums)):

            # Check if current index is pivot
            if l == total - nums[i] - l: return i

            # Update left sum
            l += nums[i]

        return -1