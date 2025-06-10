"""
Escreva um programa que leia um valor em metros e o exiba convertedo em centimetros e milímetros.
"""

value = float(input("Medida em metros: "))
print(f"{value:.1f} metros é igual a {value * 100} centimetros.")
print(f"{value:.1f} metros é igual a {value * 1000} milímetros.")
