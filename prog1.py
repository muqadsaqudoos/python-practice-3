r=int(input('Rows:'))
c=int(input('columns:'))
sum=0
for i in range(r):
    a=1
    for j in range(c):
        print(a,end='')
        sum=sum+a
        a=a+(i+1)
        if(j==c-1):
            print('=',end='')
        else:
            print('+',end='')
    print(sum)
    sum=0
