import os
import sys
from ex01 import Group

sys.path.append('..')
from lab08.ex01_model import Student

g = Group("C:/Users/Librix/Desktop/labs/python_labs/data/lab09/students.csv")


print("=== ИЗНАЧАЛЬНЫЙ СПИСОК ===:")
print(*g.list(), sep="\n")

print("\n=== add() ===")
s = Student("Тестовый Студент", "2005-05-05", "TEST-01", 4.5)
g.add(s)
print(*g.list(), sep="\n")

print("\n=== find('Тест') ===")
print(g.find("Тест"))

print("\n=== update() ===")
g.update("Тестовый Студент", gpa="4.9")
print(g.find("Тест"))
print(*g.list(), sep="\n")

print("\n=== remove() ===")
g.remove("Тестовый Студент")
print(*g.list(), sep="\n")

print("\n=== stats() ===")
print(g.stats())