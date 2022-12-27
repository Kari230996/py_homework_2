# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input("Choose a number: "))

array = []

def multi(n):
    if n == 1:
        return 1
    else:
        return n * multi(n-1)

for i in range(1, num+1):
    array.append(multi(i))

print(array)

