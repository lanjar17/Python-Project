file = open("data.txt", "r")
sum = 0
for data in file:
    sum = sum + int(data)
print(sum)
