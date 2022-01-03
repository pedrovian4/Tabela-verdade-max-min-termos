import string


#variaveis globais para geração da tabela verdade
alfabeto = list(string.ascii_uppercase)
estados = {0,1}
letras_usadas= []
quantidade_de_letras:int
arquivoTabela=None


#função para abertura de arquivo
def abrir_inputs ():
    with open ("input.txt") as file:
        linhas= list(file.readlines())
        return linhas

#criar e abrir
def abrir_e_criar_tabela_verdade():
    arquivoTabela = open("tabelaVerdade.txt","w")
    return arquivoTabela

#contabilizar quantidade de variaveis para tabela verdade
def quantidade_variaveis():
    quantidade_inputs = len(abrir_inputs())
    for i in range(quantidade_inputs):
            if 2**i == quantidade_inputs:
                return i
    return "Error"


#Armazenar as variaveis necessarias para criação da tabela verdade seguindo uma ordem alfabetica
def armazenar_variaveis():
    quantidade_de_letras = quantidade_variaveis()
    if not (letras_usadas == None):
        letras_usadas.clear()
    for i in range(int(quantidade_de_letras)):
        letras_usadas.append(alfabeto[i])
    letras_usadas.append('S')
    return letras_usadas

#irá escrever a tabela verdade em um arquivo txt
def escrever_tabela ():
    arquivoTabelaVerdade = abrir_e_criar_tabela_verdade()
    line=[]
    pularlinhas:str=''
    for i in range(2**quantidade_variaveis()):
        line.append([i//2**j%2 for j in reversed(range(quantidade_variaveis()))])
    line=[letras_usadas,*line]
    for i in range(1,len(line)):
        line[i]+=abrir_inputs()[i-1]
    for i in line:
        pularlinhas+='\n'+str(i)
    arquivoTabelaVerdade.write(pularlinhas)


def executar():
    armazenar_variaveis()
    escrever_tabela()