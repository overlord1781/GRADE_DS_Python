a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a <= b <= 10 and c<=d and d<=10:
    for q in range(c, d+1):
        print('\t',q,end='')
    print()
    for i in range(a,b+1,1):
        print(i,end='')
        for j in range(c, d + 1, 1):
            print('\t',j*i,end='')
        print()
else:
    print()
