class Solution:

    """
    Binary Search — Iterative Implementation (Optimal Solution)

    Approach:
    - Maintain two pointers: left and right.
    - Repeatedly check the middle element.
    - Narrow the search space depending on comparison.

    Time  : O(log n)
    Space : O(1)
    """

    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                l = mid + 1

            else:
                r = mid - 1

        return -1