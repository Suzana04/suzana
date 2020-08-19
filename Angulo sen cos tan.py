#Feito por Suzana de Santana 2020 como parte dos meus estudos em Python
#contato: suzana_santana@id.uff.br
#descrição: exercício do curso em vídeo; programa para calcular o seno, cosseno e tangente


import math
angrau = float(input('Digite o valor de um angulo qualquer:'))
sen = math.sin(math.radians(angrau))
cos = math.cos(math.radians(angrau))
tan = math.tan(math.radians(angrau))
print('O valor do seno é {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}'.format(sen,cos,tan) )

angrad = angrau*(math.pi/180)
cosseno = math.cos(angrad)
seno = math.sin(angrad)
tangente = math.tan(angrad)
print('O angulo {} em radiano é {:.2f} e possui como cosseno {:.2f} como seno {:.2f} e tangente {:.2f}'.format(angrau,angrad,cosseno,seno,tangente))

