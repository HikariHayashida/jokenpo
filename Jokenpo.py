import random
import time

PLACAREMPATE = 0
PLACARVITORIA = 0
PLACARDERROTA = 0

def jogar_novamente():
    querJogar = str(input("Gostaria de jogar Jankepo? (sim/não): ")).lower().strip()
    if querJogar != "não":
        return jogo_jankepo()
    else:
        print("Obrigada por jogar, esse é um trabalho da disciplina de RA da aluna Hikari Hayashida Garbozza.")

def jogo_jankepo():
    global PLACAREMPATE
    global PLACARVITORIA
    global PLACARDERROTA

    print("O jogo já vai começar...")
    time.sleep(1)

    jogador = str(input("Você é humano ou computador? ")).lower().strip()

    oponente = str(input("Você vai jogar contra humano ou computador? ")).lower().strip()

    if jogador == "humano":
        print("Jogador1 escolha: pedra, papel ou tesoura?")
        escolhaJogador = str(input(":").lower().strip())

    if jogador == "computador":
        print("O computador está sorteando um valor...")
        time.sleep(2)
        escolhaJogador = random.randint(1, 3)
        if escolhaJogador == 1:
            escolhaJogador = "pedra"
        if escolhaJogador == 2:
            escolhaJogador = "papel"
        if escolhaJogador == 3:
            escolhaJogador = "tesoura"
        print("Escolha do computador: ")
        print(escolhaJogador)

    if oponente == "humano":
        print("Jogador2 escolha: pedra, papel ou tesoura?")
        escolhaOponente = str(input(":").lower().strip())

    if oponente == "computador":
        print("O computador está sorteando um valor")
        escolhaOponente = random.randint(1, 3)
        time.sleep(2)
        if escolhaOponente == 1:
            escolhaOponente = "pedra"
        if escolhaOponente == 2:
            escolhaOponente = "papel"
        if  escolhaOponente == 3:
            escolhaOponente = "tesoura"
        print("Escolha do computador: ")
        print(escolhaOponente)

    print("Jo...")
    time.sleep(1)
    print("Ken...")
    time.sleep(1)
    print("Po...")
    time.sleep(1)

    if (escolhaJogador == "pedra" and escolhaOponente == "pedra") or (escolhaJogador == "papel" and escolhaOponente == "papel") or (escolhaJogador == "tesoura" and escolhaOponente == "tesoura"):
        print("___________Empate!___________")
        PLACAREMPATE += 1

    if (escolhaJogador == "pedra" and escolhaOponente == "tesoura") or (escolhaJogador == "papel" and escolhaOponente == "pedra") or (escolhaJogador == "tesoura" and escolhaOponente == "papel"):
        print("___________Vitória!___________")
        PLACARVITORIA += 1

    if (escolhaJogador == "pedra" and escolhaOponente == "papel") or (escolhaJogador == "papel" and escolhaOponente == "tesoura") or (escolhaJogador == "tesoura" and escolhaOponente == "pedra"):
        print("___________Derrota!___________")
        PLACARDERROTA += 1

    print("Placar:")
    print("Vitórias:")
    print(PLACARVITORIA)
    print("Empates:")
    print(PLACAREMPATE)
    print("Derrotas:")
    print(PLACARDERROTA)

    jogar_novamente()


jogar_novamente()
