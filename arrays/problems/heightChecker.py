class Solution:

    """
    Height Checker — Compare with Sorted Order (Optimal Solution)

    Approach:
    - Create a sorted copy of the array (expected order).
    - Compare each element with the original array.
    - Count how many positions differ.

    Example:
        heights = [1,1,4,2,1,3]
        expected = [1,1,1,2,3,4]
        mismatches = 3

    Time  : O(n log n) — sorting
    Space : O(n) — extra array for expected

    Note:
    - Simple and reliable.
    - Works for all value ranges.
    """

    def heightChecker(self, heights: List[int]) -> int:

        expected = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]: count += 1

        return count