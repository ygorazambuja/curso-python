#!/usr/local/bin/python3

arquivo = open('pessoas.csv')

#Streaming - Melhor
for registro in arquivo:
    print('Nome: {} Idade: {}'.format(*registro.split(',')), end='')

arquivo.close()
