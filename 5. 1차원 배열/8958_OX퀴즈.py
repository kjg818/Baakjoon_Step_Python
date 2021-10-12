N = int(input())

for i in range(N):
    cnt = 0
    sum = 0
    answer = list(input())
    for j in answer:
        if j == "O":
            cnt += 1
            sum += cnt
                
        else : 
            cnt = 0
    print(sum)