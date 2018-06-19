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
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = [int(x) for x in t3.column_to_list(data_list, 2)]
trip_duration_list.sort()
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
mean_trip = sum(trip_duration_list) / len(trip_duration_list)
median_trip = 0.
if len(trip_duration_list) % 2 == 0:
    index = len(trip_duration_list) / 2
    median_trip = (trip_duration_list[index] + trip_duration_list[index - 1]) / 2
else:
    median_trip = trip_duration_list[int(len(trip_duration_list) / 2)]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# trip_duration_list = t3.column_to_list(data_list, 2)

# min_trip = 0.
# max_trip = 0.
# sum_trip = 0.
# mean_trip = 0.
# median_trip = 0.

# trip_duration_parsed_list = []
# for index, value in enumerate(trip_duration_list):
#     try:
#         parsed = float(value)
#         sum_trip += parsed
#         trip_duration_parsed_list.append(parsed)
#         if index == 0 or parsed < min_trip:
#             min_trip = parsed
#         if parsed > max_trip:
#             max_trip = parsed
#     except ValueError:
#         print('Nao foi possivel fazer o parse do valor', value)
#         raise

# len_trip = len(trip_duration_parsed_list)
# mean_trip = sum_trip / len_trip
# trip_duration_parsed_list = sorted(trip_duration_parsed_list)

# index = len_trip // 2
# if len_trip % 2 > 0:
#     median_trip = trip_duration_parsed_list[index]
# else:
#     median_trip = (trip_duration_parsed_list[index] + trip_duration_parsed_list[index - 1]) / 2