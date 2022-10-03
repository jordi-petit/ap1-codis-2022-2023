from yogi import read

n= read(int)
# i=0
if n==0:
    print('0')
else:
    while n!=0:
        i=n%10
        n=n//10
        print(i,end='')
    print()