Problem
Alice and Bob are playing a game of table tennis where irrespective of the point scored, every player makes 22 consecutive serves before the service changes. Alice makes the first serve of the match. Therefore the first 22 serves will be made by Alice, then the next 22 serves will be made by Bob and so on.

Let's consider the following example match for more clarity:

Alice makes the 1^{st}1 
st
  serve.
Let us assume, Bob wins this point. (Score is 00 for Alice and 11 for Bob)
Alice makes the 2^{nd}2 
nd
  serve.
Let us assume, Alice wins this point. (Score is 11 for Alice and 11 for Bob)
Bob makes the 3^{rd}3 
rd
  serve.
Let us assume, Alice wins this point. (Score is 22 for Alice and 11 for Bob)
Bob makes the 4^{th}4 
th
  serve.
Let us assume, Alice wins this point. (Score is 33 for Alice and 11 for Bob)
Alice makes the 5^{th}5 
th
  serve.
And the game continues \ldots…
After the score reaches PP and QQ for Alice and Bob respectively, both the players forgot whose serve it is. Help them determine whose service it is.

Input Format
The first line contains a single integer TT — the number of test cases. Then the test cases follow.
The first line of each test case contains two integers PP and QQ — the score of Alice and Bob respectively.
Output Format
For each test case, determine which player's (Alice or Bob) serve it is.

You may print each character of Alice and Bob in uppercase or lowercase (for example, Bob, BOB, boB will be considered identical).

Constraints
1 \leq T \leq 2001≤T≤200
0 \le P, Q \le 100≤P,Q≤10
Sample 1:
Input
Output
4
0 0
0 2
2 2
4 7
Alice
Bob
Alice
Bob
Explanation:
Test Case 1: Since no points have been scored yet, this is the first serve of the match. Alice makes the 1^{st}1 
st
  serve of the match.
Test Case 2: Two points have been scored yet. Thus, it is the third serve of the match. Bob makes the 3^{rd}3 
rd
  serve of the match.
Test Case 3: Four points have been scored yet. Thus, it is the fifth serve of the match. Alice makes the 5^{th}5 
th
  serve of the match.
Test Case 4: Eleven points have been scored yet. Thus, it is the twelfth serve of the match. Bob makes the 12^{th}12 
th
  serve of the match.
  Solution:t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if(((n+m)//2)%2==0):
        print("Alice")
    else:
        print("Bob")
