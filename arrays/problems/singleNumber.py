class Solution:

    """
    Single Number — XOR Bit Manipulation (Optimal Solution)

    Approach:
    - Use XOR operation properties:
          • a ^ a = 0
          • a ^ 0 = a
          • XOR is commutative and associative
    - XOR all elements in the array.
    - Duplicate numbers cancel each other out.
    - The remaining value is the single number.

    Example:
        nums = [4,1,2,1,2]
        result = 4 ^ 1 ^ 2 ^ 1 ^ 2
               = 4 ^ (1^1) ^ (2^2)
               = 4 ^ 0 ^ 0
               = 4

    Time  : O(n) — single pass
    Space : O(1) — constant extra space

    Note:
    This is the most optimal solution.
    Avoids using extra data structures like sets or dictionaries.
    """

    def singleNumber(self, nums: List[int]) -> int:

        result = 0

        for i in nums:
            result ^= i

        return result
