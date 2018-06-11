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

# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
def my_median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2
    print("Tamanho da Lista: " + str(lstLen))

    if (lstLen % 2):
        print(">>>>1")
        return sortedLst[index + 1]
    else:
        print(">>>>2")
        return (sortedLst[index] + sortedLst[index + 1])/2.0

trip_duration_list = t3.column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
total = 0.
list_len = len(trip_duration_list)

for trip_duration in trip_duration_list:
    if float(trip_duration) > max_trip or max_trip == 0:
        max_trip = float(trip_duration)
    elif float(trip_duration) < min_trip or min_trip == 0:
        min_trip = float(trip_duration)

    total += float(trip_duration)

mean_trip = total / (len(trip_duration_list) - 1)

median_trip = my_median(trip_duration_list)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")