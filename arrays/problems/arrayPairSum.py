from typing import List


class Solution:

    """
    Array Partition — Counting Sort + Greedy Pairing (Optimal Solution)

    Approach:
    - Use a frequency array to simulate sorting (since values are bounded).
    - Shift values by +10000 to handle negative numbers.
    - Iterate through the frequency array in sorted order.
    - Use a boolean `take`:
          • Add every alternate element (minimum of each pair).
          • This simulates pairing after sorting.

    Why it works:
    - After sorting, the optimal strategy is:
          sum of nums[0], nums[2], nums[4], ...
      (i.e., take the smaller element of each pair)

    Time  : O(n + K) ≈ O(n)
    Space : O(K) — frequency array (constant size)

    Note:
    - Avoids explicit sorting.
    - Efficient when value range is limited.
    """

    def arrayPairSum(self, nums: List[int]) -> int:

        # Frequency array for range [-10000, 10000]
        freq = [0] * 20001
    
        # Fill frequency
        for i in nums: freq[i + 10000] += 1

        sum = 0
        take = True  # toggle to pick every alternate number

        # Traverse in sorted order
        for i in range(20001):

            while freq[i] > 0:

                if take: sum += i - 10000  # convert back to original value

                take = not take
                freq[i] -= 1

        return sum