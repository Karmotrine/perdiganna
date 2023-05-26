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