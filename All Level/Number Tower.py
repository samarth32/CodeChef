Problem
Problem Statement
Write a program that keeps accepting numbers and printing them.

Input
First line contains the number of integers, N.
The next N lines which follow each have an integer.
Output
For each integer, output one new line which contains the integer.

Constraints
1 ≤ N ≤ 20
1 ≤ every integer ≤ 1000000
Sample Input
5
1
12
5
535
349764
Sample Output
1
12
5
535
349764

Ans:t=int(input())
for i in range(t):
    n=int(input())
    print(n)
