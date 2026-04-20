# Read an integer input from the user
x = int(input())

# Check if x is greater than 2 AND even (divisible by 2)
if x > 2 and x % 2 == 0:
    print("YES")
else:
    print("NO")