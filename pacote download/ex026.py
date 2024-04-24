frase = str(input('Difite uma frase: ')).upper()
print(f'A letra A aparece {frase.count('A')} vezes')
print((f'A primeira letra A aparace na posição {frase.find('A')+1}'))
print(f'A ultima letra A aparece na posição {frase.rfind('A')+1}')
