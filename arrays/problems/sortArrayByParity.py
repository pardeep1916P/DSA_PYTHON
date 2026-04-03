class Solution:

    """
    Sort Array By Parity — Two Pointer Partitioning (Optimal Solution)

    Approach:
    - Use two pointers:
          • l from start
          • r from end
    - If left is odd and right is even → swap
    - If left is even → move l forward
    - If right is odd → move r backward
    - Continue until pointers meet

    Time  : O(n) — each element visited at most once
    Space : O(1) — in-place

    Note:
    - Even numbers (0) should come before odd numbers (1)
    - Uses modulo to classify parity
    """

    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        l, r = 0, len(nums) - 1

        while l < r:

            # If left is odd and right is even → swap
            if nums[l] % 2 > nums[r] % 2:
                nums[l], nums[r] = nums[r], nums[l]

            # If left is already even → move forward
            elif nums[l] % 2 == 0: l += 1

            # If right is already odd → move backward
            elif nums[r] % 2 == 1: r -= 1

        return nums