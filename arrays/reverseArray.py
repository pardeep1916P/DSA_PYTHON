"""
Reverse Array — Two Pointer In-Place Swap (Optimal Solution)

Approach:
- Use two pointers:
      • l starting at the beginning
      • r starting at the end
- Swap elements at l and r.
- Move l forward and r backward.
- Continue until l >= r.

Time  : O(n) — each element swapped at most once
Space : O(1) — in-place modification

Note:
- Raises ValueError if input is None.
- Works for empty and single-element arrays.
"""

def reverseArray(a):

    # Validate input
    if a is None:
        raise ValueError("Input cannot be None")

    l, r = 0, len(a) - 1

    # Swap elements from both ends moving inward
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1

    return a
