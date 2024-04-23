# 10. Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade de pessoas colaboradoras e o(a) gestor(a) gostaria de ter um agrupamento da soma dessas pessoas para cada estado. As informações contidas na tabela são:

funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]


   # Armazenando os estados sem repetição de valor
estados_unicos = list(set([tupla[0] for tupla in funcionarios]))

# Criando uma lista de listas com valores de funcionários de cada estado
lista_de_listas = []
for estado in estados_unicos:
    lista = [tupla[1] for tupla in funcionarios if tupla[0] == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

# Criando um dicionário com dados agrupados de funcionário por estado
agrupamento_por_estado = {estados_unicos[i]: lista_de_listas[i] for i in range(len(estados_unicos))}
print(agrupamento_por_estado)

# Criando um dicionário com a soma de funcionários por estado
soma_por_estado = {estados_unicos[i]: sum(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(soma_por_estado)
