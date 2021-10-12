N = []
for i in range(9):
    num = int(input())
    N.append(num)

M = max(N)
n = N.index(M)

print(M)
print(n + 1)