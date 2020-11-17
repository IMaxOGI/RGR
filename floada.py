f = open("in.txt", "r")
[nv, ne] = f.readline().split()
nv = int(nv)# кількість вершин
ne = int(ne) # кількість ребер
b = []# списки суміжності
w = [] # ваги ребер
c = []# ознака сталості
p = []
l = []
l_max = 999999
for k in range(nv):
    b.append([])
    w.append([])
    c.append(False)
    l.append(l_max)
    p.append(0)
for i in range(ne):
    [j, k, u] = f.readline().split()
    j = int(j)
    k = int(k)
    u = int(u)
    b[j].append(k)
    w[j].append(u)
    b[k].append(j)
    w[k].append(u)
f.close


def step(j):
    for i in range(0, len(b[j])):
        if (not c[b[j][i]]):
            s = l[j] + w[j][i]
            if (l[b[j][i]] > s):
                l[b[j][i]] = s
                p[b[j][i]] = j
    s = l_max
    for k in range(0, nv):
        if (not c[k]):
            if (s > l[k]):
                s = l[k]
                i = k
    c[i] = True
    return i
ck=c.copy()
print(c)
f = open("out.txt", "w")
for i in range(1,nv-1):
    start = 0  # Номери вершини,
    finish = nv - i  # між якими шукаємо шлях
    c[start] = True
    l[start] = 0
    j = start
    while not (j == finish):
        j = step(j)

    # Запис у вихідний файл
    # 1) довжини найкоротшого шляху;
    # 2) послідовнисті номерів вершин шляху у зворотньому порядку


    f.write(str(l[finish]) + '\n')
    f.write(str(finish))
    j = finish
    while (not (j == start)):
        j = p[j]
        f.write(' ' + str(j))
    f.write('\n')
    c=ck.copy()
    print(c)
f.close()
