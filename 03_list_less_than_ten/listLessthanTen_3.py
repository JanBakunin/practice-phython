a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = []
num = input("Enter an number")
for element in a:
    if element < num:
        x.append(element)
for element in x:
    print(element)