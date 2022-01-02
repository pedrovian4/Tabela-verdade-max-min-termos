import re

def ler_tabela():
    with open("tabelaVerdade.txt") as file:
        linhas =list(file.readlines())
    return linhas

def min_termos():
    array_string=[]
    aux=[]
    #posição 1 da tabela contém as variaveis para formar a expressão
    #indices a serem pulados na comparação 
    #por serem caracteres especiais
    #0,2,4,6,8,10 -> converter cada posição para uma lista
    #
    #11 -> indice do input, responsavel pela operação
    #12-> quebra de linha, ignorar


min_termos()

print(ler_tabela()[1])