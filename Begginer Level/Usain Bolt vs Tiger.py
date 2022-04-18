Displacement(S)  = ut +(1/2)at2 where u is the initial velocity , #is the acceleration and t is the time taken.

Velocity = Displacement/Time
Input:
The first line will contain T, the number of testcases. Then the description of each test case follow.
Each test case contains 4 integers finish,distancetoBolt,tigerAccelaration,boltSpeed.
Output:
For each testcase, output in a single line, the word "Bolt" or "Tiger" without quotes, depending on whether Bolt wins or the tiger wins.

Solution:
# cook your dish here
n = int(input())

for i in range(n):
    L = input().split()
    
    f = int(L[0])
    dtb = int(L[1])
    ta = int(L[2])
    bs = int(L[3])
    
    bt = f/bs
    
    S = dtb + f
    
    tt = ((2*S)/ta)**(0.5)
    
    if tt>bt:
        print("Bolt")
        
    else:
        print("Tiger")
