#iterative approach
def find_sum_iterative(n):

    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(find_sum_iterative(5))

#recursive approach
def find_sum_recursive(n):
    if n == 1:
        return 1
    return n + find_sum_recursive(n-1)

print(find_sum_recursive(5))


# Fibonacci Series
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))