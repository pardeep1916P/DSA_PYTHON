class Solution:

    """
    Remove Duplicates from Sorted Array — Two Pointer Technique (Optimal Solution)

    Approach:
    - Since the array is sorted, duplicates appear consecutively.
    - Maintain a slow pointer `k` pointing to the last unique element.
    - Traverse the array using index `i`:
          • If nums[i] differs from nums[k],
            move k forward and overwrite nums[k] with nums[i].
    - The first (k + 1) elements of the array will contain unique values.

    Time  : O(n) — single pass through the array
    Space : O(1) — in-place modification

    Note:
    This solution modifies the array in-place
    and returns the count of unique elements.
    """

    def removeDuplicates(self, nums: List[int]) -> int:

        k = 0  # index of last unique element

        for i in range(1, len(nums)):

            # Found a new unique element
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]

        return k + 1
