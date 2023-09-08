def main():
    x=1
    count=0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    count8=0
    f=open('nums.txt','r')
    while(x<=10000):
        y = f.readline()
        z=int(y)
        if(z==1):
            count=count+1
        if(z==2):
            count1=count1+1
        if(z==3):
            count2=count2+1
        if(z==4):
            count3+=1
        if(z==5):
            count4+=1
        if(z==6):
            count5+=1
        if(z==7):
            count6+=1
        if(z==8):
            count7+=1
        if(z==9):
            count8+=1
        
        x=x+1
    print('count of 1:',count)
    print('count of 2:',count1)
    print('count of 3:',count2)
    print('count of 4:',count3)
    print('count of 5:',count4)
    print('count of 6:',count5)
    print('count of 7:',count6)
    print('count of 8:',count7)
    print('count of 9:',count8)
    
    
    
    

    f.close()
    file.close()
main()
