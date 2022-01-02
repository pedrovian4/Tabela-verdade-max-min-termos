import tabelaverdade as tabela

def ler_tabela():
    with open("tabelaVerdade.txt") as file:
        linhas =list(file.readlines())
    return linhas

#Se a coluna S for 1 então a produto da soma das variaveis da coluna
#Se uma variavel for 0  para uma coluna 1 S então essa variavel é barrar


def formatar_tabela():
    aux=[]
    equacao:str=" "
    for i in range(1,len(ler_tabela())):
        for j in range(len(ler_tabela()[i])):
            if str(ler_tabela()[i][j])=='0' or str(ler_tabela()[i][j])=='1' or str(ler_tabela()[i][j]) in tabela.alfabeto:
                aux.append(str(ler_tabela()[i][j]))
    return aux


def min_terms():
    aux_index:int
    equacao:str
    for i in range (len(formatar_tabela())):
        aux_index= tabela.quantidade_variaveis()*(i+2)
        if  aux_index>len(formatar_tabela()):
            break
        if formatar_tabela()[aux_index] =='1':
            for i in range (aux_index):
                print('#')
                #fazer comparação aqui

print(len(formatar_tabela()))
min_terms()

