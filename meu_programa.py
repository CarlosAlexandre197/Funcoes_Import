#Função 00

def apresentacao(nome, idade, sexo):
    print(f'Olá, {nome}! \nSua idade é: {idade}. \nSexo: {sexo}.')

#Função 01

def soma_dois_numeros(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

#Função 02

def potencia(x, expoente=2):
    return x ** expoente

#Função 03

def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo

#Função 04

def mistura_palavras(*args):
    return '_'.join(args)
