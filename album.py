# album.py
class Album:
    def __init__(self, titulo, ano_lancamento):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento
        self.faixas = []

    def adicionar_faixa(self, faixa):
        self.faixas.append(faixa)

    def mostrar_info(self):
        print(f'Álbum: {self.titulo}, Ano de Lançamento: {self.ano_lancamento}')
        print('Faixas:')
        for faixa in self.faixas:
            print(f'- {faixa}')
