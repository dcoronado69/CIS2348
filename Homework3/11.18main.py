#This is 11.18 ZyBooks
#David Coronado: People Soft ID: 1971072
ZyBooksnumbers = input().split()
result = []

for num in numbers:
    num = int(num)
    if num >= 0:
        result.append(num)

result.sort()
for num in result:
    print(num, end=' ')
