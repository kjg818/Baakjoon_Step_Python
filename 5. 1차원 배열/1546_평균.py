N = []
s = 999
result = []
for i in range(10):
    num = int(input())
    N.append(num)
    
for i in range(len(N)):
    s = N[i] % 42
    if s not in result:
        result.append(s)
            
print(len(result))