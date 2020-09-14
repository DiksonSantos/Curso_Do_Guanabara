from math import hypot
#import math
co = float(input('Comprimento do Cateto Oposto:'))
ca = float(input('Comprimento do Cateto Adjacente:'))

'''hi = (co **  2 +ca ** 2 ) ** (1/2)
print('A Hipotenusa Vai Medir {:.3f}'.format(hi))'''

hi = hypot(co,ca)
#hi = math.hypot(co,ca)

print('A Hipotenusa Vai Medir {:.2f}'.format(hi))
