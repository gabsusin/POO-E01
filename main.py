# main.py
from banda import Banda
from musico import Musico
from instrumento import Guitarra, Bateria
from album import Album

# Criando instrumentos
guitarra = Guitarra('Fender Stratocaster', 'Cordas', 6)
bateria = Bateria('Yamaha Stage Custom', 'Percussão', 5)

# Criando músicos com instrumentos
musico1 = Musico('John', guitarra)
musico2 = Musico('Ringo', bateria)

# Criando álbuns e adicionando faixas
album1 = Album('Abbey Road', 1969)
album1.adicionar_faixa('Come Together')
album1.adicionar_faixa('Something')
album1.adicionar_faixa('Maxwell\'s Silver Hammer')
album2 = Album('Sgt. Pepper\'s Lonely Hearts Club Band', 1967)
album2.adicionar_faixa('Lucy in the Sky with Diamonds')
album2.adicionar_faixa('With a Little Help from My Friends')
album2.adicionar_faixa('A Day in the Life')

# Criando banda e adicionando músicos e álbuns
banda = Banda('The Beatles')
banda.adicionar_musico(musico1)
banda.adicionar_musico(musico2)
banda.adicionar_album(album1)
banda.adicionar_album(album2)

# Exibindo informações da banda e dos álbun
banda.()
banda.mostrar_albums()
