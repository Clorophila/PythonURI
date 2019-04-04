import re
for c in range(int(input())):
    print(sum([int(s) for s in re.findall(r'\d+',input())]))
