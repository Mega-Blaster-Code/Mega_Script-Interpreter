def let(name, val, lst):
    # Verifica se a variável já existe na lista
    for i in range(len(lst)):
        if lst[i] is None:
            # Se encontrar um índice vazio, insere o par e retorna o índice
            lst[i] = (name, val)
            return i
        elif lst[i][0] == name:
            # Se a variável já existe, retorna -1
            return i
    return -1