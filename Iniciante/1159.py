while(True):
    x = int(input())
    if(x==0):
        break
    if(x%2!=0):
        x+=1
    print(5*(x+4))