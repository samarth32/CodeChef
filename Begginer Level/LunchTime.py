Chef has his lunch only between 1 pm and 4 pm (both inclusive).

Given that the current time is X pm, find out whether it is lunchtime for Chef.

Input Format
The first line of input will contain a single integer T, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, containing one integer X.
Output Format
For each test case, print in a single line YES if it is lunchtime for Chef. Otherwise, print NO.

You may print each character of the string in either uppercase or lowercase (for example, the strings YeS, yEs, yes and YES will all be treated as identical).

Constraints
1≤T≤12
1≤X≤12
Sample Input 1 
3
1
7
3
Sample Output 1 
YES
NO
YES
Explanation
Test case 1: Lunchtime is between 1 pm and 4 pm (both inclusive). Since 1 pm lies within lunchtime, the answer is YES.

Test case 2: Lunchtime is between 1 pm and 4 pm (both inclusive). Since 7 pm lies outside lunchtime, the answer is NO.

Test case 3: Lunchtime is between 1 pm and 4 pm (both inclusive). Since 3 pm lies within lunchtime, the answer is YES.

Author:	5★notsoloud
Editorial:	https://discuss.codechef.com/problems/LTIME
Tags:	Tags are hidden. Show temporarily
Update this setting in edit profile


Difficulty Rating:	352
Date Added:	10-04-2022
Time Limit:	1 secs
Source Limit:	50000 Bytes
Languages:	CPP17, PYTH 3.6, JAVA, C, CPP14, PYTH, PYP3, CS2, ADA, PYPY, TEXT, PAS fpc, NODEJS, RUBY, PHP, GO, HASK, TCL, kotlin, PERL, SCALA, LUA, BASH, JS, rust, LISP sbcl, PAS gpc, BF, CLOJ, R, D, CAML, swift, FORT, ASM, FS, WSPC, LISP clisp, SQL, SCM guile, PERL6, ERL, CLPS, PRLG, SQLQ, ICK, NICE, ICON, COB, SCM chicken, PIKE, SCM qobi, ST, NEM
Submit
My SolutionsOther’s Solutions
Successful Solutions
Video SolutionNew!
Tried this problem but couldn't solve it? Check the detailed explanation by our expert educators.



Discussions
See all discussions related to this problem on the discussion forum.

See Discussions Give Feedback

Solution:# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    if(n>=1 and n<=4):
        print("YES")
    else:
        print("NO")
