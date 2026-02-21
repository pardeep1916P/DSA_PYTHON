class Solution:

    """
    Valid Palindrome — Two Pointer Filtering Approach (Optimal Solution)

    Approach:
    - Use two pointers:
          • l starting from the left
          • r starting from the right
    - Skip non-alphanumeric characters using isalnum().
    - Compare lowercase versions of characters.
    - If mismatch occurs → return False.
    - If all valid characters match → return True.

    Time  : O(n) — each character processed at most once
    Space : O(1) — constant extra space

    Note:
    - Avoids creating a filtered string.
    - More space-efficient than preprocessing.
    """

    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:

            left = s[l]
            right = s[r]

            # Skip non-alphanumeric from left
            if not left.isalnum(): l += 1

            # Skip non-alphanumeric from right
            elif not right.isalnum(): r -= 1

            else:
                # Compare case-insensitively
                if left.lower() != right.lower(): return False
                l += 1
                r -= 1

        return True