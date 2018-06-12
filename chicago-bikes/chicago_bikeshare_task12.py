# coding: utf-8

# Começando com os imports
import csv
import chicago_bikeshare_task3 as t3



# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")
# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    item_types = []
    count_items = []

    for user_type in column_list:
        if user_type not in item_types:
            item_types.append(user_type)
            count_items.append(1)
        else:
            index = item_types.index(user_type)
            count_items[index] += 1
    return item_types, count_items


# if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
column_list = t3.column_to_list(data_list, -2)
types, counts = count_items(column_list)
print("\nTAREFA 11: Imprimindo resultados para count_items()")
print("Tipos:", types, "Counts:", counts)
assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
# -----------------------------------------------------