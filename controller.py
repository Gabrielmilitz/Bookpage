from model import *
from csvconvert import *

def main():
    try:
        app = Bookpage()
        app.exibir_menu()
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
