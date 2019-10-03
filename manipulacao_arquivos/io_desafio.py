import csv

with open('desafio-ibge.csv', encoding='latin1') as dados:
    for cidade in csv.reader(dados):
        print(f'{cidade[8]} : {cidade[3]}')
