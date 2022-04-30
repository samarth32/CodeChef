Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains a single string S with length N.
Output
For each test case, print a single line containing one integer ― the number of occurrences of a vowel immediately after a consonant.
Explanation
Example case 1: The vowel 'a' follows after the consonant 'b', 'e' follows after 'z' and 'i' follows after 'c', so the answer is 3.

Example case 2: The only vowel 'u' follows after 'b', so the answer is 1.
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    l=["a","e","i","o","u"]
    c=0
    for i in range(1,len(s)):
        if s[i-1] not in l and s[i] in l:
            c=c+1
    print(c)
