# print the nth number of Fibonacci
# use a dict to store already computed result, then use recursion

checked = {}


def fib(n):
    if n in checked:
        return checked[n]

    if n <= 2:
        return 1

    checked[n] = fib(n - 1) + fib(n - 2)
    return checked[n]


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))  # 12586269025
