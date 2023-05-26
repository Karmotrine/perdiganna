

def check_moves(el,yellow,board,only_jumps,diz):
    #check for move 1 -> upper left
    if board[el][0]-75>0 and board[el][1]-75>0 and (board[el][6]==1 or board[el][5]==0): #valid move
        if board[el-4-board[el][3]][4]==2: #cell not empty
            if board[el-4-board[el][3]][5]!=board[el][5]: #different color
                if board[el][0]-150>0 and board[el][1]-150>0: #jump cell exists
                    if board[el-9][4]!=2 and board[el][6]>=board[el-4-board[el][3]][6]: #valid jump
                        if el not in diz.keys():
                            diz[el-9] = {'n_jumps':1, 'jump':[el-9], 'eaten':[el-4-board[el][3]], 'origin':el}
                        else:
                            diz[el-9]=deepcopy(diz[el])
                            diz[el-9]['n_jumps']+=1
                            diz[el-9]['eaten'].append(el-4-board[el][3])
                            diz[el-9]['jump'].append(el-9)
                            diz[99] = {'n_jumps':1, 'jump':[el-9], 'eaten':[el-4-board[el][3]], 'origin':el}
                        if yellow==True:
                            print_image(board[el-9][0],board[el-9][1],0,0,1,0)
                        board_copy=deepcopy(board)
                        board_copy=update_graphics(diz,el-9,el,False,board_copy)   
                        diz = check_moves(el-9,yellow,board_copy,True,diz)
        elif only_jumps==False:
            diz[el-4-board[el][3]] = {'n_jumps':0, 'jump':[el-4-board[el][3]], 'eaten':[], 'origin':el}
            if yellow==True:
                print_image(board[el-4-board[el][3]][0],board[el-4-board[el][3]][1],0,0,1,0)
    #check for move 2 -> upper right
    if board[el][0]+75<550 and board[el][1]-75>0 and (board[el][6]==1 or board[el][5]==0):
        if board[el-3-board[el][3]][4]==2:
            if board[el-3-board[el][3]][5]!=board[el][5]:
                if board[el][0]+150<550 and board[el][1]-150>0:
                    if board[el-7][4]!=2 and board[el][6]>=board[el-3-board[el][3]][6]:
                        if el not in diz.keys():
                            diz[el-7] = {'n_jumps':1, 'jump':[el-7], 'eaten':[el-3-board[el][3]], 'origin':el}
                        else:
                            diz[el-7]=deepcopy(diz[el])
                            diz[el-7]['n_jumps']+=1
                            diz[el-7]['eaten'].append(el-3-board[el][3])
                            diz[el-7]['jump'].append(el-7)
                            diz[99] = {'n_jumps':1, 'jump':[el-7], 'eaten':[el-3-board[el][3]], 'origin':el}
                        if yellow==True:
                            print_image(board[el-7][0],board[el-7][1],0,0,1,0)
                        board_copy=deepcopy(board)
                        board_copy=update_graphics(diz,el-7,el,False,board_copy)   
                        diz = check_moves(el-7,yellow,board_copy,True,diz)
        elif only_jumps==False:
            diz[el-3-board[el][3]] = {'n_jumps':0, 'jump':[el-3-board[el][3]], 'eaten':[], 'origin':el}
            if yellow==True:
                print_image(board[el-3-board[el][3]][0],board[el-3-board[el][3]][1],0,0,1,0)
    #check for move 3 -> lower left
    if board[el][0]-75>0 and board[el][1]+75<550 and (board[el][6]==1 or board[el][5]==1):
        if board[el+3+(board[el][3]+1)%2][4]==2:
            if board[el+3+(board[el][3]+1)%2][5]!=board[el][5]:
                if board[el][0]-150>0 and board[el][1]+150<550:
                    if board[el+7][4]!=2 and board[el][6]>=board[el+3+(board[el][3]+1)%2][6]:
                        if el not in diz.keys():
                            diz[el+7] = {'n_jumps':1, 'jump':[el+7], 'eaten':[el+3+(board[el][3]+1)%2], 'origin':el}
                        else:
                            diz[el+7]=deepcopy(diz[el])
                            diz[el+7]['n_jumps']+=1
                            diz[el+7]['eaten'].append(el+3+(board[el][3]+1)%2)
                            diz[el+7]['jump'].append(el+7)
                            diz[99] = {'n_jumps':1, 'jump':[el+7], 'eaten':[el+3+(board[el][3]+1)%2], 'origin':el}
                        if yellow==True:
                            print_image(board[el+7][0],board[el+7][1],0,0,1,0)
                        board_copy=deepcopy(board)
                        board_copy=update_graphics(diz,el+7,el,False,board_copy)   
                        diz = check_moves(el+7,yellow,board_copy,True,diz)
        elif only_jumps==False:
            diz[el+3+(board[el][3]+1)%2] = {'n_jumps':0, 'jump':[el+3+(board[el][3]+1)%2], 'eaten':[], 'origin':el}
            if yellow==True:
                print_image(board[el+3+(board[el][3]+1)%2][0],board[el+3+(board[el][3]+1)%2][1],0,0,1,0)
    #check for move 4 -> lower right
    if board[el][0]+75<550 and board[el][1]+75<550 and (board[el][6]==1 or board[el][5]==1):
        if board[el+5-board[el][3]%2][4]==2:
            if board[el+5-board[el][3]%2][5]!=board[el][5]:
                if board[el][0]+150<550 and board[el][1]+150<550:
                    if board[el+9][4]!=2 and board[el][6]>=board[el+5-board[el][3]%2][6]:
                        if el not in diz.keys():
                            diz[el+9]={'n_jumps':1, 'jump':[el+9], 'eaten':[el+5-board[el][3]%2], 'origin':el}
                        else:
                            diz[el+9]=deepcopy(diz[el])
                            diz[el+9]['n_jumps']+=1
                            diz[el+9]['eaten'].append(el+5-board[el][3]%2)
                            diz[el+9]['jump'].append(el+9)
                            diz[99] = {'n_jumps':1, 'jump':[el+9], 'eaten':[el+5-board[el][3]%2], 'origin':el}
                        if yellow==True:
                            print_image(board[el+9][0],board[el+9][1],0,0,1,0)
                        board_copy=deepcopy(board)
                        board_copy=update_graphics(diz,el+9,el,False,board_copy)   
                        diz = check_moves(el+9,yellow,board_copy,True,diz)
        elif only_jumps==False:
            diz[el+5-board[el][3]%2]={'n_jumps':0, 'jump':[el+5-board[el][3]%2], 'eaten':[], 'origin':el}
            if yellow==True:
                print_image(board[el+5-board[el][3]%2][0],board[el+5-board[el][3]%2][1],0,0,1,0)
    return diz

def game_finished(table,color):
    for el in range(1,33):
        if table[el][4]==2 and table[el][5]==color:
            return False
    return True

def evaluate(board,move={},draw=False):
    if not draw:
        for destination in move.keys():
            dest=destination
            origin=move[dest]['origin']
            diz={dest:move[dest]}
        board=update_graphics(diz,dest,origin,False,board)
    score=0
    for i in range(1,33):
        if board[i][4]==2:
            if board[i][5]==1:
                if board[i][6]==1:
                    score+=1.5
                else:
                    score+=1
            elif board[i][5]==0:
                if board[i][6]==1:
                    score-=1.5
                else:
                    score-=1
    return score
