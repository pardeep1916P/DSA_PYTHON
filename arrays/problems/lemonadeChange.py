class Solution:

    """
    Lemonade Change — Greedy Cash Handling (Optimal Solution)

    Approach:
    - Track number of $5 and $10 bills.
    - For each customer:
          • If $5 → just collect
          • If $10 → give one $5 as change
          • If $20 → prioritize giving ($10 + $5), else give three $5
    - If at any point change cannot be given → return False

    Why greedy works:
    - Always try to use a $10 bill first for $20 change
      to preserve smaller bills for future transactions.

    Time  : O(n) — single pass
    Space : O(1)

    Note:
    - No need to track $20 bills.
    """

    def lemonadeChange(self, bills: List[int]) -> bool:

        fives, tens = 0, 0

        for bill in bills:

            if bill == 5: fives += 1

            elif bill == 10:
                if fives == 0: return False # cannot give change
                fives -= 1
                tens += 1

            else:  # bill == 20

                # Prefer giving $10 + $5
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1

                # Otherwise give three $5 bills
                elif fives >= 3: fives -= 3

                else: return False

        return True