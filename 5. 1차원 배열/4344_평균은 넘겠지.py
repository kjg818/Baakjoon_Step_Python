C = int(input())

for i in range(C):
    sum = 0
    avg = 0
    cnt = 0

    num = list(map(int, input().split())) # num[0] : N, num[1:] : scores
    for j in range(1, len(num)):
        sum += num[j]
    avg = sum / num[0]
    for j in range(1, len(num)):
        if num[j] > avg:
            cnt += 1
    per = cnt / num[0] * 100
    
    print("{:.3f}%".format(round(per,4)))