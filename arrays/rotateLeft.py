"""
Rotate Array Left — Reversal Algorithm (Optimal In-Place Solution)

Approach:
- To rotate the array left by d positions:
      1) Reverse the first d elements
      2) Reverse the remaining n-d elements
      3) Reverse the entire array
- This rearranges elements to achieve left rotation in-place.

Example:
    arr = [1,2,3,4,5], d = 2

    Step 1: reverse(0,1)   → [2,1,3,4,5]
    Step 2: reverse(2,4)   → [2,1,5,4,3]
    Step 3: reverse(0,4)   → [3,4,5,1,2]

Time  : O(n) — each element swapped at most once
Space : O(1) — in-place modification

Note:
- d is reduced using d % n to handle cases where d > n.
- Always handle empty array to avoid division by zero.
"""

def rotateLeft(d, arr):
    n = len(arr)

    # Edge case: empty array
    if n == 0:
        return arr

    # Normalize rotation count
    d = d % n

    # Step 1: Reverse first d elements
    reverse(arr, 0, d - 1)

    # Step 2: Reverse remaining elements
    reverse(arr, d, n - 1)

    # Step 3: Reverse entire array
    reverse(arr, 0, n - 1)

    return arr


def reverse(arr, l, r):
    # Reverse elements between indices l and r
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
