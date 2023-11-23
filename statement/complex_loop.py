# problem series = 1+(1+2)+(1+2+3)+(1+2+3+4)
sum = 0

for i in range(1,5):
    for j in range(1,i+1):
        sum = sum + j

print(sum)