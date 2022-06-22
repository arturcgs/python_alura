
class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    def __str__(self):
        return f'Nome: {self._nome} | Ano: {self._ano} | Duração: {self.duracao} min | Likes: {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    def __str__(self):
        return f'Nome: {self._nome} | Ano: {self._ano} | Temporadas: {self.temporadas} min | Likes: {self._likes}'

class Playlist():
    def __init__(self, nome, shows):
        self.nome = nome
        self.shows = shows
    def __getitem__(self, item):
        return shows[item]
    def __len__(self):
        return len(self.shows)

vingadores = Filme('vingadores: guerra infinita', 2018, 160)
breaking_bad = Serie('breaking bad', 2015, 5)
bojack = Serie('bojack horseman', 2016, 5)
interstellar = Filme('inter-estelar', 2014, 130)

#likes
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()
breaking_bad.dar_like()
bojack.dar_like()
bojack.dar_like()
bojack.dar_like()
bojack.dar_like()
bojack.dar_like()
interstellar.dar_like()
interstellar.dar_like()
interstellar.dar_like()

shows = [vingadores, breaking_bad, bojack, interstellar]
playlist_fds = Playlist('Playlist final de semana', shows)

print(f'A playlist tem {len(playlist_fds)} itens')
for show in playlist_fds:
    print(show)