import heapq
from datetime import datetime

class Pessoa:
    def __init__(self, nome, idade, tipo_deficiencia=None, condicao_especial=None):
        self.nome = nome
        self.idade = idade
        self.tipo_deficiencia = tipo_deficiencia  # Ex: "visual", "auditiva", etc.
        self.condicao_especial = condicao_especial  # Ex: "gestante", "lactante"
        self.data_chegada = datetime.now()
        self.prioridade = self.calcular_prioridade()
    
    def calcular_prioridade(self):
        if self.tipo_deficiencia:
            return 1
        elif self.idade >= 60 or self.condicao_especial in ['gestante', 'lactante']:
            return 2
        else:
            return 3

    def __str__(self):
        return f"{self.nome} | Idade: {self.idade} | Prioridade: {self.prioridade}"

# Fila de prioridade usando heapq (menor valor = mais prioridade)
class FilaPrioridade:
    def __init__(self):
        self.fila = []
        self.contador = 0  # Para desempate por ordem de chegada

    def adicionar_pessoa(self, pessoa):
        heapq.heappush(self.fila, (pessoa.prioridade, self.contador, pessoa))
        self.contador += 1

    def visualizar_fila(self):
        print("\nFila atual de atendimento (por prioridade):")
        for prioridade, _, pessoa in sorted(self.fila):
            print(pessoa)

    def atender_proxima(self):
        if self.fila:
            _, _, pessoa = heapq.heappop(self.fila)
            print(f"\n🔔 Próxima pessoa a ser atendida: {pessoa.nome} (Prioridade {pessoa.prioridade})")
        else:
            print("\n✅ Fila vazia.")

fila = FilaPrioridade()

p1 = Pessoa("edson", 21)
p2 = Pessoa("ana", 61)
p3 = Pessoa("paulo", 22, tipo_deficiencia="cadeirante")
p4 = Pessoa("maria", 25, condicao_especial="gestante")

fila.adicionar_pessoa(p1)
fila.adicionar_pessoa(p3)
fila.adicionar_pessoa(p4)
fila.adicionar_pessoa(p2)
fila.visualizar_fila()
fila.atender_proxima()
fila.atender_proxima()
fila.atender_proxima()
fila.atender_proxima()
fila.atender_proxima()




