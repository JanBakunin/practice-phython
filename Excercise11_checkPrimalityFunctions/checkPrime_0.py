num = int(input("Enter a number: "))

divisors = range(2,num)
div_list = [i for i in divisors if num % i == 0]
print(*div_list)

if len(div_list) == 0 and num > 1:
    print(num, "is a prime")
else:
    print(num, "isn't a prime")