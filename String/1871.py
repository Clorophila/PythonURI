while True:
    m,n=map(int,input().split())
    if m==n and m==0:
        break
    else:
        print(str(m+n).replace('0',''))