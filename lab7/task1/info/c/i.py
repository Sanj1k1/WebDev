a = int(input())
sum = 2
for i in range(2,a//2+1):
    if a % i == 0:
        sum += 1

print(sum)