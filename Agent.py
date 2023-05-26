def minimax_fun(max_player,depth,board,black_move,move=[],alpha=float('-inf'),beta=float('inf')):
    print(f"depth: {depth}, alpha: {alpha}, beta: {beta}, max_player: {max_player}")
    if depth==0 or game_finished(board,0) or game_finished(board,1):
        val=evaluate(board,move)
        return val
    elif black_move==True:
        max_best=float('-inf')
        for i in all_moves(1,board):
            for destination in i.keys():
                dest=destination
                origin=i[dest]['origin']
                key = str(dest) + '_' + str(origin)
                diz_copy={key:i[dest]}
            board_copy=deepcopy(board)
            board_copy=update_graphics(diz_copy,dest,origin,False,board_copy)
            minimax = minimax_fun(False,depth-1,board_copy,False,i)
            if minimax>max_best:
                coll={}
                max_best=minimax
                coll[dest]=[max_best,i,origin]
            elif minimax==max_best and max_best>float('-inf'):
                max_best=minimax
                coll[dest]=[max_best,i,origin]
        dest, minimax  = random.choice(list(coll.items()))
        return minimax[0],minimax[2],dest,minimax[1]
    elif max_player==True:
        best=float('-inf')
        for i in all_moves(1,board):
            for destination in i.keys():
                dest=destination
                origin=i[dest]['origin']
                key = str(dest) + '_' + str(origin)
                diz_copy={key:i[dest]}
            board_copy=deepcopy(board)
            board_copy=update_graphics(diz_copy,dest,origin,False,board_copy)
            minimax = minimax_fun(False,depth-1,board_copy,False,i,alpha,beta)
            # Alpha Beta Pruning
            best = max(best, minimax)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    elif max_player==False:
        best=float('inf')
        for i in all_moves(0,board):
            for destination in i.keys():
                dest=destination
                origin=i[dest]['origin']
                key = str(dest) + '_' + str(origin)
                diz_copy={key:i[dest]}
            board_copy=deepcopy(board)
            board_copy=update_graphics(diz_copy,dest,origin,False,board_copy)
            minimax = minimax_fun(True,depth-1,board_copy,False,i,alpha,beta)
            # Alpha Beta Pruning
            best = min(best, minimax)
            beta = min(beta, best)
            if beta <= alpha:
                break  
        return best