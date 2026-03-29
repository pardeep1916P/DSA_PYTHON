class Solution:

    """
    Count Negative Numbers in a Sorted Matrix — Top-Right Traversal (Optimal Solution)

    Approach:
    - Matrix is sorted in non-increasing order (rows & columns).
    - Start from top-right corner.
    - For each position:
          • If current value is negative:
                → all elements below in that column are also negative
                → add (m - r) to count
                → move left
          • Else:
                → move down

    Time  : O(m + n) — at most one pass across rows and columns
    Space : O(1) — constant extra space

    Note:
    - Much faster than scanning all elements (O(m*n)).
    - Uses matrix ordering efficiently.
    """

    def countNegatives(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        r, c = 0, n - 1
        count = 0

        while r < m and c >= 0:

            # Found a negative number
            if grid[r][c] < 0:
                count += m - r   # all below are negative
                c -= 1           # move left

            else:
                r += 1           # move down

        return count