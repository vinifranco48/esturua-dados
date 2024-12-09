class Cliente:
    def __init__(self, nome, idade, endereco, email, telefone):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.email = email
        self.telefone = telefone
        self.proximo = None

class ListaClientesEncadeada:
    def __init__(self):
        self.primeiro = None

    def adicionar_cliente(self, cliente):
        if self.primeiro is None:
            self.primeiro = cliente
        else:
            atual = self.primeiro
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = cliente

    def remover_cliente(self, nome):
        if self.primeiro is None:
            print("Lista vazia. Não há clientes para remover.")
            return

        if self.primeiro.nome == nome:
            self.primeiro = self.primeiro.proximo
            print(f"Cliente {nome} removido com sucesso.")
            return

        anterior = self.primeiro
        atual = self.primeiro.proximo
        while atual is not None:
            if atual.nome == nome:
                anterior.proximo = atual.proximo
                print(f"Cliente {nome} removido com sucesso.")
                return
            anterior = atual
            atual = atual.proximo

        print(f"Cliente {nome} não encontrado na lista.")

    def atualizar_cliente(self, nome, **kwargs):
        if self.primeiro is None:
            print("Lista vazia. Não há clientes para atualizar.")
            return

        atual = self.primeiro
        while atual is not None:
            if atual.nome == nome:
                for key, value in kwargs.items():
                    setattr(atual, key, value)
                print(f"Informações do cliente {nome} atualizadas com sucesso.")
                return
            atual = atual.proximo

        print(f"Cliente {nome} não encontrado na lista.")

    def listar_clientes(self):
        if self.primeiro is None:
            print("Lista vazia. Não há clientes para exibir.")
            return

        print("Lista de Clientes:")
        atual = self.primeiro
        while atual is not None:
            print("Nome:", atual.nome)
            print("Idade:", atual.idade)
            print("Endereço:", atual.endereco)
            print("E-mail:", atual.email)
            print("Telefone:", atual.telefone)
            print("-----------------------------")
            atual = atual.proximo


# Exemplo de utilização:

# Criando uma lista encadeada de clientes
lista_clientes = ListaClientesEncadeada()

# Adicionando alguns clientes à lista
cliente1 = Cliente("João", 30, "Rua A, 123", "joao@example.com", "123456789")
cliente2 = Cliente("Maria", 25, "Rua B, 456", "maria@example.com", "987654321")
lista_clientes.adicionar_cliente(cliente1)
lista_clientes.adicionar_cliente(cliente2)

# Listando os clientes
lista_clientes.listar_clientes()

# Atualizando informações de um cliente
lista_clientes.atualizar_cliente("João", idade=32)

# Removendo um cliente da lista
lista_clientes.remover_cliente("Maria")

# Listando os clientes após as operações
lista_clientes.listar_clientes()
