class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class NavegadorWeb:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def visitar_link(self, link):
        novo_no = No(link)
        if self.primeiro is None:
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no

    def voltar_pagina(self):
        if self.primeiro != self.ultimo:
            atual = self.primeiro
            while atual.proximo != self.ultimo:
                atual = atual.proximo
            atual.proximo = None
            self.ultimo = atual
        else:
            print("Não há páginas anteriores para voltar.")

    def exibir_historico(self):
        if self.primeiro is None:
            print("Histórico de navegação vazio.")
        else:
            print("Histórico de Navegação:")
            atual = self.primeiro
            while atual:
                print("-", atual.dado)
                atual = atual.proximo

# Exemplo de utilização:

navegador = NavegadorWeb()

# Visitando alguns links
navegador.visitar_link("https://www.google.com")
navegador.visitar_link("https://www.openai.com")
navegador.visitar_link("https://www.github.com")

# Exibindo o histórico de navegação
navegador.exibir_historico()

# Voltando para a página anterior
navegador.voltar_pagina()

# Exibindo o histórico de navegação novamente
navegador.exibir_historico()
