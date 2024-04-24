real = float(input('Quanto reais voce tem na carteira? '))
dolar = real / 5.07
d = float(input('Quantos dolares voce tem na carteira? '))
r = d * 5.07
print(f'com R${real:.2f} voce pode comprar US${dolar:.2f}')
print(f'com US${d:.2f} voce pode comprar R${r:.2f}')
