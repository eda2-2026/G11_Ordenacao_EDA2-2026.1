# G11-Busca-2026-01 - Order Book

**Número da Lista**: 11<br>
**Conteúdo da Disciplina**: Algoritmos de Ordenação<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 22/1007706  |  Elias Faria de Oliveira |
| 211031403 | Marcus Vinicius Cunha Dantas|

## Sobre

Este é um projeto acadêmico desenvolvido para a disciplina **EDA2 (Estruturas de Dados e Algoritmos 2)** da Universidade de Brasília. 

O objetivo é aprender e comparar **algoritmos de ordenação** através de uma aplicação prática que ordena uma coleção de livros por diferentes critérios (nome, ISBN, páginas, ano de publicação), utilizando dois algoritmos clássicos: **Insertion Sort** e **Quick Sort**.

## Base de dados

A base de dados utilizada é um dataset com aproximadamente 11 mil registros de livros com os campos: nome, isbn, páginas e ano de publicação.

[Base de dados](https://www.kaggle.com/datasets/diegomariano/tabela-de-livros?resource=download)

## Estrutura do Projeto

```
src/
├── livro.py          # Classe que representa um livro
├── order_livros.py   # Interface Streamlit
└── service.py        # Implementação dos algoritmos de ordenação

livros.csv           # Base de dados dos livros
requirements.txt     # Dependências do projeto
```

## Como Rodar Localmente

### Pré-requisitos
- Python 3.7+
- pip

### Passos de Instalação

1. **Clone ou navegue até o diretório do projeto:**
   ```bash
   cd /home/elias/UnB/EDA2/G11-Ordenacao-2026-01
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação Streamlit:**
   ```bash
   streamlit run src/order_livros.py
   ```

4. **Acesse a aplicação:**
   - A aplicação abrirá automaticamente em `http://localhost:8501`
   - Se não abrir, acesse manualmente pelo navegador

### Uso da Aplicação

1. No menu à esquerda, selecione o critério de ordenação:
   - **Nome**: ordena alfabeticamente pelo título
   - **ISBN**: ordena pelo código ISBN
   - **Páginas**: ordena pela quantidade de páginas
   - **Ano de publicação**: ordena pelo ano de lançamento
   - **Autor**: ordena pelo nome do autor

2. Escolha o algoritmo:
   - **Quick Sort**: mais rápido em média
   - **Insertion Sort**: mais simples de entender

3. Clique no botão **"Ordenar"** para visualizar os resultados

A aplicação mostra lado a lado a lista **antes** e **depois** da ordenação.

## Aplicação

![web_aplication](./assets/image.png)

## Link da Gravação

[Gravação](link da gravação)


## Algoritmos Implementados

### Insertion Sort
- Complexidade: O(n²) no pior caso
- Simples e intuitivo
- Bom para listas pequenas
- Ordena a lista de forma decrescente, trazendo as maiores chaves para o início da lista(nesta implementação)

### Quick Sort
- Complexidade: O(n log n) em média, O(n²) no pior caso
- Mais eficiente em listas grandes
- Implementação com pivô na mediana
