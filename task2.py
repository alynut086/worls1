n = int(input("Введите число: "))
if n > 0:
    n += 1
else:
    n -= 2

print(n)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

min_num = min(a, b, c)
max_num = max(a, b, c)

print(min_num, max_num)

n = int(input("Введите количество поездок: "))

ticket_60 = n // 60
n %= 60

ticket_20 = n // 20
n %= 20

ticket_10 = n // 10
n %= 10

ticket_5 = n // 5
n %= 5
ticket_1 = n 
print(ticket_1, ticket_5, ticket_10, ticket_20, ticket_60)