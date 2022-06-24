Problem
Chef appeared for a placement test.

There is a problem worth XX points. Chef finds out that the problem has exactly 1010 test cases. It is known that each test case is worth the same number of points.

Chef passes NN test cases among them. Determine the score Chef will get.

NOTE: See sample explanation for more clarity.

Input Format
First line will contain TT, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers XX and NN, the total points for the problem and the number of test cases which pass for Chef's solution.
Output Format
For each test case, output the points scored by Chef.

Constraints
1 \leq T \leq 1001≤T≤100
10 \leq X \leq 20010≤X≤200
0 \leq N \leq 100≤N≤10
XX is a multiple of 1010.
Sample 1:
Input
Output
4
10 3
100 10
130 4
70 0
3
100
52
0
Explanation:
Test Case 11: The problem is worth 1010 points and since there are 1010 test cases, each test case is worth 11 point. Since Chef passes 33 test cases, his score will be 1 \cdot 3 = 31⋅3=3 points.

Test Case 22: The problem is worth 100100 points and since there are 1010 test cases, each test case is worth 1010 points. Since Chef passes all the 1010 test cases, his score will be 10 \cdot 10 = 10010⋅10=100 points.

Test Case 33: The problem is worth 130130 points and since there are 1010 test cases, each test case is worth 1313 points. Since Chef passes 44 test cases, his score will be 13 \cdot 4 = 5213⋅4=52 points.

Test Case 44: The problem is worth 7070 points and since there are 1010 test cases, each test case is worth 77 points. Since Chef passes 00 test cases, his score will be 7 \cdot 0 = 07⋅0=0 points.

Solution:
  t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    print((n)*(m)//10)
