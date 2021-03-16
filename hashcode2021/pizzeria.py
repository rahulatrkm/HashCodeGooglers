def countPizza(numberOfTeams, teamSize, currentRemPizza, ans):
    # print(numberOfTeams, teamSize, currentRemPizza, ans)
    if (currentRemPizza > (numberOfTeams*teamSize)):
        ans += numberOfTeams
        currentRemPizza -= numberOfTeams*teamSize
    else:
        teamServed = currentRemPizza//teamSize
        ans += teamServed
        currentRemPizza -= (teamServed * teamSize)
    return ans, currentRemPizza

f = open("e_many_teams.in", "r")
lines = f.readlines()
fo = open("ope.txt", "w")
m, t2, t3, t4 = map(int, lines[0].split())
# d = {}
# for i in range(m):
#     // reading pizza slices
#     arr = lines[i+1].split()

ans = 0
ans, m = countPizza(t2, 2, m, ans)
ans, m = countPizza(t3, 3, m, ans)
ans, m = countPizza(t4, 4, m, ans)

print(ans)
fo.write(str(ans) + '\n')
curr = ans
j = 0
for i in range(ans):
    if (t2 > 0):
        print(2, j, j+1)
        fo.write(str(2) + ' ' + str(j) + ' ' + str(j+1) + '\n')
        j += 2
        t2 -= 1
    elif (t3 > 0):
        print(3, j, j+1, j+2)
        fo.write(str(3) + ' ' + str(j) + ' ' + str(j+1) + ' ' + str(j+2) + '\n')
        j += 3
        t3 -= 1
    elif (t4 > 0):
        print(4, j, j+1, j+2, j+3)
        fo.write(str(4) + ' ' + str(j) + ' ' + str(j+1) + ' ' + str(j+2) + ' ' + str(j+3) + '\n')
        j += 4
        t4 -= 1