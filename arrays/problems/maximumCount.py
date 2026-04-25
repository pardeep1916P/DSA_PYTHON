from bisect import bisect_left, bisect_right

class Solution:

    """
    Maximum Count of Positive or Negative Integers — Binary Search (Optimal Solution)

    Approach:
    - Array is sorted.
    - Use binary search to find:
          • First index of 0 → gives count of negatives
          • Last index of 0 → helps compute positives
    - Compute:
          • neg = index of first 0
          • pos = total length - index after last 0
    - Return max of both.

    Example:
        nums = [-2,-1,-1,1,2,3]
        neg = 3
        pos = 3
        result = 3

    Time  : O(log n) — binary search
    Space : O(1)

    Note:
    - bisect_left → first occurrence of 0
    - bisect_right → position after last 0
    """

    def maximumCount(self, nums: List[int]) -> int:

        # Count of negative numbers
        neg = bisect_left(nums, 0)

        # Count of positive numbers
        pos = len(nums) - bisect_right(nums, 0)

        return max(pos, neg)