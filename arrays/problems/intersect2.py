class Solution:

    """
    Intersection of Two Arrays II — Frequency Map Approach (Optimal Solution)

    Approach:
    - Build a frequency dictionary for nums1.
    - Traverse nums2:
          • If the current number exists in the dictionary
            and its frequency is greater than 0:
                - Add it to the result.
                - Decrement its frequency.
    - This ensures duplicates are counted correctly.

    Example:
        nums1 = [1,2,2,1]
        nums2 = [2,2]

        freq = {1:2, 2:2}
        result → [2,2]

    Time  : O(n + m)
            n = len(nums1)
            m = len(nums2)
    Space : O(n) — frequency dictionary

    Note:
    - This is the optimal approach when duplicates must be preserved.
    - More efficient than sorting-based approaches.
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        freq = {}
        result = []

        # Build frequency map for nums1
        for i in nums1: freq[i] = freq.get(i, 0) + 1

        # Collect intersection elements
        for i in nums2:
            if freq.get(i, 0) > 0:
                result.append(i)
                freq[i] -= 1

        return result