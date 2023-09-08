def main():
    f=open('counts.txt','r')
    sum=0
    x=1
    while(x<=9):
        y = f.readline()
        z=int(y)
        sum=sum+z
        x=x+1
    print(sum)
    f.close()
main()
    
    
