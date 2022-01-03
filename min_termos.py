import tabela_verdade as tabela

def ler_tabela():
    with open("tabelaVerdade.txt") as file:
        linhas =list(file.readlines())
    return linhas

#Se a coluna S for 1 então a produto da soma das variaveis da coluna
#Se uma variavel for 0  para uma coluna 1 S então essa variavel é barrada
def formatar_tabela():
    aux=[]
    equacao:str=" "
    for i in range(1,len(ler_tabela())):
        for j in range(len(ler_tabela()[i])):
            if str(ler_tabela()[i][j])=='0' or str(ler_tabela()[i][j])=='1' or str(ler_tabela()[i][j]) in tabela.alfabeto:
                aux.append(str(ler_tabela()[i][j]))
    return aux

def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]

def min_terms():
    arr= convert_1d_to_2d(formatar_tabela(),tabela.quantidade_variaveis()+1)
    equa=''
    for i in range(1,len(arr)):
        for j in range(len(arr[i])):
            if arr[i][tabela.quantidade_variaveis()]=='1':
                if j< tabela.quantidade_variaveis():
                    if arr[i][j]=='0':
                        equa+=arr[0][j]+"'"
                    else:
                        equa+=arr[0][j]
        equa+='+'
    print(equa)

def executar():
    min_terms()