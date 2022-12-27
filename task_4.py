# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


import random

n = int(input("Choose a N number: "))


array = [random.randint(-10, 10) for i in range(1, n+1)]

print(array)