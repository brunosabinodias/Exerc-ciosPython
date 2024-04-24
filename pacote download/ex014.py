km = float(input('Quantidade de km percorridos: '))
dias = float(input('Quantidade de dias: '))
valor = (km * 60) + (dias * 0.15)
print(f'O valor a pagar sera R${valor:.2f}')
