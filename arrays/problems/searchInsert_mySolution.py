class Solution:

    """
    Search Insert Position — Linear Scan (Brute Force Solution)

    Approach:
    - Traverse the array from left to right.
    - If the current element equals the target
      OR is greater than the target,
      return the current index.
    - If the loop finishes, the target should be
      inserted at the end of the array.

    Time  : O(n) — scan entire array in worst case
    Space : O(1)

    Note:
    - Works correctly but does not use the sorted
      property of the array.
    - Binary search is the optimal approach.
    """

    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):

            if nums[i] == target or nums[i] > target:
                return i

        return len(nums)