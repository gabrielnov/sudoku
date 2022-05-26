def quick_sort(v):
    quick_sort_helper(v, 0, len(v)-1)

def quick_sort_helper(v, ini, fim):
    print(f'{v}, ini={ini}, fim={fim}')
    """ ordena a região do vetor v no intervalo das posições de ini até fim """

    n = fim - ini + 1
 
    if n > 1:
        posicao_pivo = selecionar_pivo(v, ini, fim)
        
        # particionar
        posicao_divisao = particionar(v, posicao_pivo, ini, fim)
        
        # ordenar a primeira partição
        quick_sort_helper(v, ini, posicao_divisao - 1)
        
        # ordenar a segunda partição
        quick_sort_helper(v, posicao_divisao + 1, fim)
    # caso contrário, já está ordenado
    else:
        pass

def selecionar_pivo(v, ini, fim):
    """ retorna a posição do pivô escolhido no intervalo das posições ini até fim """
    return ini

def particionar(v, posicao_pivo, ini, fim):
    """
        reorganiza os elementos no intervalo das posições ini até fim;
        retorna a nova posição do pivô
    """

    # inicializar os cursores esquerdo e direito
    cursor_esq = ini
    cursor_dir = fim
    
    # enquanto os cursores esquerdo e direito não se cruzam
    while cursor_esq <= cursor_dir:
        # enquanto o valor apontado pelo cursor esquerdo for menor ou igual ao pivo
        while cursor_esq <= cursor_dir and v[cursor_esq] <= v[posicao_pivo]:
            # avançar o cursor esquerdo
            cursor_esq += 1
            
        # enquanto o valor apontado pelo cursor direito for maior ou igual ao pivo
        while cursor_esq <= cursor_dir and v[cursor_dir] >= v[posicao_pivo]:
            # "avançar" (da direita para a esquerda) o cursor direito
            cursor_dir -= 1
            
        # trocar os valores apontados pelos cursores
        if cursor_esq <= cursor_dir:
            v[cursor_esq], v[cursor_dir] = v[cursor_dir], v[cursor_esq]

    # posicionar o pivô entre as duas partições
    v[posicao_pivo], v[cursor_dir] = v[cursor_dir], v[posicao_pivo]

    # retornar a nova posição do pivô
    return cursor_dir