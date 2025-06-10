"""
Faça um programa que leia algo
pelo teclado e mostre na tela
o seu tipo primitivo e todas as informações
possíveis sobre ele.
"""

buff = input("Digite algo: ")
print(f">>> \'{buff}\' é numérico: {buff.isnumeric()}")
print(f">>> \'{buff}\' caractere(s): {buff.isalpha()}")
print(f">>> \'{buff}\' é um alfanumerico: {buff.isalnum()}")
print(f">>> \'{buff}\' está minusculo: {buff.islower()}")
print(f">>> \'{buff}\' está maiusculo: {buff.isupper()}")
