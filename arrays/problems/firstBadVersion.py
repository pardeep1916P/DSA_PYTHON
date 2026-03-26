class Solution:

    """
    First Bad Version — Binary Search (Optimal Solution)

    Approach:
    - Search in range [1, n]
    - If mid is bad → first bad is at mid or before
    - Else → move to right half
    - Narrow down until l == r

    Time  : O(log n)
    Space : O(1)
    """

    def firstBadVersion(self, n: int) -> int:

        l, r = 1, n  # correct range

        while l < r:

            mid = l + (r - l) // 2

            if isBadVersion(mid): r = mid
            
            else: l = mid + 1

        return l