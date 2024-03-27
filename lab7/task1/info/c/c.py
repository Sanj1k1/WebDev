import math
a = int(input())
b = int(input())

result = ""

for i in range(a,b+1):
    if i % math.sqrt(i) == 0:
        result += str(i) + " "

print(result)