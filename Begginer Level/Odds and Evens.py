#Input Format
First line will contain T, number of testcases. Then the T testcases follow.
Each testcase contains of a single line of input, two integers a,b which denote the number played by Alice and Bob respectively

#Output Format
For each testcase, output which player won the game.

#Explanation
In the first test case, Alice and Bob both played 1. The sum of the numbers played by them is 2 which is even. Therefore Bob wins.

In the second test case, Alice played 1 while Bob played 2. The sum of the numbers played by them is 3 which is odd. Therefore Alice wins.

#Solution
# cook your dish here
t=int(input())
for i in range(t):
    n,m=list(map(int,input().split()))
    sum=n+m
    if(sum%2==0):
        print("Bob")
    else:
        print("Alice")
