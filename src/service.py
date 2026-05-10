# Algoritmos de ordenação para livros

# Insertion Sort
def insertion_sort(livros, key=lambda x: x.titulo):
    # Percorre a lista de livros a partir do segundo elemento
    for i in range(1, len(livros)):
        # Armazena o livro atual como chave
        chave = livros[i]
        # Move os elementos da lista que são maiores que a chave para uma posição à frente
        j = i - 1
        # Compara a chave com os elementos anteriores e move-os para a direita até encontrar a posição correta
        while j >= 0 and key(livros[j]) > key(chave):
            # Move o livro para a direita
            livros[j + 1] = livros[j]
            # Decrementa o índice para continuar comparando com os elementos anteriores
            j -= 1
        # Insere a chave na posição correta
        livros[j + 1] = chave
