#Feito por Suzana de Santana 2020 como parte dos meus estudos em Python
#contato: suzana_santana@id.uff.br
#descrição: exercício do curso em vídeo; programa para escolher um aluno e verificar a ordem de apresentação


from random import randint
lista_de_alunos = []
n= int(input('Quantos alunos tem em sala?'))

for alunos in range (1,n+1):
    novo = input('Digite o nome do aluno de número {}'.format(alunos))
    lista_de_alunos.append(novo)

lista_de_alunos_alfabetica = sorted(lista_de_alunos)

#for alunos in range (0,n):
   # print(lista_de_alunos_alfabetica[alunos])

for alunos in lista_de_alunos_alfabetica:
    print(alunos)

sorteado = randint(0,n-1)
print('O aluno sorteado para apagar o quadro é:{}'.format(lista_de_alunos_alfabetica[sorteado]))


lista_sorteada = []
sorteados = 0

while(sorteados<n):
    sorteado_novo = randint(0,n-1)

    nome = lista_de_alunos_alfabetica[sorteado_novo]
    if nome not in lista_sorteada:
        lista_sorteada.append(nome)
        sorteados+=1

print ('A ordem de apresentação será:')

for alunos in lista_sorteada:
    print(alunos)








