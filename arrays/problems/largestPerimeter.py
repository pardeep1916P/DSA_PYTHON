class Solution:

    """
    Largest Perimeter Triangle — Greedy After Sorting (Optimal Solution)

    Approach:
    - Sort the array in descending order.
    - Check every consecutive triplet:
          • For triangle: a < b + c
      (largest side must be smaller than sum of other two)
    - Since array is sorted:
          • First valid triplet gives maximum perimeter.

    Example:
        nums = [2,1,2] → sorted = [2,2,1]
        2 < 2+1 → valid → return 5

    Time  : O(n log n) — sorting
    Space : O(1)

    Note:
    - Sorting descending ensures we try largest sides first.
    - First valid triangle is the best possible.
    """

    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort(reverse=True)

        for i in range(len(nums) - 2):

            # Check triangle condition
            if nums[i + 1] + nums[i + 2] > nums[i]: return nums[i] + nums[i + 1] + nums[i + 2]

        return 0