Problem
Chef is playing a videogame, and is getting close to the end. He decides to finish the rest of the game in a single session.

There are XX levels remaining in the game, and each level takes Chef YY minutes to complete. To protect against eye strain, Chef also decides that every time he completes 33 levels, he will take a ZZ minute break from playing. Note that there is no need to take this break if the game has been completed.

How much time (in minutes) will it take Chef to complete the game?

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
The first and only line of input will contain three space-separated integers XX, YY, and ZZ.
Output Format
For each test case, output on a new line the answer — the length of Chef's gaming session.

Constraints
1 \leq T \leq 1001≤T≤100
1 \leq X \leq 1001≤X≤100
5 \leq Y \leq 1005≤Y≤100
5 \leq Z \leq 155≤Z≤15
Sample 1:
Input
Output
4
2 12 10
3 12 10
7 20 8
24 45 15
24
36
156
1185
Explanation:
Test case 11: There are 22 levels, each taking 1212 minutes. Chef thus needs a total of 2 \cdot 12 = 242⋅12=24 minutes to complete them both, and no breaks are needed.

Test case 22: There are 33 levels, each taking 1212 minutes. Chef thus needs a total of 3 \cdot 12 = 363⋅12=36 minutes to complete all three. Since the game is completed after the third level, there is no need to take a break.

Test case 33: There are 77 levels, each taking 2020 minutes. Here is Chef's playthrough:

Chef completes the first three levels in 3 \cdot 20 = 603⋅20=60 minutes, and then takes a break for X = 8X=8 minutes.
Next, he completes the fourth, fifth, and sixth levels in another 6060 minutes, and again takes a break for 88 minutes.
Finally, the seventh level is completed in 2020 minutes.
Chef's session hence lasted for 60 + 8 + 60 + 8 + 20 = 15660+8+60+8+20=156 minutes.

#Solution:
t=int(input(""))
for i in range(t):
    x,y,z=map(int,input().split())
    if (x<=3):
        print(int(x*y))
    else:
        a=int((x-1)/3) 
        print(int((x*y)+(a*z)))
