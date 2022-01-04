import tabela_verdade as tabela


#nesse arquivo vamos abrir a o arquivo gerado no  tabela_verdade.py e ler como uma lista
def ler_tabela():
    with open("tabelaVerdade.txt") as file:
        linhas =list(file.readlines())
    return linhas


#Logo após leitura será feito a remoção de characteres especiais
def formatar_tabela():
    aux=[]
    equacao:str=" "
    for i in range(1,len(ler_tabela())):
        for j in range(len(ler_tabela()[i])):
            if str(ler_tabela()[i][j])=='0' or str(ler_tabela()[i][j])=='1' or str(ler_tabela()[i][j]) in tabela.alfabeto:
                aux.append(str(ler_tabela()[i][j]))
    return aux

#Logo em seguida temos uma função para converter um array 1d para 2d
#Isso é feito para facilitar as comprações e localização das variabeis 
def converter_1d_para_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]


#aqui é realizado as comparações e retirada da equação
def min_terms():
    arr= converter_1d_para_2d(formatar_tabela(),tabela.quantidade_variaveis()+1)
    equa=''
    k= False
    for i in range(1,len(arr)):
        for j in range(len(arr[i])):
            if arr[i][tabela.quantidade_variaveis()]=='1':
                if j< tabela.quantidade_variaveis():
                    k = True
                    if arr[i][j]=='0':
                        equa+=arr[0][j]+"'"
                    else:
                        equa+=arr[0][j]
        if k:
            k = not k
            equa+='+'
    print(equa)

def executar():
    min_terms()