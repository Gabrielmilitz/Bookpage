import json
import csv 

class ConverterCSV:
    def __init__(self, caminho_json, csv_caminho):
        self.caminho_json = caminho_json  
        self.csv_caminho = csv_caminho  

    def converter(self):
        try:
            with open(self.caminho_json, "r", encoding="utf-8") as jsonfile:
                data = json.load(jsonfile) 

                
                if "y" in data and isinstance(data["y"], dict):  
                    dados_para_csv = [{"x": chave, "y": valor} for chave, valor in data["y"].items()]
                else:
                    raise ValueError("Formato de dados inesperado na chave 'y'")

                # Escreve os dados no CSV
                with open(self.csv_caminho, "w", newline='', encoding='utf-8') as csv_file:
                    escrita = csv.DictWriter(csv_file, fieldnames=["x", "y"])  
                    escrita.writeheader()
                    escrita.writerows(dados_para_csv)

                print(f"Conversão realizada: {self.csv_caminho}")

        except Exception as e:
            print(f"Erro na conversão: {e}")
