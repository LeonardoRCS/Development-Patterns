# --- SEM ITERATOR ---

class ColecaoCanais:
    def __init__(self):
        self.canais = ["HBO", "Globo", "SBT", "ESPN"]

# Cliente tentando percorrer
minha_tv = ColecaoCanais()
lista = minha_tv.canais

# O cliente precisa saber que é uma lista e usar índices
for i in range(len(lista)):
    print(f"Assistindo: {lista[i]}")