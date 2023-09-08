m, M = int(input()), set(map(int, input().split()))
n, N = int(input()), set(map(int, input().split()))

res = list(M.union(N))
res.sort()

for i in range(len(res)):
    if res[i] not in list(M.intersection(N)):
        print(res[i])