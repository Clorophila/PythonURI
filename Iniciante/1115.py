while(True):
    x, y = map(int,input().split())
    if(x>0):
        if(y>0):
            print('primeiro')
        elif(y<0):
            print('quarto')
        else:
            break
    elif(x<0):
        if(y>0):
            print('segundo')
        elif(y<0):
            print('terceiro')
        else:
            break
    else:
        break