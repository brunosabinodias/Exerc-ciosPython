'''import math
num = float(input('Informe um numero: '))
print(f'A tangente é {math.tan(math.radians(num)):.2f}')
print(f'O cosseno é {math.cos(math.radians(num)):.2f}')
print(f'O seno é {math.sin(math.radians(num)):.2f}')'''

import math
num = float(input('Informe um numero: '))
tan = math.tan(math.radians(num))
print(f'A tangente é {tan:.2f}')
cos = math.cos(math.radians(num))
print(f'O cosseno é {cos:.2f}')
sen = math.sin(math.radians(num))
print(f'O seno é {sen:.2f}')

