# banda.py
from musico import Musico
from album import Album

class Banda:
    def __init__(self, nome):
        self.nome = nome
        self.musicos = []
        self.albums = []

    def adicionar_musico(self, musico):
        self.musicos.append(musico)

    def adicionar_album(self, album):
        self.albums.append(album)

    def mostrar_musicos(self):
        print(f'Banda: {self.nome}')
        for musico in self.musicos:
            musico.mostrar_info()

    def mostrar_albums(self):
        print(f'Álbuns da Banda {self.nome}:')
        for album in self.albums:
            album.mostrar_info()

