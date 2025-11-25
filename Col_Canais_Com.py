# --- COM ITERATOR ---
from collections.abc import Iterator, Iterable

# 1. Iterador Concreto
class IteradorCanais(Iterator):
    def __init__(self, colecao):
        self._colecao = colecao
        self._indice = 0

    def __next__(self):
        try:
            valor = self._colecao[self._indice]
            self._indice += 1
            return valor
        except IndexError:
            raise StopIteration()

# 2. Coleção Iterável
class ColecaoCanais(Iterable):
    def __init__(self):
        self._canais = ["HBO", "Globo", "SBT", "ESPN"]

    def __iter__(self):
        return IteradorCanais(self._canais)

    def add_canal(self, canal):
        self._canais.append(canal)

# Uso (O cliente não acessa índices manualmente)
tv = ColecaoCanais()
tv.add_canal("Telecine")

print("Zapeando pelos canais:")
# O 'for' do Python usa o Iterator automaticamente por baixo dos panos
for canal in tv:
    print(f"📺 Assistindo: {canal}")