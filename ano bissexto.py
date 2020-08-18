#Feito por Suzana de Santana 2020 como parte dos meus estudos em Python
#contato: suzana_santana@id.uff.br
#descrição: exercício do curso em vídeo; programa para verificar se o ano selecionado é bissexto


ano = int(input('Digite um ano qualquer: '))

verificador_1 = ano%4
verificador_2 = ano%100
verificador_3 = ano%400

resto_1 = verificador_1
resto_2 = verificador_2
resto_3 = verificador_3

if verificador_1==0:
    print('o ano digitado é bissexto!')
else:
    if verificador_3 == 0:
        print('O ano digitado é bissexto')
    else:print('O ano digitado não é bissexto')
