from random import randint

continua = 0
pontuacao1 = 0
pontuacao2 = 0
possibilidades = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
vencedor = ['Empate!', 'Jogador 2 venceu!', 'Jogador 1 venceu!', 'Jogador 1 venceu!',
'Empate!', 'Jogador 2 venceu!', 'Jogador 2 venceu!', 'Jogador 1 venceu!', 'Empate!']
jokenpo = ['Pedra', 'Papel', 'Tesoura']

def winner(p1, p2):
    for c in range(len(possibilidades)):
        if [p1, p2] == possibilidades[c]:
            print(vencedor[c])
            return vencedor[c]


modalidade = int(input('''
[ 1 ] Player X Player
[ 2 ] Player x Computador
[ 3 ] Computador x Computador
Digite a modalidade que deseja jogar: '''))
if modalidade == 1:
    while continua != 2:
        player1 = int(input('''
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Digite a Jogada do player1: '''))
        player2 = int(input('''
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Digite a Jogada do player2: '''))
        print(f'Player 1 Jogou: {jokenpo[player1 - 1]} & Player 2 Jogou: {jokenpo[player2 - 1]}!')
        pontos = winner(player1, player2)
        if pontos == 'Jogador 1 venceu!':
            pontuacao1 += 1
        elif pontos == 'Jogador 2 venceu!':
            pontuacao2 += 1
        print(f'O player 1 esta com: {pontuacao1} pontos & O Player 2 está com: {pontuacao2} pontos!')
        continua = int(input('''
[ 1 ] Sim
[ 2 ] Não
Deseja continuar: '''))
elif modalidade == 2:
    while continua != 2:
        player1 = int(input('''
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Digite a Jogada do player1: '''))
        player2 = randint(1, 3)
        print(f'Player Jogou: {jokenpo[player1 - 1]} & Computador Jogou: {jokenpo[player2 - 1]}!')
        pontos = winner(player1, player2)
        if pontos == 'Jogador 1 venceu!':
            pontuacao1 += 1
        elif pontos == 'Jogador 2 venceu!':
            pontuacao2 += 1
        print(f'O player 1 esta com: {pontuacao1} pontos & O Player 2 está com: {pontuacao2} pontos!')
        continua = int(input('''
[ 1 ] Sim
[ 2 ] Não
Deseja continuar: '''))
elif modalidade == 3:
    while continua != 2:
        player1 = randint(1, 3)
        player2 = randint(1, 3)
        print(f'Computador 1 Jogou: {jokenpo[player1 - 1]} & Computador 2 Jogou: {jokenpo[player2 - 1]}!')
        pontos = winner(player1, player2)
        if pontos == 'Jogador 1 venceu!':
            pontuacao1 += 1
        elif pontos == 'Jogador 2 venceu!':
            pontuacao2 += 1
        print(f'O player 1 esta com: {pontuacao1} pontos & O Player 2 está com: {pontuacao2} pontos!')
        continua = int(input('''
[ 1 ] Sim
[ 2 ] Não
Deseja continuar: '''))
print(f'''
==========Pontuação=Final=========
O player 1 ficou com: {pontuacao1} pontos!  |
O player 2 ficou com: {pontuacao2} pontos!  |
==================================
''')
print('''
=====Obrigado==por==Jogar=====
Trabalho realizado por:      |
Nicolas Lamback de Paulo.    |
==============================''')
