from abc import ABC, abstractmethod

# ==========================================
# CENÁRIO 1: JEITO ERRADO (ACOPLADO)
# ==========================================
print("\n--- 1. EXECUTANDO DO JEITO ERRADO (SEM COMMAND) ---")

class LuzSimples:
    def ligar(self):
        print("   -> [LUZ]: Luz acesa!")

class BotaoSimples:
    def __init__(self, luz):
        self.luz = luz
    
    def click(self):
        print("   -> [BOTÃO]: Eu conheço a classe Luz. Chamando luz.ligar() direto...")
        self.luz.ligar()

# Teste Errado
luz = LuzSimples()
botao = BotaoSimples(luz)
botao.click()


# ==========================================
# CENÁRIO 2: JEITO CERTO (COM COMMAND)
# ==========================================
print("\n--- 2. EXECUTANDO DO JEITO CERTO (COM COMMAND) ---")

# Interface
class IComando(ABC):
    @abstractmethod
    def executar(self):
        pass

# Receiver (Quem faz)
class LuzInteligente:
    def ligar(self):
        print("   -> [RECEIVER/LUZ]: Luz acesa (eu nem sei quem apertou o botão!)")

# Command (O envelope)
class LigarLuzCommand(IComando):
    def __init__(self, luz):
        self.luz = luz
    
    def executar(self):
        print("   -> [COMMAND]: Recebi o pedido. Agora vou mandar a Luz ligar.")
        self.luz.ligar()

# Invoker (Quem pede)
class ControleRemoto:
    def __init__(self):
        self.comando = None
    
    def set_comando(self, comando):
        self.comando = comando
    
    def apertar_botao(self):
        print("   -> [INVOKER/CONTROLE]: Botão apertado! Executando o comando genérico...")
        if self.comando:
            self.comando.executar()

# Teste Certo
luz_smart = LuzInteligente()
comando = LigarLuzCommand(luz_smart)
controle = ControleRemoto()

controle.set_comando(comando)
controle.apertar_botao()