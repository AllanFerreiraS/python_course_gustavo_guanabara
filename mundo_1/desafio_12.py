"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
"""

money = float(input("Preço de um produto: R$"))
print(f"Com 5% de desconto, esse produto vai valer R${(money * 0.95):.2f}")
