MAX = 20
n = 1
while n <= MAX:
    factor = 1
    print(end=str(n) + ': ')
    while factor <= n:
        if n % factor == 0:
            print(factor, end=' ')
            factor += 1
            print()
            n += 1
            break
            
        # 1: 1
        # 2: 1
        # 3: 1
        # 4: 1
        # 5: 1
        # 6: 1
        # 7: 1
        # 8: 1
        # 9: 1
        # 10: 1
        # 11: 1
        # 12: 1
        # 13: 1
        # 14: 1
        # 15: 1
        # 16: 1
        # 17: 1
        # 18: 1
        # 19: 1
        # 20: 1 
