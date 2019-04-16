from collections import defaultdict
import functools
 
 
def fib_list(n):
    fib_lst = [0, 1]
    if n > 1:
        for i in range(2, n+1):
            fib_lst.append(fib_lst[i - 1] + fib_lst[i - 2])
    return fib_lst[n]
 
 
def fib_values(n):
    prev, cur = 0, 1
    for _ in range(n - 1):
        prev, cur = cur, prev + cur
    return cur
 
 
def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
 
 
def memorize(fib_rec_func):
    mem = defaultdict(int)
 
    def wrapper(n):
        mem[n] = fib_rec_func(n)
        return mem[n]
    return wrapper
 
 
@memorize
def fib_rec_mem(n):
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
 
 
@functools.lru_cache(maxsize=None)
def fib_cache(n):
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
 
 
def fib_bin(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return int((phi ** n - psi ** n) / (5 ** 0.5))
 
 
def main():
    n = int(input())
 
 
if __name__ == "__main__":
    main()