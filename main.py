from cmath import inf
import pygame, sys
from pygame.locals import *
import time
from copy import deepcopy
import random
import time

#each square is a list of features
# board = [x,y,row,column,free,color,king]
# row=0 -> even, color=0 -> white, color=1 -> black, king=1 -> True
# x-axis: +150, y-axis: +75
# y-axis: inverse (always positive)

# Yellow = Move hint
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


def update_graphics(diz,el,origin,graphic,board):
    key=''
    for i in diz.keys():
        if diz[i]['jump'][-1]==el and diz[i]['origin']==origin:
                key=i
                if key==99:
                    key=el
    if graphic==True:
        screen.blit(fill_image, (board[origin][0]-2,board[origin][1]-2))
        pygame.display.update()
    board[origin][4] = 0
    board[el][4] = 2
    board[el][5] = board[origin][5]
    board[el][6] = board[origin][6]
    if diz[key]['n_jumps']==0 :
        image(board,el,origin,graphic)
        board[origin][6]=0
        if graphic==True:
            move_sound.play() 
    else:
        for i in range(0,len(diz[key]['jump'])):
            board[diz[key]['jump'][i]][4] = 2
            board[diz[key]['jump'][i]][5] = board[origin][5]
            board[diz[key]['jump'][i]][6] = board[origin][6]
            board[diz[key]['eaten'][i]][4] = 0
            if graphic==True:
                screen.blit(fill_image, (board[diz[key]['eaten'][i]][0]-2,board[diz[key]['eaten'][i]][1]-2))
                if i>0:
                    screen.blit(fill_image, (board[diz[key]['jump'][i-1]][0]-2,board[diz[key]['jump'][i-1]][1]-2))
                pygame.display.update()
            if i>0:
                image(board,diz[key]['jump'][i],diz[key]['jump'][i-1],graphic)
                board[diz[key]['jump'][i-1]][4] = 0
            else:
                image(board,diz[key]['jump'][i],origin,graphic)  
            if graphic==True:
                capture_sound.play()
                time.sleep(0.3)              
    return board


def image(board,el,origin,graphic):
    if (board[el][1]<50 or board[origin][6]==1) and board[origin][5]==0:
        board[origin][6]=0
        board[el][6]=1
        if graphic==True:
            print_image(board[el][0],board[el][1],0,1,0,0)
    elif board[origin][5]==0:
        board[origin][6]=0
        board[el][6]=0
        if graphic==True:
            print_image(board[el][0],board[el][1],0,0,0,0)
    elif (board[el][1]>500 or board[origin][6]==1) and board[origin][5]==1:
        board[origin][6]=0
        board[el][6]=1
        if graphic==True:
            print_image(board[el][0],board[el][1],1,1,0,0)
    elif board[origin][5]==1:
        board[origin][6]=0
        board[el][6]=0
        if graphic==True:
            print_image(board[el][0],board[el][1],1,0,0,0)


def equal(color):
    for n in range(1,33):
        if board[n][5]==color and board[n][4]==2:
            diz=check_moves(n,False,board,False,{})
            if len(diz.keys())>0:
                return False
    return True


def print_image(x,y,color,king,yellow,selected):
    if yellow==1:
        screen.blit(pygame.image.load("./Images/move.png"), (x,y))
    elif color==0 and selected==0 and king==0:
        screen.blit(pygame.image.load("./Images/white.png"), (x,y))
    elif color==0 and selected==1 and king==0:
        screen.blit(pygame.image.load("./Images/white2.png"), (x,y))
    elif color==0 and selected==0 and king==1:
        screen.blit(pygame.image.load("./Images/white_king.png"), (x,y))
    elif color==0 and selected==1 and king==1:
        screen.blit(pygame.image.load("./Images/white_king2.png"), (x,y))
    elif color==1 and selected==0 and king==0:
        screen.blit(pygame.image.load("./Images/black.png"), (x,y))
    elif color==1 and selected==1 and king==0:
        screen.blit(pygame.image.load("./Images/black2.png"), (x,y))
    elif color==1 and selected==0 and king==1:
        screen.blit(pygame.image.load("./Images/black_king.png"), (x,y))
    elif color==1 and selected==1 and king==1:
        screen.blit(pygame.image.load("./Images/black_king2.png"), (x,y))
    pygame.display.update()


# 0 = Black?
# 1 = White?
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
            if board[i][5]==1: # Black
                if board[i][6]==1:
                    score-=1.5 #negated
                else:
                    score-=1 #negated
            elif board[i][5]==0: # White
                if board[i][6]==1:
                    score+=1.5 #negated
                else:
                    score+=1 #negated
    return score


def all_moves(color,board):
    list=[]
    for n in range(1,33):
        if board[n][5]==color and board[n][4]==2:
            diz2=check_moves(n,False,board,False,{})
            for l in diz2:
                diz_temp={l:diz2[l]}
                list.append(diz_temp)
    max_value=float('-inf')
    for el in list:
        for val in el.keys():
            if el[val]['n_jumps']>max_value:
                max_value=el[val]['n_jumps']
    list_final=[]
    for el in list:
        for val in el.keys():
            if el[val]['n_jumps']==max_value:
                list_final.append(el)
    return list_final


def minimax_fun(max_player,depth,board,black_move, start_time, max_time, move=[],alpha=float('-inf'),beta=float('inf')):
    print(f"depth: {depth}, alpha: {alpha}, beta: {beta}, max_player: {max_player}")

    if depth==0 or game_finished(board,0) or game_finished(board,1):
        val=evaluate(board,move)
        return val
    #if time.time() - start_time >= max_time:
    #    val=evaluate(board,move)
    #    return val
    
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
            minimax = minimax_fun(False,depth-1,board_copy,False, start_time, max_time, i)
            if minimax>max_best:
                coll={}
                max_best=minimax
                coll[dest]=[max_best,i,origin]
            elif minimax==max_best and max_best>float('-inf'):
                max_best=minimax
                coll[dest]=[max_best,i,origin]
            if time.time() - start_time >= max_time:
                dest, minimax  = random.choice(list(coll.items()))
                return minimax[0],minimax[2],dest,minimax[1]
        dest, minimax  = random.choice(list(coll.items()))
        # Iterative Deepening
        #if time.time() - start_time >= max_time:
        #    return minimax[0],minimax[2],dest,minimax[1]
        # Final return
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
            minimax = minimax_fun(False,depth-1,board_copy,False, start_time, max_time, i,alpha,beta)
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
            minimax = minimax_fun(True,depth-1,board_copy,False, start_time, max_time, i,alpha,beta)
            # Alpha Beta Pruning
            best = min(best, minimax)
            beta = min(beta, best)
            if beta <= alpha:
                break  
        return best

pygame.init()
screen = pygame.display.set_mode((637,787))
icon = pygame.image.load("./Images/white.png")
pygame.display.set_icon(icon)
screen.fill([252, 223, 180])
pygame.display.set_caption('Perdigana')
pygame.font.init()
font = pygame.font.SysFont('CenturyGothic', 30)
move_sound = pygame.mixer.Sound('./Sounds/chess.wav')
capture_sound = pygame.mixer.Sound('./Sounds/capture.wav')
tie_sound = pygame.mixer.Sound('./Sounds/tie.wav')
winner_sound = pygame.mixer.Sound('./Sounds/winner.wav')
screen.blit(pygame.image.load('./Images/board.png'), (0, 0))

board={}
y = 23
i=1
for row in range(8):
    x=24 # X-axis Pixel offset
    if row%2 != 0:
        while(x<600):
            board[i]=[x,y,0,1,0,0,0]
            x+=150
            i+=1
    else:
        x+=75
        while(x<600):
            board[i]=[x,y,1,0,0,0,0]
            x+=150
            i+=1
    y+=75

for i in board.keys():
    # White Pieces
    if i>20:
        board[i][4]=2
        board[i][5]=0
        print_image(board[i][0],board[i][1],board[i][5],board[i][6],0,0)
    # Black Pieces
    elif i<=12:
        board[i][4]=2
        board[i][5]=1
        print_image(board[i][0],board[i][1],board[i][5],board[i][6],0,0)
    # key[n] = blank space, where   12 <= n > 20

turn=1
fill_image = pygame.image.load("./Images/fill.png")
cup_image = pygame.image.load("./Images/cup.png")
origin=0
n_moves=0
prev_score=99
selected=False
text = font.render('WHITE TO MOVE', True, (0, 0, 0))
text_rect = text.get_rect(center=(637/2, 660))
screen.blit(text, text_rect)
pygame.draw.rect(screen, (0,0,0), (20,730,595,30))
pygame.draw.rect(screen, (255,255,255), (637/2,730,298,30))
pygame.draw.rect(screen, (255,0,0), (637/2-2,730,4,30))
font2 = pygame.font.SysFont('CenturyGothic', 20)
text = font2.render('-18', True, (0, 0, 0))
text_rect = text.get_rect(center=(20, 710))
screen.blit(text, text_rect)
text = font2.render('+18', True, (0, 0, 0))
text_rect = text.get_rect(center=(607, 710))
screen.blit(text, text_rect)
text = font2.render('0', True, (0, 0, 0))
text_rect = text.get_rect(center=(637/2, 710))
screen.blit(text, text_rect)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            print(pos)
            if turn==1:
                if selected==False:
                    for el in range(1,33):
                        if board[el][0]+10 < pos[0] < board[el][0]+57 and board[el][1]+10 < pos[1] < board[el][1]+57 and board[el][5]==0 and board[el][4]!=0:
                            possible_moves = check_moves(el,True,board,False,{})
                            origin=el
                            if len(possible_moves.keys())>0:
                                selected=True
                                el_copy=el
                                print_image(board[el][0],board[el][1],0,board[el][6],0,1)
                                screen.fill([252, 223, 180],rect=(0,638,637,50))
                                text = font.render('SELECT A SQUARE', True, (0, 0, 0))
                                text_rect = text.get_rect(center=(637/2, 660))
                                screen.blit(text, text_rect)
                                pygame.display.update()
                            else:
                                screen.fill([252, 223, 180],rect=(0,638,637,50))
                                text = font.render('NO POSSIBLE MOVES, RETRY', True, (0, 0, 0))
                                text_rect = text.get_rect(center=(637/2, 660))
                                screen.blit(text, text_rect)
                                pygame.display.update()
                else:
                    for el in range(1,33):
                        if board[el][0]+10 < pos[0] < board[el][0]+57 and board[el][1]+10 < pos[1] < board[el][1]+57:
                            if board[el][5]==0 and board[el][4]==2:
                                if el==el_copy:
                                    print_image(board[el_copy][0],board[el_copy][1],0,board[el_copy][6],0,0)
                                    selected=False
                                    for value in possible_moves.keys():
                                        if value!=99:
                                            screen.blit(fill_image, (board[value][0]-2,board[value][1]-2))
                                    pygame.display.update()
                                else:
                                    print_image(board[el_copy][0],board[el_copy][1],0,board[el_copy][6],0,0)
                                    el_copy=el
                                    print_image(board[el][0],board[el][1],0,board[el][6],0,1)
                                    for value in possible_moves.keys():
                                        screen.blit(fill_image, (board[value][0]-2,board[value][1]-2))
                                    for el in range(1,33):
                                        if board[el][0]+10 < pos[0] < board[el][0]+57 and board[el][1]+10 < pos[1] < board[el][1]+57 and board[el][5]==0 and board[el][4]!=0:
                                            possible_moves = check_moves(el,True,board,False,{})
                                            origin=el
                                            if len(possible_moves.keys())>0:
                                                selected=True
                                                print_image(board[el][0],board[el][1],0,board[el][6],0,1)
                                                screen.fill([252, 223, 180],rect=(0,638,637,50))
                                                text = font.render('SELECT A SQUARE', True, (0, 0, 0))
                                                text_rect = text.get_rect(center=(637/2, 660))
                                                screen.blit(text, text_rect)
                                                pygame.display.update()
                                            else:
                                                screen.fill([252, 223, 180],rect=(0,638,637,50))
                                                text = font.render('NO POSSIBLE MOVES, RETRY', True, (0, 0, 0))
                                                text_rect = text.get_rect(center=(637/2, 660))
                                                screen.blit(text, text_rect)
                                                pygame.display.update()
                            # White Legal Moves
                            elif el in [*possible_moves]:
                                max_value=float('-inf')
                                for cell in range(1,33):
                                    if board[cell][4]==2 and board[cell][5]==0:
                                        tmp_possible_moves = check_moves(cell,False,board,False,{})
                                        if len(tmp_possible_moves.keys())>0:
                                            for i in tmp_possible_moves:
                                                if tmp_possible_moves[i]['n_jumps']>max_value:
                                                    max_value=tmp_possible_moves[i]['n_jumps']
                                if possible_moves[el]['n_jumps']<max_value:
                                    screen.fill([252, 223, 180],rect=(0,638,637,50))
                                    text = font.render('SELECT A LEGAL MOVE', True, (0, 0, 0))
                                    text_rect = text.get_rect(center=(637/2, 660))
                                    screen.blit(text, text_rect)
                                    pygame.display.update()
                                else:
                                    for value in possible_moves.keys():
                                        if value!=99:
                                            screen.blit(fill_image, (board[value][0]-2,board[value][1]-2))
                                    pygame.display.update()
                                    update_graphics(possible_moves,el,origin,True,board)
                                    selected=False

                                    if evaluate(board,move={},draw=True)!= prev_score:
                                        prev_score=evaluate(board,move={},draw=True)
                                        n_moves=0
                                    else:
                                        n_moves+=1
                                    if n_moves==50:
                                        screen.fill([252, 223, 180],rect=(0,638,637,50))
                                        text = font.render('TIE GAME!', True, (0, 0, 0))
                                        text_rect = text.get_rect(center=(637/2, 660))
                                        screen.blit(text, text_rect)
                                        tie_sound.play()
                                        pygame.display.update()
                                        time.sleep(3)
                                        pygame.quit()
                                        sys.exit()  

                                    # modified for perdigana
                                    if game_finished(board,1)==True or equal(1)==True:
                                        screen.fill([252, 223, 180],rect=(0,638,637,50))
                                        text = font.render('BLACK WINS!', True, (0, 0, 0))
                                        text_rect = text.get_rect(center=(637/2, 660))
                                        screen.blit(text, text_rect)
                                        winner_sound.play()
                                        screen.blit(cup_image,(218,70))
                                        pygame.display.update()
                                        turn=999
                                    else:
                                        screen.fill([252, 223, 180],rect=(0,638,637,50))
                                        text = font.render('BLACK TO MOVE', True, (0, 0, 0))
                                        text_rect = text.get_rect(center=(637/2, 660))
                                        screen.blit(text, text_rect)
                                        pygame.display.update()
                                        board_copy=deepcopy(board)
                                        # Iterative Deepening
                                        max_time = 5
                                        start_time = time.time()
                                        best_move = None
                                        current_depth = 1
                                        while True:
                                            val,origin,el,lis = minimax_fun(True,current_depth,board_copy, True, start_time, max_time)
                                            current_depth += 1
                                            if time.time() - start_time >= max_time:
                                                break
                                        pygame.draw.rect(screen, (0,0,0), (20,730,595,30))
                                        pygame.draw.rect(screen, (255,255,255), (637/2+(val*596)/36,730,298-(val*596)/36,30))
                                        pygame.draw.rect(screen, (255,0,0), (637/2-2,730,4,30))
                                        pygame.display.update()
                                        update_graphics(lis,el,origin,True,board)

                                        if evaluate(board,move={},draw=True)!= prev_score:
                                            prev_score=evaluate(board,move={},draw=True)    

                                        # modified to perdigana
                                        if game_finished(board,0)==True or equal(0)==True:
                                            screen.fill([252, 223, 180],rect=(0,638,637,50))
                                            text = font.render('WHITE WINS!', True, (0, 0, 0))
                                            text_rect = text.get_rect(center=(637/2, 660))
                                            screen.blit(text, text_rect)
                                            screen.blit(cup_image,(218,400))
                                            winner_sound.play()
                                            pygame.display.update()
                                            turn=3
                                        else:
                                            screen.fill([252, 223, 180],rect=(0,638,637,50))
                                            text = font.render('WHITE TO MOVE', True, (0, 0, 0))
                                            text_rect = text.get_rect(center=(637/2, 660))
                                            screen.blit(text, text_rect)
                                            pygame.display.update()
