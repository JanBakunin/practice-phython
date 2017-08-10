a = 0
b = 1
fibo = [1,1]
how_many = int(input("How many numbers should be displayed: "))

def fibonacci(a, b):
    if a+2 < how_many:
        fibo.append(fibo[a] + fibo[b])
        a += 1
        b += 1
        fibonacci(a, b)
    else:
        print (*fibo)
fibonacci(a,b)