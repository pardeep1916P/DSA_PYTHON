class Solution:

    """
    Merge Sorted Array — Extra Array Merge (Brute Force Solution)

    Approach:
    - Use two pointers:
          • i for nums1 (valid elements up to m)
          • j for nums2
    - Compare elements and append the smaller one to a temporary list.
    - After one array is exhausted, append remaining elements.
    - Finally, overwrite nums1 with the merged result.

    Time  : O(m + n)
    Space : O(m + n) — extra array used

    Note:
    - This solution works correctly.
    - However, it violates the in-place requirement of the problem.
    - Not optimal because it uses additional space.
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i, j = 0, 0
        result = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < m:
            result.append(nums1[i])
            i += 1

        while j < n:
            result.append(nums2[j])
            j += 1

        nums1[:] = result