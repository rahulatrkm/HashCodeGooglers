import random
f = open("c.txt", "r")
lines = f.readlines()
fo = open("opc.txt", "w")
D, I, S, V, F = map(int, lines[0].split())
streets = {}
line_idx = 1
for i in range(S):
    temp = lines[line_idx].split()
    str_name = temp[2]
    streets[str_name] = temp
    line_idx += 1

cars = {}
used_streets = set()
follow_path = set()
for i in range(V):
    cars[i] = lines[line_idx].split()
    used_streets.update(cars[i][1:])
    follow_path.update(cars[i][1:-1])
    line_idx += 1
# print(follow_path)

used_interseections = {}
for st in used_streets:
    x = streets[st][1]
    if (st in follow_path):
        if x in used_interseections:
            used_interseections[x].add(st)
        else:
            used_interseections[x] = {st}

# print(used_interseections)
ans = 1
print(len(used_interseections))
fo.write(str(len(used_interseections)) + '\n')
for intersect in used_interseections:
    print(intersect)
    fo.write(str(intersect) + '\n')
    # sts = streets
    sts = list(used_interseections[intersect])
    random.shuffle(sts)
    # print(sts)
    print(len(sts))
    fo.write(str(len(sts)) + '\n')
    if (len(sts) == 1):
        te = sts.pop()
        print(te, D)
        fo.write(te + " " + str(D) + "\n")
    else:
        for street in sts:
            print(street, ans)
            fo.write(street + " " + str(ans) + "\n")
