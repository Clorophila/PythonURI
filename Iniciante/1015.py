x = 0
y = 1
p1 = [float(n) for n in input().split()]
p2 = [float(n) for n in input().split()]

print('{:.4f}'.format((((p2[x]-p1[x])**2) + ((p2[y]-p1[y])**2))**(0.5)))