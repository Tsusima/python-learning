# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну
# строку.

print(
    f"Numbers that are multiples of 20 or 21 in the range from 20 to 240: {[i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]}")
