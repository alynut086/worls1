import math
a = int(input("Введите сторону квадрата: "))
square_area = a ** 2
print("Площадь квадрата:", square_area)

L = float(input("Введите длину окружности: "))
radius = L / (2 * 3.14)
S = 3.14 * radius ** 2
print(f"Радиус: {radius:.2f}, Площадь круга: {S:.2f}")

seconds = int(input("Введите количество секунд: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
sec = seconds % 60 
print(f"{hours}:{minutes:02}:{sec:02}")