Problem
A person is said to be sleep deprived if he slept strictly less than 77 hours in a day.

Chef was only able to sleep XX hours yesterday. Determine if he is sleep deprived or not.

Input Format
The first line contains a single integer TT — the number of test cases. Then the test cases follow.
The first and only line of each test case contains one integer XX — the number of hours Chef slept.
Output Format
For each test case, output YES if Chef is sleep-deprived. Otherwise, output NO.

You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical).

Constraints
1 \leq T \leq 201≤T≤20
1 \le X \le 151≤X≤15
Sample 1:
Input
Output
3
4
7
10
YES
NO
NO
Explanation:
Test Case 1: Since 4 \lt 74<7, Chef is sleep deprived.

Test Case 2: Since 7 \ge 77≥7, Chef is not sleep deprived.

Test Case 3: Since 10 \ge 710≥7, Chef is not sleep deprived.
  
  Ans:t=int(input())
for i in range(t):
    n=int(input())
    if(n<7):
        print('YES')
    else:
        print('NO')
