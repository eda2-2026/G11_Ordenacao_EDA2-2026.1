import streamlit as st
from livro import Livro
from service import insertion_sort, quick_sort
import pandas as pd

# Página centralizada e título da aba
st.set_page_config(page_title="Ordenação de Livros", layout="wide", initial_sidebar_state="expanded", page_icon=None)   

def make_key(attr):
    def key(l):
        val = getattr(l, attr, "")
        # Tranforma floats em string vazia para evitar erros de comparação, já que não esperamos floats nos atributos"
        if isinstance(val, float):
            val = ""
        # Normaliza strings para comparação e tenta converter números
        try:
            if isinstance(val, str):
                if attr in ("titulo", "isbn", "autor"):
                    return val.lower()
                return int(val) if val.isdigit() else val
            return val
        except Exception:
            return val

    return key


def livros_to_df(livros):
    return pd.DataFrame([
        {
            "titulo": l.titulo,
            "autor": l.autor,
            "isbn": l.isbn,
            "paginas": l.paginas,
            "ano_publicacao": l.ano_publicacao,
        }
        for l in livros
    ])


def main():
    # Carrega dados
    df = pd.read_csv("livros.csv", sep=";")

    df = df.rename(columns={"ano": "ano_publicacao"})

    livros = []
    for _, row in df.iterrows():
        livro = Livro(row["titulo"], row["autor"], row["isbn"], row["paginas"], row["ano_publicacao"])
        livros.append(livro)

    st.title("Ordenação de Livros", anchor=None)

    st.divider()    

    a,b = st.columns(2)

    with a:
        st.header("Opções")
        sort_choice = st.selectbox(
        "Ordenar por:",
        ("Nome", "ISBN", "Páginas", "Ano de publicação", "Autor"),
        index=0,
        )
    
    with b:

                # Escolha do algoritmo de ordenação
        algo = st.radio("Algoritmo:", ("Quick Sort", "Insertion Sort"), index=0)

        ordenar = st.button("Ordenar")

    st.divider()


    # Mapeamento dos rótulos para atributos
    map_attr = {
        "Nome": "titulo",
        "ISBN": "isbn",
        "Páginas": "paginas",
        "Ano de publicação": "ano_publicacao",
        "Autor": "autor",
    }

    attr = map_attr[sort_choice]

    # Mostra antes e depois em duas colunas
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("Antes")
        st.dataframe(df.reset_index(drop=True))

    with col2:
        st.subheader("Depois")
        if ordenar:
            # copia para não alterar a lista original
            livros_copy = livros.copy()
            key = make_key(attr)
            if algo == "Quick Sort":
                sorted_livros = quick_sort(livros_copy, key=key)
            else:
                # insertion_sort ordena in-place
                insertion_sort(livros_copy, key=key)
                sorted_livros = livros_copy

            df_sorted = livros_to_df(sorted_livros)
            st.dataframe(df_sorted.reset_index(drop=True))
        else:
            st.caption("Clique em 'Ordenar' no menu lateral para ver o resultado")
            st.dataframe(pd.DataFrame(columns=df.columns))


if __name__ == "__main__":
    main()