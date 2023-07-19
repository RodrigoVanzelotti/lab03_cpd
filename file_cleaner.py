# Função para limpar a file e retornar o texto formatado
def read_file(file_path:str):
    # opening file
    with open(file_path, 'r') as f:
        conteudo = f.read()
    
    return conteudo.split(' ')
