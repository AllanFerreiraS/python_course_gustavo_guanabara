"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos dolares ela pode comprar
"""

dolar = 5.57
real = float(input("Quantos reais na carteira: "))
print(f"Com R${real:.2f} na carteira, o dolar valendo ${dolar:.2f}, você pode comprar ${(real / dolar):.2f} dolar(es).")
