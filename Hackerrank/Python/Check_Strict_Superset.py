A = set(map(int, input().split()))
N = int(input())

set_list = []
for i in range(N):
    x = set(map(int, input().split()))
    set_list.append(x)

result = True

for i in set_list:
    if not A.issuperset(i):
        result = False

print(result)




