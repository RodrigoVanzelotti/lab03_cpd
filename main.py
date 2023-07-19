import os
from radix_sort_msd import radix_sort_letters
from file_cleaner import read_file

def contar_ocorrencias(lista_palavras):
    # Inicia variáveis necessárias
    ocorrencias = {}
    palavra_anterior = None
    contador = 0

    # Pra cada palavra na lista, verificar se ela é igual a anterior
    # Se for, realize o contador, se não, apenas o mantenha
    for palavra in lista_palavras:
        if palavra != palavra_anterior:
            if palavra_anterior is not None:
                ocorrencias[palavra_anterior] = contador
            palavra_anterior = palavra
            contador = 1
        else:
            contador += 1

    # Se a palavra anterior existir, o item correspondente das ocorrencias é igual ao contador
    if palavra_anterior is not None:
        ocorrencias[palavra_anterior] = contador

    # Retorna um dicionário de ocorrências
    return ocorrencias

def ordenar_por_frequencia(dicionario_ocorrencias):
    # Classificar as palavras com base em suas contagens (ordenar pelo valor do dicionário)
    palavras_ordenadas = sorted(dicionario_ocorrencias.items(), key=lambda item: item[1], reverse=True)

    # Retornar apenas as 1000 palavras mais frequentes
    return palavras_ordenadas[:1000]


texts = ['frankestein.txt', 'war_and_peace.txt']
sorted_filenames = ['frankestein_sorted.txt', 'war_and_peace_sorted.txt']
counted_filenames = ['frankestein_counted.txt', 'war_and_peace_counted.txt']
ranked_filenames = ['frankestein_ranked.txt', 'war_and_peace_ranked.txt']

files = [os.path.join('entradas', 'textos', file) for file in texts]
# nome_arquivo = 'teste_de_dados.txt'
# nome_arquivo_sorted = 'teste_de_dados_sorted.txt'

for file, save_file_sorted, save_file_counted, save_file_ranked in zip(files, sorted_filenames, counted_filenames, ranked_filenames):
    data = read_file(file)
    data = [palavra.lower() for palavra in data]
    sorted_list = radix_sort_letters(data)
    ocorrencias = contar_ocorrencias(sorted_list)
    ranked = ordenar_por_frequencia(ocorrencias)

    with open(save_file_sorted, 'w') as arquivo:
        for palavra in sorted_list:
            arquivo.write(f'{palavra}\n')

    with open(save_file_counted, 'w') as arquivo:
        for key, value in ocorrencias.items():
            arquivo.write(f'{key} {value}\n')

    with open(save_file_ranked, 'w') as arquivo:
        for tupla in ranked:
            arquivo.write(f'{tupla[0]} {tupla[1]}\n')
