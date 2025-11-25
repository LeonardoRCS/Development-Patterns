# --- COM COMMAND ---
from abc import ABC, abstractmethod

# 1. Interface do Comando
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# 2. Receiver (Quem faz o trabalho real)
class Luz:
    def ligar(self):
        print("💡 A luz foi ligada via Command!")

# 3. Concrete Command (O envelope do pedido)
class LigarLuzCommand(Command):
    def __init__(self, luz):
        self.luz = luz

    def execute(self):
        self.luz.ligar()

# 4. Invoker (Quem dispara, ex: controle remoto)
class Botao:
    def __init__(self):
        self.comando = None

    def set_comando(self, comando):
        self.comando = comando

    def pressionar(self):
        if self.comando:
            self.comando.execute()

# Uso
luz_sala = Luz()                 # O Receiver
comando_luz = LigarLuzCommand(luz_sala) # O Comando encapsulado
botao = Botao()                  # O Invoker

botao.set_comando(comando_luz)   # Configura
botao.pressionar()               # Dispara