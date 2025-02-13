import random

players_aliens = [
    "Mago Xylox", "Dragão Cósmico de Olhos Brilhantes", "Caçador Estelar Voraz", "Exodia, o Devastador de Mundos", "Obelisco, o Senhor do Caos",
    "Slifer, o Senhor do Trovão Cósmico", "Cavaleiro da Ruína Galáctica", "Espectro Sombrio de Nébula", "Colosso Titânico da Aniquilação", 
    "Sombra do Eclipse Supremo", "Imperador Abissal", "Titã Devastador de Sistemas", "Gorz, o Mensageiro do Fim", "Onda de Terror Estelar", 
    "Flagelo Cósmico", "Horror das Dimensões Perdidas", "Ryu, o Espectro Voraz", "Senhor do Vácuo Infinito", "Jinzo, o Paranoico Cibernético", 
    "Feiticeiro do Vazio Absoluto", "Guardião das Estrelas Mortas", "Dragão Apocalíptico Metálico", "Cyber-Vortex.exe", "Dragão Supremo da Obliteração", 
    "Paladino do Eclipse", "Destruidor do Firewall Celestial", "General do Império Sombrio", "Xenofear, o Infinitamente Perdido", "Xylox, o Arcano", 
    "Grande Parasita Nebuloso", "O Criador do Nada", "Saqueador das Galáxias Perdidas", "Ser Supremo da Fusão Cósmica", "Filhote do Caos Ancestral", 
    "Dama da Morte Cibernética", "Corrente da Entropia", "Lorde Devastador de Planetas", "Zork, o Governante do Vazio", "Beelze, o Deus Exterminador"
]

players_humanos = [
    "General Titanblade", "Sentinela de Ferro", "Arqueiro Celestial", "Cavaleiro do Amanhecer", "Dragão Guardião de Gaia", 
    "Guardião da Fortaleza de Aço", "Pegasus Dourado", "Feiticeira Suprema", "Gladiador de Elite", "Comandante da Luz", 
    "Batedor Fantasma", "Templário de Elite", "Águia Veloz", "Rex, o Guerreiro Primordial", "Líder da Frota Estelar", 
    "Mestre da Forja", "Paladino do Reino", "Místico do Céu", "Defensor do Povo", "Barão do Trovão", 
    "Campeão do Reino", "Guerreiro do Destino", "Titã do Campo de Batalha", "Berserker de Elite", "Monge Guerreiro", 
    "Número 39: Utopia Suprema", "Cavaleiro Dourado", "Domador de Bestas", "Vingador Sombrio", "Colosso de Adamantium", 
    "Guardiã das Chamas", "Ave Fênix do Norte", "Escudeiro da Luz", "Guerreiro da Tempestade", "Zelador da Justiça", 
    "Vento Cortante", "Titã da Guerra", "Mestre da Espada Sagrada", "Soberano da Arena", "Assassino do Caos"
]

class Guerreiro:
    def __init__(self, nome, espada, escudo, forca, velocidade, magia, vida=100):
        self.nome = nome
        self.espada = espada
        self.escudo = escudo
        self.forca = forca
        self.velocidade = velocidade
        self.magia = magia
        self.vida = vida

    def atacar(self, inimigo):
        dano = random.randint(10, 20) if self.espada else random.randint(5, 10)
        if inimigo.escudo:
            dano //= 2  
        inimigo.vida -= dano
        print(f"{self.nome} ataca {inimigo.nome} causando {dano} de dano!")

    def defender(self):
        defesa = random.randint(1, 5)
        self.vida += defesa
        print(f"{self.nome} se defende e recupera {defesa} de vida!")

class Alien(Guerreiro):
    def __init__(self, nome):
        super().__init__(nome, espada=True, escudo=False, forca=True, velocidade=True, magia=False)

    def rugido_de_guerra(self, inimigo):
        print(f"{self.nome} usa Rugido de Guerra! O inimigo {inimigo.nome} fica atordoado!")
        inimigo.vida -= 1  

class Humanos(Guerreiro):
    def __init__(self, nome):
        super().__init__(nome, espada=True, escudo=True, forca=True, velocidade=False, magia=True)

    def magia_sagrada(self):
        cura = random.randint(1, 5)
        self.vida += cura
        print(f"{self.nome} usa Magia Sagrada e recupera {cura} de vida!")

def escolher_acao(guerreiro, inimigo):
    print("\nEscolha sua ação:")
    print("1 - Atacar")
    print("2 - Defender")
    if isinstance(guerreiro, Humanos): 
        print("3 - Poder especial sagrado")
    elif isinstance(guerreiro, Alien):
        print("3 - Rugido de Guerra")
    
    escolha = input("Digite o número da ação: ")
    
    if escolha == "1":
        guerreiro.atacar(inimigo)
    elif escolha == "2":
        guerreiro.defender()
    elif escolha == "3":
        if isinstance(guerreiro, Humanos):
            guerreiro.magia_sagrada()
        elif isinstance(guerreiro, Alien):
            guerreiro.rugido_de_guerra(inimigo)
    else:
        print("Opção inválida! Você perdeu sua vez.")

def batalha(jogador, inimigo):
    while jogador.vida > 0 and inimigo.vida > 0:
        print("\n----- NOVO TURNO -----")
        print(f"{jogador.nome}: {jogador.vida} de vida | {inimigo.nome}: {inimigo.vida} de vida")
        
        escolher_acao(jogador, inimigo)
        if inimigo.vida <= 0:
            print(f"\n{inimigo.nome} foi derrotado! Você venceu!")
            return False

        acao_inimigo = random.choice(["atacar", "defender"])
        if acao_inimigo == "atacar":
            inimigo.atacar(jogador)
        else:
            inimigo.defender()
        
        if jogador.vida <= 0:
            print(f'''"{jogador.nome} foi derrotado!"


███████╗ █████╗ ████████╗ █████╗ ██╗     ██╗████████╗██╗   ██╗
██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██║     ██║╚══██╔══╝╚██╗ ██╔╝
█████╗  ███████║   ██║   ███████║██║     ██║   ██║    ╚████╔╝ 
██╔══╝  ██╔══██║   ██║   ██╔══██║██║     ██║   ██║     ╚██╔╝
██     ╗██║  ██║   ██║   ██║  ██║███████╗██║   ██║      ██║   
╚      ╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝      ╚═╝   
''')
            return False
    
    return True


while True:
    print("\nWARRIORS VS ALIENS")
    print("Escolha sua facção:")
    print("1 - Humanos")
    print("2 - Aliens")
    escolha_faccao = input("Digite o número da sua escolha: ")

    if escolha_faccao == "1":
        jogador = Humanos(random.choice(players_humanos))
        inimigo = Alien(random.choice(players_aliens))
    else:
        jogador = Alien(random.choice(players_aliens))
        inimigo = Humanos(random.choice(players_humanos))

    print(f"\n VOCÊ: {jogador.nome} | INIMIGO: {inimigo.nome}")

    while batalha(jogador, inimigo):
        print("\nNovo jogo iniciado!")

    

