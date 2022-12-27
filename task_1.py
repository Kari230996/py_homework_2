# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = str(input("Choose a good number if you can: "))



count = 0
for i in num:
    if i != '.':

        count += float(i)

print(round(count))
