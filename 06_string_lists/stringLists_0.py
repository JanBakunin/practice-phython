palin = input("Enter a string:")
nilap = palin[::-1]
if palin == nilap:
    print(palin, "is a palindrome")
else:
    print(palin, "is not a palindrome")