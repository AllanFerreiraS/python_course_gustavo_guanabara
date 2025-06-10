"""
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
"""

n = int(input("Tabuada do número: "))
for i in range(1,11):
    print(f"{i} x {n} = {i * n}")

