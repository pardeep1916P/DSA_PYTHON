class Solution:

    """
    Best Time to Buy and Sell Stock — One Pass Min Tracking (Optimal Solution)

    Approach:
    - Track the index of the minimum price seen so far.
    - For each price:
          • If current price is lower → update min index.
          • Else → calculate profit using current price and min price.
          • Update maximum profit if needed.

    Example:
        prices = [7,1,5,3,6,4]
        buy at 1, sell at 6 → profit = 5

    Time  : O(n) — single pass
    Space : O(1)

    Note:
    - Ensures buy happens before sell.
    - Avoids nested loops (O(n²)).
    """

    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0: return 0

        min, max = 0, 0  # indices and profit

        for i in range(len(prices)):

            # Update minimum price index
            if prices[i] < prices[min]: min = i

            else:
                # Calculate profit
                profit = prices[i] - prices[min]

                # Update maximum profit
                max = profit if profit > max else max

        return max