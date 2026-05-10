class Livro:
    def __init__(self, titulo, autor,isbn, paginas, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.ano_publicacao})"