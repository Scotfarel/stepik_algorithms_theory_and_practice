Задача на программирование: различные слагаемые
По данному числу 1≤n≤10e9 найдите максимальное число k, для которого n можно представить как сумму k различных натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.
 
 
n = int(input())
i = 1
 
numbers = []
while n > 2*i:
    n -= i
    numbers.append(i)
    i += 1
 
numbers.append(n)
print(i)
print(*numbers, sep=' ')
 
 
Задача на программирование: покрыть отрезки точками
 
 
По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.
 
В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит по два числа 0≤l≤r≤10e9, задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них.
 
n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))
lines.sort(key=lambda x: x[1])
 
covered = []
i = 0
while i < n:
    covered.append(lines[i])
    right_end = lines[i][1]
    i += 1
    while i < n and lines[i][0] <= right_end:
        i += 1
 
print(len(covered))
print(*(dot[1] for dot in covered))
 
 
 
Задача на программирование: непрерывный рюкзак
 
 
Первая строка содержит количество предметов 1≤n≤10e3 и вместимость рюкзака 0≤W≤2⋅10e6. Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅10e6 и объём 0<wi≤2⋅10e6 предмета (n, W, ci, wi — целые числа). Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
 
items_num, bag_volume = map(int, input().split())
items = []
for _ in range(items_num):
    cost, item_volume = map(int, input().split())
    items.append((cost / item_volume, item_volume))
items.sort(key=lambda x: x[0], reverse=True)
 
items_weight = 0
price = 0
for item in items:
    if bag_volume >= item[1]:
        price += item[0] * item[1]
        bag_volume -= item[1]
    else:
        price += item[0] * bag_volume
        break
print(round(price, 3))
 
 
 
Задача на программирование: наибольший общий делитель
 
 
По данным двум числам 1≤a, b≤2*10e9 найдите их наибольший общий делитель.
 
 
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    if a >= b:
        return gcd(a % b, b)
    else:
        return gcd(b % a, a)
 
def gcd_optimized(a, b):
    while b:
        a, b = b, a % b
    return a
 
 
 
def main():
    a, b = map(int, input().split())
    print(gcd(a, b))
 
 
if __name__ == "__main__":
    main()