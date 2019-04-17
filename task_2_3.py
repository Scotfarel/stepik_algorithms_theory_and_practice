"""
Задача на программирование: последняя цифра большого числа Фибоначчи.
 
 
Дано число 1≤n≤10e7, необходимо найти последнюю цифру n-го числа Фибоначчи.
"""
 
def fib_digit(n):
    prev, cur = 0, 1
    for _ in range(n - 1):
        prev, cur = cur, (prev + cur) % 10
    return cur
 
 
def main():
    n = int(input())
    print(fib_digit(n))
 
 
if __name__ == "__main__":
    main()
 
 
"""
Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю.
 
 
Даны целые числа 1≤n≤10e18 и 2≤m≤10e5, необходимо найти остаток от деления n-го числа Фибоначчи на m.
"""
def fib_mod(n, m):
    period = [0, 1]
    i = 2
    while i < m * 6:
        period.append((period[i - 1] + period[i - 2]) % m)
        if period[i] == 1 and period[i - 1] == 0:
            break
        i += 1
    return period[n % (len(period) - 2)]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))
 
 
if __name__ == "__main__":
    main()
