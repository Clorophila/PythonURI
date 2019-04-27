PI = 3.1415

r, l = map(int,input().split())

v = 4*PI*(r**3)/3

print(int(l//v))