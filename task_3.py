# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

num = int(input("Choose the N number: "))



res = [round((1 + 1/i)**i, 3) for i in range(1, num+1)]
print(f"For n={num} {res}\nSum: {round(sum(res), 3)}")

