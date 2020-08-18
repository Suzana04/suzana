#Feito por Suzana de Santana 2020 como parte dos meus estudos em Python
#contato: suzana_santana@id.uff.br
#descrição: exercício do curso em vídeo; programa para verificar a viabilidade da costrução de um triângulo com três segmentos de reta.

import math
a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))
if math.fabs(b-c)<a and a<b+c:
    if math.fabs(a-c)<b and b<a+c:
        if math.fabs(a-b)<c and c<a+b:
            print('Podemos construir um triângulo com o perimetro igual a {}'.format(a+b+c))

else:
    print('O triângulo não pode ser construído')
