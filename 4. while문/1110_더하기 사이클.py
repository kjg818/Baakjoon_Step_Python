N = input()
tmp = "asdf"
b = N
cnt = 0

while N != tmp:
    if int(N) < 10:
        N += "0"
        cnt += 1
        if int(N) == 0:
            break
    
    elif int(N) >= 10:
        a = int((int(b) / 10) + (int(b) % 10))
        b = str((int(b) % 10)) + str(a % 10)
        tmp = b
        cnt += 1

print(cnt)