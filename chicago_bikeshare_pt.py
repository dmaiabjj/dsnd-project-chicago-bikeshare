# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("\nAperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for index in range(1,21):
      print("Linha {} :\n{}".format(index,data_list[index]))

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("\nAperte Enter para continuar...")
# TAREFA 2
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

# TODO: Imprima o `gênero` das primeiras 20 linhas
for index in range(0,20):
      print("Linha {} :\nGênero - {}".format(index+1,data_list[index][-2]))


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("\nAperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for line in data:
        column_list.append(line[index])

    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("\nAperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male    = 0
female  = 0
genders = column_to_list(data_list, -2)

for gender in genders:
    if(gender == "Male"):
        male +=1
    elif(gender == "Female"):
        female +=1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("\nAperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)


def feature_count(features,data_list):
    #      """
    #      Função que compara 2 elementos de uma linha do data list
    #      Argumentos:
    #          features:  É um dictionary que possue como Key o valor a ser comparado e o Value é o index da coluna na qual iremos ter esse valor
    #          data_list: É uma lista contendo todos os dados da amostra
    #      Retorna:
    #          Retorna um dictionary que possue como Key o valor comparado e como Value o total desses valores que apareceram na coluna
    #          Ex : {"Male": 2,"Female": 2}
    #      """
    features_counted = {}
    for key, value in features.items():
        features_counted[key] = column_to_list(data_list,value).count(key)
    return features_counted


def count_gender(data_list):
    #      """
    #      Função que conta quantas x cada um dos gêneros apareceram no data list
    #      Argumentos:
    #          data_list: É uma lista contendo todos os dados da amostra
    #      Retorna:
    #          Retorna uma lista onde no indice 0 estão os valores do gênero Masculino e no indice 1 os valores do gênero feminino
    #          Ex : [25,50]
    #
    #      """
    genders = feature_count({"Male" : -2,"Female": -2},data_list)
    return [genders["Male"], genders["Female"]]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("\nAperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    #      """
    #      Função que verifica qual o gênero mais popular dentro da amostra
    #      Argumentos:
    #          data_list: É uma lista contendo todos os dados da amostra
    #      Retorna:
    #          Retorna uma string com o gênero mais popular ou indicando se os valores são iguais
    #          Ex : Masculino para o gênero Male, Feminino para o gênero Female e Igual em caso de empate
    #
    #      """
    answer      = ""
    gender_qtd  = count_gender(data_list)
    if(gender_qtd[0] > gender_qtd[1]):
        answer = "Masculino"
    elif (gender_qtd[0] < gender_qtd[1]):
        answer = "Feminino" 
    else:
        answer="Igual"

    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("\nAperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
types       = ["Customer", "Subscriber"]
user_types  = feature_count({"Customer" : -3,"Subscriber": -3},data_list)
quantity    = [user_types["Customer"],user_types["Subscriber"]]
y_pos       = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('User Types')
plt.xticks(y_pos, types)
plt.title('Quantidade por User Types')
plt.show(block=True)

input("\nAperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = """Devido aos usuários do tipo Customer não possuírem o registro de gênero informado, apenas o de tipo Subscriber. Provavelmente para usuários que fazem a subscription do serviço,
informar o gênero se faz obrigatório no cadastro e para clientes esporádicos não."""
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("\nAperte Enter para continuar...")
print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip    = 0
max_trip    = 0
mean_trip   = 0
median_trip = 0


round_int   = lambda value:int(round(value))

def quick_sort(unordered_list):
    #      """
    #      Função que executa a ordenação de uma lista pelo método quicksort
    #      Argumentos:
    #          unordered_list: É uma lista na qual desejamos ordenar
    #      Retorna:
    #          Retorna uma lista com os valores ordenados
    #      Algoritmo baseado no exemplo da página:
    #      https://stackoverflow.com/questions/18262306/quicksort-with-python
    #      """
    #Recurso para parar a recursão quando os agrupamentos não tiverem mais elementos
    if not unordered_list:
        return []
    #Escolhemos o primeiro item da lista como nosso Pivô
    pivots = [item for item in unordered_list if item == unordered_list[0]]
    #Agrupamos os elementos menores que o nosso elemento Pivô
    less    = quick_sort([item for item in unordered_list if item < unordered_list[0]])
    #Agrupamos os elementos maiores que o nosso elemento Pivô
    greater = quick_sort([item for item in unordered_list if item > unordered_list[0]])
    #Concatenamos as 3 listas. Pivô é o central com os menores elementos a esquerda e os maiores elementos a direita
    return less + pivots + greater
     
def calc_mean(alist):
    #      """
    #      Função que calcula a média dos valores de uma lista
    #      Argumentos:
    #          alist: É uma lista na qual desejamos calcular a média de seus valores
    #      Retorna:
    #          Retorna a média no formato inteiro
    #
    #      """
    total = 0
    for num in alist:
        total += num
    return round_int(total/len(alist))

def median(alist):
    #      """
    #      Função que calcula a mediana dos valores de uma lista
    #      Argumentos:
    #          alist: É uma lista na qual desejamos calcular a mediana 
    #      Retorna:
    #          Retorna a mediana no formato inteiro
    #
    #      """
    size = len(alist)
    if (size % 2 == 0):
        return (alist[(size)//2] + alist[(size)//2-1]) / 2
    else:
        return alist[(size-1)//2]

trip_duration_list = list(map(int,trip_duration_list))
trip_duration_list = quick_sort(trip_duration_list)

min_trip    = trip_duration_list[0]
max_trip    = trip_duration_list[-1]
mean_trip   = calc_mean(trip_duration_list)
median_trip = median(trip_duration_list)


print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("\nAperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list,3))



print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("\nAperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
#      """
#      Função de exemplo com anotações.
#      Argumentos:
#          param1: O primeiro parâmetro.
#          param2: O segundo parâmetro.
#      Retorna:
#          Uma lista de valores x.
#
#      """

# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types,count_items      = zip(*[(column,column_list.count(column)) for column in iter(set(column_list))])
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------



# TAREFA 12 - Quem tem mais horas de viagens? Homens ou Mulheres (Extra)
input("\nAperte Enter para continuar...")
print("\nTAREFA 12: Imprimindo total das viagens de homens e mulheres")

def feature_sum(tuple_features,data_list):
    #      """
    #      Função que utiliza uma coluna como agrupamento e soma os valores da coluna referente
    #      Argumentos:
    #          tuple_features:  Lista de tuplas que contém 3 elementos: 
    #                               1 - Valor de agrupamento
    #                               2 - Index da coluna na qual o valor de agrupamento se encontra
    #                               3 - Index da coluna na qual o valor referente ao valor de agrupamento está
    #          data_list: É uma lista contendo todos os dados da amostra
    #      Retorna:
    #          Retorna um dictionary que possue como Key o valor de agrupamento e como Value o total dos valores somados 
    #          Ex : {"Male": 1000,"Female": 2500}
    #      """
    features_counted = {}
    for key,key_index,value_index in tuple_features:
        features_counted[key] = sum([int(row[value_index]) for row in filter(lambda row: row[key_index] == key,data_list)])
    return features_counted



print(feature_sum([("Male",-2,-6),("Female",-2,-6)],data_list))



# TAREFA 13 - Ponto de partida mais popular (Extra)
input("\nAperte Enter para continuar...")
print("\nTAREFA 13: Imprimindo os 5 pontos iniciais mais populares")
column_list     = column_to_list(data_list, 3)
types, counts   = count_items(column_list)
zip_list        = list(zip(types,counts))
zip_list        = sorted(zip_list,key = lambda item: item[1],reverse =True)
print(zip_list[:5])


# TAREFA 14 - Ponto de chegada mais popular (Extra)
input("\nAperte Enter para continuar...")
print("\nTAREFA 14: Imprimindo os 5 pontos finais mais populares")
column_list = column_to_list(data_list, 4)
types, counts = count_items(column_list)
zip_list        = list(zip(types,counts))
zip_list        = sorted(zip_list,key = lambda item: item[1],reverse =True)
print(zip_list[:5])



