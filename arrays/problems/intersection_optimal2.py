class Solution:

    """
    Intersection of Two Arrays — Sorting + Two Pointers (Optimal Solution 2)

    Approach:
    - Sort both arrays.
    - Use two pointers to traverse both arrays simultaneously.
    - If elements match:
          • Add to result set (to avoid duplicates).
          • Move both pointers.
    - If nums1[i] < nums2[j], move i.
    - Otherwise, move j.

    Time  : O(n log n + m log m)
            due to sorting
    Space : O(k) — result set (k = size of intersection)

    Note:
    - Useful when set usage is restricted.
    - More manual control compared to set intersection.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()

        i = j = 0
        result = set()

        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:
                result.add(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]: i += 1

            else: j += 1

        return list(result)
