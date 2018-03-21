di = int(input().split()[1])
hi, mi, si = map(int,input().split(' : '))
df = int(input().split()[1])
hf, mf, sf = map(int,input().split(' : '))

tf = sf + (60*mf) + (3600*hf) + (24*3600*(df-1))
ti = si + (60*mi) + (3600*hi) + (24*3600*(di-1))

dur = tf - ti

d = dur//(24*3600)
dur = dur%(24*3600)
h = dur//(3600)
dur = dur%(3600)
m = dur//(60)
s = dur%(60)

print('{} dia(s)'.format(d))
print('{} hora(s)'.format(h))
print('{} minuto(s)'.format(m))
print('{} segundo(s)'.format(s))