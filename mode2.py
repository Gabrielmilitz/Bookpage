import pandas as pandinha


class Valdemort:
    def __init__(self, avadacadavra, cabecadedragao):
        self.avadacadavra = avadacadavra
        self.cabecadedragao = cabecadedragao

    def Olokomeu(self):
        varinha = pandinha.DataFrame(columns=["id", "nome_completo", "quantidade", "data"])

        while True:
            print("🎵 Música recomendada: Too Far Down the Trap - Vintage Culture")
            print("🎬 Filme recomendado: Harry Potter e o Cálice de Fogo")
           

          
            id_pessoas = input("Digite um id: ")
            nome = input("Digite o nome completo: ")
            quantia = input("Digite a quantidade: ")
            time = input("Digite a data: ")

            guarda_na_caixa = {
                "id": [id_pessoas],
                "nome_completo": [nome],
                "quantidade": [quantia],
                "data": [time],
            }

         
            varinha = pandinha.concat([varinha, pandinha.DataFrame(guarda_na_caixa)], ignore_index=True)

            print("\n✅ Registro na caixa de pandora efetuado!")
            print("\n🕒 Linha do tempo foi salva!")
            print("\n❌ Ares não curtiu isso!")
            print(varinha)

            
            mexe_mais = input("Deseja adicionar mais coisas na caixa? (y/n) ").strip().lower()
            if mexe_mais == "n":
                break

        
        varinha.to_csv("caixa_de_pandora.csv", index=False)
        print("\n📁 A caixa de pandora está disponível!")




        


               
        

            



        
