cube = lambda x: x ** 3
fibo = [0, 1]


def fibonacci(n):
    # return a list of fibonacci numbers

    if n < 0:
        print("Incorrect Input")
    else:
        for i in range(2, n + 1):
            fibo.append(fibo[i - 1] + fibo[i - 2])

        return fibo[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))