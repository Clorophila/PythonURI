i = int(input())
f = int(input())

if i<f:
    print(sum([n if n%2!=0 else 0 for n in range(i+1,f)]))
elif i>f:
    print(sum([n if n%2!=0 else 0 for n in range(f+1,i)]))
else:
    print('0')