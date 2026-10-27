a1 = int(input("a1: "))
a2 = int(input("a2: "))
b1 = int(input("b1: "))
b2 = int(input("b2: "))

# Складываем единицы
sum_a2b2 = a2 + b2

perenos = sum_a2b2 // 10  # перенос 13(1)
ostatok = sum_a2b2 % 10  # 13(3)

# Складываем десятки + перенос
sum_a1b1 = a1 + b1 + perenos

print(f"{sum_a1b1}; {ostatok}")
