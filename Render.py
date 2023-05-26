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