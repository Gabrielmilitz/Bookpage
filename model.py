import json

class Adicao:
    def __init__(self):
     
        self.lista = []
        self.respostas = {}

    def adicionar_conteudo(self):
        
        usuario = input("O que você gostaria de adicionar ao Bookpage? ")
        conteudo = input("Qual conteúdo gostaria de compartilhar com esse novo tópico? ")

        
        if usuario not in self.lista:
            if usuario not in self.respostas:
                print("Conteúdo verificado: não existe")
                self.lista.append(usuario)
                self.respostas[usuario] = conteudo
                print("O conteúdo foi armazenado com sucesso no seu Bookpage.")
            else:
                print("Este conteúdo já existe.")
        else:
            print("Este tópico já existe no Bookpage.")


class Exibir:
    def __init__(self, adicao):
        
        self.adicao = adicao
        self.exibir_existente()

    def exibir_existente(self):
        """
        Menu interativo para visualizar, remover e exportar os dados.
        """
        while True:
            print('''
                ========================
                BEM-VINDO AO BOOKPAGE 🟡
                
                (1) Exibir Bookpage ✅
                (2) Remover item do Bookpage ✅
                (3) Exibir conteúdo ✅
                (4) Exportar Bookpage para JSON ✅
                (5) Adicionar ao Bookpage ✅
                (6) Sair do programa ✅
                ========================
                  Version 1.0
                  @angelusdev 
                  @gabrielmarinmilitz@gmail.com
                
            ''')

            try:
                usuario = int(input("Digite uma das opções acima: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            if usuario == 1:
                print("Tópicos do Bookpage:", self.adicao.lista)

            elif usuario == 2:
                escolha = input("Qual item deseja remover? ")
                if escolha in self.adicao.lista:
                    self.adicao.lista.remove(escolha)
                    self.adicao.respostas.pop(escolha, None)
                    print(f"O item '{escolha}' foi removido com sucesso.")
                else:
                    print("Este item não existe no Bookpage.")

            elif usuario == 3:
                exibir = input("Digite um tópico do Bookpage para ver as informações: ")
                if exibir in self.adicao.lista:
                    print(f"Conteúdo de '{exibir}':", self.adicao.respostas[exibir])
                else:
                    print("Este tópico não existe no Bookpage.")

            elif usuario == 4:
                dados = {
                    "x": self.adicao.lista,
                    "y": self.adicao.respostas
                }
                with open("dados.json", "w", encoding="utf-8") as file:
                    json.dump(dados, file, indent=4, ensure_ascii=False)
                    print("Arquivo JSON exportado com sucesso.")

            elif usuario == 5:
                self.adicao.adicionar_conteudo()


            elif usuario == 6:
                print("Saindo do programa...")
                break

            else:
                print("Opção inválida. Tente novamente.")


          

            