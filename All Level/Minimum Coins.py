Problem
There are only 22 type of denominations in Chefland:

Coins worth 11 rupee each
Notes worth 1010 rupees each
Chef wants to pay his friend exactly XX rupees. What is the minimum number of coins Chef needs to pay exactly XX rupees?

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of a single line of input containing a single integer XX.
Output Format
For each test case, output on a new line the minimum number of coins Chef needs to pay exactly XX rupees.

Constraints
1 \leq T \leq 10001≤T≤1000
1 \leq X \leq 10001≤X≤1000
Sample 1:
Input
Output
4
53
100
9
11
3
0
9
1
Explanation:
Test case 11: Chef can use 55 notes and 33 coins in the optimal case.

Test case 22: Chef can use 1010 notes and 00 coins in the optimal case.

Test case 33: Chef can only use 99 coins.

Test case 44: Chef can use 11 note and 11 coin in the optimal case.

#Solution:
t=int(input())
for i in range(t):
    X=int(input())
    n=(str(X))[-1]
    if len(str(X))>1:
        if (X-(int(n)))%10==0:
            print(int(n))
        elif X%10:
            print("0")
    else:
        print(X)
