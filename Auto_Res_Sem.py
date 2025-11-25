# --- SEM COMMAND ---

class Luz:
    def ligar(self):
        print("A luz foi ligada!")

class Botao:
    def __init__(self, luz):
        self.luz = luz  # Acoplamento direto!

    def pressionar(self):
        # O botão sabe EXATAMENTE o que fazer com a luz
        self.luz.ligar()

# Uso
luz_sala = Luz()
botao = Botao(luz_sala)
botao.pressionar()