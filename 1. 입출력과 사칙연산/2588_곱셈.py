A = int(input())
B = int(input())

i = B / 100
i = int(i)
j = (B % 100) / 10
j = int(j)
k = (B % 100) % 10

print(A * k)
print(A * j)
print(A * i)
print(A * B)