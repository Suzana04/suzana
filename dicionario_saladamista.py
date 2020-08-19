#Feito por Suzana de Santana 2020 como parte dos meus estudos em Python
#contato: suzana_santana@id.uff.br
#descrição: exercício do curso em vídeo; programa para sortear uma fruta e qual ação deve escolher


import random
dic_saladamista = {'uva':'dar abraço','pera':'dar as mãos',
                   'maçã':'beijo no rosto','salada mista':'beijo na boca'}

lista=['pera','uva','maçã','salada mista']

escolha = random.choice(lista)

print('A fruta escolhida foi: {}'.format(escolha))
print('Voce deve:{}'.format(dic_saladamista[escolha]))
