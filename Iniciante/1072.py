n = int(input())
numeros = [int(input()) for x in range(n)]

in_ = 0
out_ = 0

for x in numeros:
    if x >= 10 and x <= 20:
        in_ += 1
    else:
        out_ += 1

print('{} in'.format(in_))
print('{} out'.format(out_))