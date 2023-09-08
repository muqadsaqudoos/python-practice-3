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
    file=open('counts.txt','w')
    file.write(str(count)+'\n')
    file.write(str(count1)+'\n')
    file.write(str(count2)+'\n')
    file.write(str(count3)+'\n')
    file.write(str(count4)+'\n')
    file.write(str(count5)+'\n')
    file.write(str(count6)+'\n')
    file.write(str(count7)+'\n')
    file.write(str(count8)+'\n')
        
    
    
    

    f.close()
main()
