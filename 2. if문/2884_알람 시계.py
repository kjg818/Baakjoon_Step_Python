H, M = map(int, input().split())
if (0 <= H <= 23) and (0 <= M <= 59):
    if M < 45:
        M = 60 - 45 + M
        H -= 1
        if H <= 0:
            H += 24
            if H == 24:
                H = 0

    elif M >= 45:
        M -= 45
        if H <= 0:
            H += 24
            if H == 24:
                H = 0

print(H, M)