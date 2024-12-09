class Cliente:
    def __init__(self, nome, operacao):
        self.nome = nome
        self.operacao = operacao
        
class NoCliente:
    def __init__(self, cliente):
        self.cliente = cliente
        self.proximo = None

class SistemaAtendimentoBanco:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def adicionar_cliente(self, cliente):
        novo_no = NoCliente(cliente)
        if self.primeiro is None:
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no
        print(f"Cliente {cliente.nome} adicionado à fila.")

    def atender_proximo_cliente(self):
        if self.primeiro is not None:
            cliente_atendido = self.primeiro.cliente
            self.primeiro = self.primeiro.proximo
            print(f"Atendendo cliente {cliente_atendido.nome} para operação de {cliente_atendido.operacao}.")
        else:
            print("Não há clientes na fila para atendimento.")

    def exibir_fila(self):
        if self.primeiro is None:
            print("Não há clientes na fila.")
        else:
            print("Fila de clientes:")
            atual = self.primeiro
            while atual:
                print(f"{atual.cliente.nome} - Operação: {atual.cliente.operacao}")
                atual = atual.proximo

# Exemplo de utilização:

sistema_banco = SistemaAtendimentoBanco()

# Adicionando clientes à fila
sistema_banco.adicionar_cliente(Cliente("João", "saque"))
sistema_banco.adicionar_cliente(Cliente("Maria", "depósito"))
sistema_banco.adicionar_cliente(Cliente("Pedro", "consulta"))

# Exibindo a fila de clientes
sistema_banco.exibir_fila()

# Atendendo o próximo cliente
sistema_banco.atender_proximo_cliente()

# Exibindo a fila após o atendimento
sistema_banco.exibir_fila()
