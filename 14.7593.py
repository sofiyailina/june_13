bykwu = '0123456789ABCDE'
for x in bykwu:
    n1 = int(f'97968{x}13', 15)
    n2 = int(f'7{x}213', 15)
    if (n1 + n2) % 14 == 0:
        print((n1 +n2)//14)
        break

