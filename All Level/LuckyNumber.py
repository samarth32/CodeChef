Problem
Read problem statements in Mandarin Chinese, Russian, and Vietnamese as well.
Chef buys a lottery ticket that has a 33 digit code associated with it. He thinks that digit 77 is his lucky digit and brings him good luck. Chef will win some amount in the lottery if at least one of the digits of the lottery ticket is 77.

Given three digits AA, BB, and CC of the lottery ticket, tell whether Chef wins something or not?

Input Format
First line will contain TT, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, three space separated integers A, B, CA,B,C.
Output Format
For each testcase, output in a single line answer "YES" if Chef wins a positive amount with the lottery and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Constraints
1 \leq T \leq 10001≤T≤1000
0 \leq A, B, C \leq 90≤A,B,C≤9
Sample 1:
Input
Output
3
0 0 0
7 8 9
2 7 7
NO
YES
YES
Explanation:
Test Case 11: Since no digit is equal to 77, Chef fails to win any amount in the lottery.

Test Case 22: Since the first digit is equal to 77, Chef will win some amount in the lottery.

Test Case 33: Since the second and third digit is equal to 77, Chef will win some amount in the lottery.
  
  Ans:t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if(a==7 or b==7 or c==7):
        print('YES')
    else:
        print('NO')
