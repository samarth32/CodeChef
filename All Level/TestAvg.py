CodeChef Logo

Upgrade To Pro
User Profile
samarthpatel32
Logout
Back to Practice
Switch to Old Problems Page
Prev Problem
Next Problem
Test Averages
Problem Code:
TESTAVG
Contest Code:
LTIME111
Add to My To Do
Difficulty Rating:558
ADVERTISEMENT

Want to Remove Ads ?
Upgrade To Pro
Problem
Chef has scored A, B,A,B, and CC marks in 33 different subjects respectively.

Chef will fail if the average score of any two subjects is less than 3535. Determine whether Chef will pass or fail.

Input Format
First line will contain TT, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, three integers A, B, CA,B,C, denoting the Chef's score in the three subjects.
Output Format
For each test case, if Chef will pass, print PASS, otherwise print FAIL.

You may print each character of the string in uppercase or lowercase (for example, the strings pass, Pass, pAss, and PASS will all be treated as identical).

Constraints
1 \leq T \leq 10001≤T≤1000
0 \leq A,B,C \leq 1000≤A,B,C≤100
Sample 1:
Input
Output
4
23 47 52
28 36 80
0 100 0
35 35 35
Pass
Fail
Fail
Pass
Explanation:
Test case 11: The average of the first two subjects is 3535, the average of the first and last subject is 37.537.5, whereas the average of the last two subjects is 49.549.5. Since all averages are greater than or equal to 3535, Chef will pass.

Test case 22: Since the average of the first two subjects is 3232 which is less than 3535, Chef will fail.

Test case 33: Since the average of the first and last subjects subjects is 00 which is less than 3535, Chef will fail.

Test case 44: Since the average of any two subjects is 3535 which is greater than or equal to 3535, Chef will pass.

# cook your dish here
t=int(input())
for i in range(t):
    m,n,p=map(int,input().split())
    a=(m+n)/2
    b=(m+p)/2
    c=(n+p)/2
    if a>=35 and b>=35 and c>=35:
        print("Pass")
    else:
        print("Fail")

