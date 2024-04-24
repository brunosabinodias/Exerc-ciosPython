import random
a = str(input('Auno a: '))
b = str(input('Aluno b: '))
c = str(input('Aluno c: '))
d = str(input('Aluno d: '))
lista = [a,b,c,d]
escolhido = random.choice(lista)
print(f'O aluno sorteado é {escolhido}')
