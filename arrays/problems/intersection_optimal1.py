class Solution:

    """
    Intersection of Two Arrays — Set Intersection (Optimal Solution 1)

    Approach:
    - Convert both lists to sets to remove duplicates.
    - Use set intersection operator (&) to get common elements.
    - Convert the result back to a list.

    Time  : O(n + m)
            n = len(nums1)
            m = len(nums2)
    Space : O(n + m) — additional space for sets

    Note:
    - This is the cleanest and most Pythonic solution.
    - Very concise and efficient.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
