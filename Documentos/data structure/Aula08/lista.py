class Cliente:
    def __init__(self, nome, idade, endereco, email, telefone):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

    def exibir_info(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Endereço:", self.endereco)
        print("E-mail:", self.email)
        print("Telefone:", self.telefone)

    def atualizar_info(self, nome=None, idade=None, endereco=None, email=None, telefone=None):
        if nome:
            self.nome = nome
        if idade:
            self.idade = idade
        if endereco:
            self.endereco = endereco
        if email:
            self.email = email
        if telefone:
            self.telefone = telefone


class ListaClientesArray:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def remover_cliente(self, indice):
        if 0 <= indice < len(self.clientes):
            del self.clientes[indice]
        else:
            print("Índice inválido.")

    def atualizar_cliente(self, indice, **kwargs):
        if 0 <= indice < len(self.clientes):
            self.clientes[indice].atualizar_info(**kwargs)
        else:
            print("Índice inválido.")

    def listar_clientes(self):
        for i, cliente in enumerate(self.clientes):
            print("Cliente", i+1)
            cliente.exibir_info()


# Exemplo de utilização:

# Criando alguns clientes
cliente1 = Cliente("João", 30, "Rua A, 123", "joao@example.com", "123456789")
cliente2 = Cliente("Maria", 25, "Rua B, 456", "maria@example.com", "987654321")

# Criando uma lista de clientes usando arrays
lista_clientes = ListaClientesArray()

# Adicionando clientes à lista
lista_clientes.adicionar_cliente(cliente1)
lista_clientes.adicionar_cliente(cliente2)

# Listando os clientes
print("Lista de Clientes:")
lista_clientes.listar_clientes()

# Atualizando informações de um cliente
lista_clientes.atualizar_cliente(0, nome="João da Silva", idade=32)

# Removendo um cliente da lista
lista_clientes.remover_cliente(1)

# Listando os clientes após as operações
print("\nLista de Clientes Atualizada:")
lista_clientes.listar_clientes()
