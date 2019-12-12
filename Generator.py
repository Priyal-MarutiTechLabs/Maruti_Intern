#Factorial without generator
def fact_not_generator(n):
    return 1 if (n == 1 or n == 0) else n * fact_not_generator(n - 1);

x = fact_not_generator(5)

print("factorial of 5 :%d"%x)


#Factorial Using Generator

def fact_generator(n):
    for i in range(0, n+1):
        yield i
x1 = fact_generator(5)
y=0
z=0

try:
    while y <= 5:
        y = next(x1)
        if (z == 0) and (y == 0):
            z = 1
        else:
            z = z * y
except StopIteration:
    pass

print("Factorial of 5 using generator:",z)
