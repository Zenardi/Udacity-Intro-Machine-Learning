# coding: utf-8

# Começando com os imports
import csv
import chicago_bikeshare_task3 as t3
import chicago_bikeshare_task5 as t5

#%%
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
# print("Número de linhas:")
# print(len(data_list))


# Se tudo está rodando como esperado, verifique este gráfico!
# gender_list = t3.column_to_list(data_list, -2)
# types = ["Male", "Female"]
# quantity = t5.count_gender(data_list)
# y_pos = list(range(len(types)))
# plt.bar(y_pos, quantity)
# plt.ylabel('Quantidade')
# plt.xlabel('Gênero')
# plt.xticks(y_pos, types)
# plt.title('Quantidade por Gênero')
# plt.show(block=True)

# input("Aperte Enter para continuar...")

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

def count_types(data_list):
    subscriber = 0
    customer = 0
    for d in data_list:
        if d[-3] == "Subscriber":
            subscriber += 1
        elif d[-3] == "Customer":
            customer += 1
    return [subscriber, customer]

# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
gender_list = t3.column_to_list(data_list, -2)
types = ["Subscriber", "Customer"]
quantity = count_types(data_list) #count_types (total)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo')
plt.show(block=True)


input("Aperte Enter para continuar...")