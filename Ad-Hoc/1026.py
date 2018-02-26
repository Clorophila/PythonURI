while True:
    try:
        a,b = [int(n) for n in input().split()]
        print('{}'.format(a^b))        
    except:
        break