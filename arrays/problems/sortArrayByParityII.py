class Solution:

    """
    Sort Array By Parity II — Two Pointer (Even/Odd Index Placement) (Optimal Solution)

    Approach:
    - Even indices (0,2,4...) must hold even numbers.
    - Odd indices (1,3,5...) must hold odd numbers.
    - Use two pointers:
          • i → even index pointer (starts at 0)
          • j → odd index pointer (starts at 1)
    - Traverse:
          • If nums[i] is even → move i by 2
          • If nums[j] is odd → move j by 2
          • Otherwise → swap nums[i] and nums[j]

    Time  : O(n) — each index visited once
    Space : O(1) — in-place

    Note:
    - Problem guarantees equal number of even and odd elements.
    """

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        i, j = 0, 1
        n = len(nums)

        while i < n and j < n:

            # Correct even position
            if nums[i] % 2 == 0: i += 2

            # Correct odd position
            elif nums[j] % 2 == 1: j += 2

            # Wrong placement → swap
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2

        return nums