from random import *
x=randint(1,9)
print(x)
n=input('Enter guess:')
while(n!=x):
    print(n)
    print(x)
    print(n!=x)
    n=input('Enter guess:')
print('Well guessed')
    
        
    
    
