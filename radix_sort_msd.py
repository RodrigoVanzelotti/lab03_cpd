def count_sort_letters(array, size, col, base, max_len):
    # Função auxiliar
    output = [0] * size
    count = [0] * (base + 1)
    min_base = ord('a') - 1 

    for item in array: # Gera contador
        # obter a letra da coluna se estiver dentro da string, se não use dummy position = 0
        letter = ord(item[col]) - min_base if col < len(item) else 0
        count[letter] += 1

    for i in range(len(count)-1):   # Acumula contador
        count[i + 1] += count[i]

    for item in reversed(array):
        # Obtém o índice da letra atual do item na coluna do índice na matriz de contagem
        letter = ord(item[col]) - min_base if col < len(item) else 0
        output[count[letter] - 1] = item
        count[letter] -= 1

    return output

def radix_sort_letters(array, max_col = None):
    # Função principal do sorting
    if not max_col:
        max_col = len(max(array, key = len)) # Coletando o max len

    for col in range(max_col-1, -1, -1): # max_len-1, max_len-2, ...0
        array = count_sort_letters(array, len(array), col, 26, max_col)

    return array


if __name__ == '__main__':
    # Main para testes
    import os
    from file_cleaner import read_file
    
    tests_path = [os.path.join('entradas', 'testes', file) for file in os.listdir(os.path.join('entradas', 'testes'))]
    
    for path in tests_path:
        data = read_file(path)
        import pdb;pdb.set_trace()
        data = [palavra.lower() for palavra in data]
        import pdb;pdb.set_trace()
        print(f'UNSORTED===============\n{data}')
        print(f'SORTED=================\n{radix_sort_letters(data)}\n')