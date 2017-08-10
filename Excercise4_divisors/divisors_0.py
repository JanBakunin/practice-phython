num = int(input("Enter a number:"))
divisors = range(1,num+1)
divList = []
for i in divisors:
    if (num % i == 0):
        divList.append(i)
for i in divList:
    print(i)
            