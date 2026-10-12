import math

# Считываем стороны треугольника
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Вычисляем полупериметр
p = (a + b + c) / 2

# Вычисляем площадь по формуле Герона
s = math.sqrt(p * (p - a) * (p - b) * (p - c))

# Выводим результат 
print(f"Площадь: {s:.3}")