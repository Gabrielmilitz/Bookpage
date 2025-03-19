import os
import json
from csvconvert import *
from mode2 import  *

class Bookpage:
    def __init__(self):
        self.lista = []
        self.respostas = {}

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def adicionar_conteudo(self):
        usuario = input("\033[1;33m➡️  O que você gostaria de adicionar ao Bookpage? \033[0m")
        conteudo = input("\033[1;33m➡️  Qual conteúdo gostaria de compartilhar com esse novo tópico? \033[0m")

        if usuario not in self.lista:
            print("\033[1;32m✔️  Conteúdo verificado: não existe\033[0m")
            self.lista.append(usuario)
            self.respostas[usuario] = conteudo
            print("\033[1;32m✔️  O conteúdo foi armazenado com sucesso no seu Bookpage.\033[0m")
        else:
            print("\033[1;31m❌ Este tópico já existe no Bookpage.\033[0m")

    def remover_conteudo(self):
        escolha = input("\033[1;33m➡️  Qual item deseja remover? \033[0m")
        if escolha in self.lista:
            self.lista.remove(escolha)
            self.respostas.pop(escolha, None)
            print(f"\033[1;32m✔️  O item '{escolha}' foi removido com sucesso.\033[0m")
        else:
            print("\033[1;31m❌ Este item não existe no Bookpage.\033[0m")

    def exibir_conteudo(self):
        if not self.lista:
            print("\033[1;31m❌ O Bookpage está vazio.\033[0m")
            return

        print("\033[1;34m📚 Tópicos do Bookpage:\033[0m")
        for i, item in enumerate(self.lista, 1):
            print(f"{i}. {item}")

    def exibir_detalhes(self):
        exibir = input("\033[1;33m➡️  Digite um tópico do Bookpage para ver as informações: \033[0m")
        if exibir in self.respostas:
            print(f"\033[1;34m📖 Conteúdo de '{exibir}': {self.respostas[exibir]}\033[0m")
        else:
            print("\033[1;31m❌ Este tópico não existe no Bookpage.\033[0m")

    def exportar_json(self):
        dados = {"x": self.lista, "y": self.respostas}
        try:
            with open("dados.json", "w", encoding="utf-8") as file:  
                json.dump(dados, file, indent=4, ensure_ascii=False)
                print("\033[1;32m✔️  Arquivo JSON exportado com sucesso.\033[0m")
        except PermissionError:
            print("\033[1;31m❌ Permissão negada. Não foi possível salvar o arquivo JSON.\033[0m")

    def exibir_menu(self):
        while True:
            self.limpar_tela()
            print("\033[1;36m" + "=" * 50 + "\033[0m")
            print("\033[1;33m" + "📚 BEM-VINDO AO BOOKPAGE".center(50) + "\033[0m")
            print("\033[1;36m" + "=" * 50 + "\033[0m")

            print("\033[1;32m" + "[1]" + "\033[0m" + " 📖 Exibir Bookpage")
            print("\033[1;32m" + "[2]" + "\033[0m" + " ❌ Remover item do Bookpage")
            print("\033[1;32m" + "[3]" + "\033[0m" + " 📚 Exibir conteúdo")
            print("\033[1;32m" + "[4]" + "\033[0m" + " 📤 Exportar Bookpage para JSON")
            print("\033[1;32m" + "[5]" + "\033[0m" + " ➕ Adicionar ao Bookpage")
            print("\033[1;32m" + "[6]" + "\033[0m" + " 💹 Converter Excel")
            print("\033[1;32m" + "[7]" + "\033[0m" + " 🏮 Caixa de Pandora")
            print("\033[1;32m" + "[8]" + "\033[0m" + " 🚪 Sair do programa")

            print("\033[1;34m" + "=" * 50 + "\033[0m")
            print("\033[1;35m" + "      📚 Version 1.4".rjust(40) + "\033[0m")
            print("\033[1;35m" + "    @angelusdev".rjust(40) + "\033[0m")
            print("\033[1;35m" + "    gabrielmarinmilitz@gmail.com".rjust(40) + "\033[0m")
            print("\033[1;34m" + "=" * 50 + "\033[0m")

            opcao = input("\033[1;33m➡️  Escolha uma opção: \033[0m")

            if opcao == '1':
                self.exibir_conteudo()
            elif opcao == '2':
                self.remover_conteudo()
            elif opcao == '3':
                self.exibir_detalhes()
            elif opcao == '4':
                self.exportar_json()
            elif opcao == '5':
                self.adicionar_conteudo()

            elif opcao == '6':
                converter = ConverterCSV('dados.json', 'dados.csv')  
                converter.converter()
            elif opcao == '7':
                voldy = Valdemort("Expelliarmus", "anhadaa kadavraa")
                voldy.Olokomeu()


            elif opcao == "8":
                print("\033[1;31m🚪 Saindo do programa... Até logo!\033[0m")
                break


            else:
                print("\033[1;31m❌ Opção inválida. Tente novamente.\033[0m")

            input("\033[1;36m\nPressione ENTER para continuar...\033[0m")

if __name__ == '__main__':
    app = Bookpage()
    app.exibir_menu()
