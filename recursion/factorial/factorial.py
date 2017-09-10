def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)
factr = lambda n: 1 if n <= 1 else n * fact(n-1)
# n = 4
# print("the resutl of !%d is: [%d]" % (n, fact(n)))
n = 4
print("the resutl of !%d is: [%d]" % (n, factr(n)))

def fibonacci(n):
    fib = lambda n: 1 if n <= 2 else fib(n-1) + fib(n-2)
    for i in range(0, n):
        print("[%d]" % fib(i+1))
# fibonacci(5)

arr = [1, 5, 6, 2, 4, 8, 9]
print arr
