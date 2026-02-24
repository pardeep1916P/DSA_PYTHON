class Solution:

    """
    Squares of a Sorted Array — Square Then Sort (Brute-Force Approach)

    Approach:
    - Traverse the array and square each element in-place.
    - Sort the resulting array.
    - Return the sorted squared array.

    Time  : O(n log n) — due to sorting
    Space : O(1) extra (ignoring sorting internals)

    Note:
    - This solution works but is not optimal.
    - It ignores the fact that the original array is already sorted.
    """

    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)): nums[i] = nums[i] * nums[i]

        return sorted(nums)