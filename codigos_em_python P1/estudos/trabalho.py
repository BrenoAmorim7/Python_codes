



def checar_game_over(vida_zero, tem_item_ressurreicao, tempo_esgotado):

    # Simplificado: é Game Over se o tempo acabar OU se a vida zerar e o jogador não tiver o item     
    return tempo_esgotado or (vida_zero and not tem_item_ressurreicao)







    