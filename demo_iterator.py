from collections.abc import Iterator, Iterable

# ==========================================
# CENÁRIO 1: JEITO ERRADO (EXPOSTO)
# ==========================================
print("\n--- 1. EXECUTANDO DO JEITO ERRADO (MANUAL) ---")

canais_lista = ["Globo", "SBT", "Band"]

print("   -> [CLIENTE]: Tenho que saber o tamanho da lista (len)...")
tamanho = len(canais_lista)
print(f"   -> [CLIENTE]: A lista tem tamanho {tamanho}. Vou criar um 'for' com índice.")

for i in range(tamanho):
    print(f"      -> Acessando índice [{i}]: {canais_lista[i]}")


# ==========================================
# CENÁRIO 2: JEITO CERTO (COM ITERATOR)
# ==========================================
print("\n--- 2. EXECUTANDO DO JEITO CERTO (ITERATOR) ---")

# Nossa coleção personalizada
class MinhaTV(Iterable):
    def __init__(self):
        self.canais = ["Discovery", "NatGeo", "History"]
    
    def __iter__(self):
        return CanalIterator(self.canais)

# Nosso Iterador (O "guia turístico" da coleção)
class CanalIterator(Iterator):
    def __init__(self, dados):
        self.dados = dados
        self.index = 0
    
    def __next__(self):
        if self.index < len(self.dados):
            valor = self.dados[self.index]
            self.index += 1
            print(f"   -> [ITERATOR]: Entregando o próximo item da pilha...")
            return valor
        else:
            print("   -> [ITERATOR]: Acabaram os itens. Parando.")
            raise StopIteration

# Uso
tv = MinhaTV()
print("   -> [CLIENTE]: Apenas peço o próximo. Não sei índice, nem tamanho.")

for canal in tv:
    print(f"      -> Assistindo: {canal}")