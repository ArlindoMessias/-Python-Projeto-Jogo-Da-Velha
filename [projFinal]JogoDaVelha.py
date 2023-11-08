#Funções do jogo

#criação do tabuleiro
def novoTabuleiro():
  tab = [0, 0,  0,
         0, 0,  0,
         0, 0,  0,]

  return tab

#exibe o tabuleiro criado
def exibirTabuleiro(tabuleiro):
    for id, valor in enumerate(tabuleiro, start=1):

      if valor == 0: #verifica o conteudo das posições
        print(" ", id, sep="", end='')
      elif valor==1:
        print(" X", end='')
      else:
        print(" O", end='')

      if id==3 or id==6:#quebra de linha ao chegar no elemento 3/6
        print("\n---+---+---\n", end='')
      elif  id<9:
        print(" |", end='')

    print("\n")

#recebe a posição da jogada
def recebeJogada(jogador):
  try: 
      jogada = int(input('Digite a posição de jogada 1-9 (jogador %s): ' %(jogador)))
      return jogada

  except ValueError:
      print("Entrada inválida")
      return -1

#verifica se a posição definida é valida
def posicaoValida(jogada, tabuleiro):
    if jogada<1 or jogada>9:
      print("Posição inválida")
      return False

    if tabuleiro[jogada-1] !=0:
      print("Posição ocupada")
      return False

    return True

#troca de jogador
def mudaJogador(jogador, jogada, tabuleiro):
    if jogador=="X":
      tabuleiro[jogada-1] = 1
      return "O"

    else:
      tabuleiro[jogada-1] = 2
      return "X"

#verificação das condições de fim de jogo
def verificaFimDeJogo(numJogadas, tabuleiro):
    #verifica linhas
    if tabuleiro[0]==tabuleiro[1]==tabuleiro[2]:
        if tabuleiro[0]==1:
          print("Jogador X ganhou")
          return 1
        elif tabuleiro[0]==2:
          print("Jogador O ganhou")
          return 2

    if tabuleiro[3]==tabuleiro[4]==tabuleiro[5]:
        if tabuleiro[3]==1:
          print("Jogador X ganhou")
          return 1
        elif tabuleiro[3]==2:
          print("Jogador O ganhou")
          return 2

    if tabuleiro[6]==tabuleiro[7]==tabuleiro[8]:
        if tabuleiro[6]==1:
          print("Jogador X ganhou")
          return 1
        elif tabuleiro[6]==2:
          print("Jogador O ganhou")
          return 2

    #verifica colunas
    if tabuleiro[0]==tabuleiro[3]==tabuleiro[6]:
        if tabuleiro[0]==1:
          print("Jogador X ganhou")
          return 1
        elif tabuleiro[0]==2:
          print("Jogador O ganhou")
          return 2

    if tabuleiro[1]==tabuleiro[4]==tabuleiro[7]:
        if tabuleiro[1]==1:
          print("Jogador X ganhou")
          return 1
        elif tabuleiro[1]==2:
          print("Jogador O ganhou")
          return 2

    if tabuleiro[2]==tabuleiro[5]==tabuleiro[8]:
        if tabuleiro[2]==1:
          print("Jogador X ganhou")
          return 1
        elif tabuleiro[2]==2:
          print("Jogador O ganhou")
          return 2


      #verifica diagonais
    if tabuleiro[0]==tabuleiro[4]==tabuleiro[8]:
        if tabuleiro[0]==1:
          print("Jogador X ganhou")
          return 1
        elif tabuleiro[0]==2:
          print("Jogador O ganhou")
          return 2

    if tabuleiro[2]==tabuleiro[4]==tabuleiro[6]:
        if tabuleiro[2]==1:
          print("Jogador X ganhou")
          return 1
        elif tabuleiro[2]==2:
          print("Jogador O ganhou")
          return 2

    if numJogadas>=9:
        print("Deu velha")
        return -1

    return 0

#Fluxo do jogo
print("SEJA BEM-VINDO AO JOGO DA VELHA COM PYTHON!!!")
print("---------------------------------------------\n")
tabuleiro = novoTabuleiro() #criação do tabuleiro

jogador = "X"
jogadas = 0

while True:
    exibirTabuleiro(tabuleiro)
    jogada = recebeJogada(jogador)
    if not posicaoValida(jogada, tabuleiro):
      continue
    jogador = mudaJogador(jogador, jogada, tabuleiro)
    jogadas += 1
    if(verificaFimDeJogo(jogadas, tabuleiro))!=0:
      break
