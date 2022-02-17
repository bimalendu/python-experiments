#fibonnaci series

n1 = 0
n2 = 1
sum = 0

print(n1, end=",") #0
print(n2, end=",") #1

while(sum < 100):
    sum = n1 + n2
    n1 = n2
    n2 = sum
    print(sum, end=",")