"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para
pinta-lá, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

x = float(input("Largura (metros): "))
y = float(input("Altura (metros: )"))
area = x * y
print(f"Área da parede: {x:.2f} x {y:.2f} = {area:.2f}")
print(f"Com a area de {area:.2f} metros, será necessário {(area / 2):.2f} litros de tinta para pintar a parede.")
