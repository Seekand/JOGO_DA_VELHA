pos_pos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']

vitoria = [['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],
           ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],
           ['a3', 'b2', 'c1'], ['a1', 'b2', 'c3']]
c = 0
xo = [' X', ' O']
jogadores = ['Jogador1', 'Jogador2']
jogada = [[], []]
jogador = [[], []]
while True:
    if c % 2 == 0:
        k = 0
    else:
        k = 1
    c += 1
    mapeamento = (f"""\033[1;30m
             JOGO - DA - VELHA

               {pos_pos[0]} | {pos_pos[1]} | {pos_pos[2]}
               --------------
               {pos_pos[3]} | {pos_pos[4]} | {pos_pos[5]}
               --------------
               {pos_pos[6]} | {pos_pos[7]} | {pos_pos[8]}""")
    print(mapeamento)
    while True:
        vit = [0, 0]
        pos_vit = pos = jog = 0
        jogada[k] = str(input(f'\n\033[1;30m{jogadores[k]}, Escolha uma posicão: '))
        if jogada[k] in pos_pos:
            jogador[k].append(jogada[k])
            pos_pos[pos_pos.index(jogada[k])] = xo[k]
            break
    while True:
        if jogador[k][jog] == vitoria[pos_vit][pos]:
            vit[k] += 1
        if vit[k] == 3 or pos_vit == (len(vitoria)-1):
            break
        if pos == 2 and jog == len(jogador[k])-1:
            pos_vit += 1
            pos = 0
            jog = 0
            vit[k] = 0
        elif pos == 2 and jog != len(jogador[k])-1:
            jog += 1
            pos = 0
        elif pos < 2:
            pos += 1
    bola = ''.join(pos_pos).count('O')
    xix = ''.join(pos_pos).count('X')
    if vit[k] == 3 or bola + xix == 9:
        break
print(mapeamento.replace(jogada[k], xo[k]))
if vit[0] == 3:
    print('\nJogador 1 Venceu !!!')
elif vit[1] == 3:
    print('\nJogador 2 Venceu !!!')
else:
    print('\nDeu Velha...')
