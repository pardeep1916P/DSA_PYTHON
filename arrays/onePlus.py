class Solution:

    """
    Plus One — Carry Propagation from Right (Optimal Solution)

    Approach:
    - Traverse the digits array from right to left.
    - If the current digit is less than 9:
          • Increment it and return immediately (no further carry).
    - If the digit is 9:
          • Set it to 0 and continue propagating the carry.
    - If all digits were 9 (e.g., 999),
      return [1] + digits to handle overflow.

    Time  : O(n) — worst case when all digits are 9
    Space : O(1) — in-place modification (except overflow case)

    Note:
    This avoids converting the list into an integer,
    which would fail for very large numbers.
    """

    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)

        # Traverse from rightmost digit
        for i in range(n - 1, -1, -1):

            # If no carry propagation needed
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # Carry case: set current digit to 0
            digits[i] = 0

        # If all digits were 9 (e.g., 999 → 1000)
        return [1] + digits
