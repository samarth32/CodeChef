Explanation
Test case 1: As mentioned in the problem statement, 2 liters of water is required by the water cooler to cool for 1 hour.

Test case 2: 4 liters of water is required by the water cooler to cool for 2 hours.

Input Format
The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
The first and only line of each test case contains an integer N, as described in the problem statement

Output Format
For each test case, output the number of liters of water required by the water cooler to cool for N hours.

Solution
t=int(input())
for i in range(t):
    n=int(input())
    ans=n*2
    print(ans)
