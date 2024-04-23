# 8. Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas:
# id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
# preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]


id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]


tabela = [('id', 'quantidade', 'preco', 'total')]
tabela += [(id[i], quantidade[i], preco[i], quantidade[i]*preco[i]) for i in range(len(id))]
