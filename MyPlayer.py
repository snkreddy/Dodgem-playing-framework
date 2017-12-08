'''
    File name: MyPlayer.py
    Author: Siddhant Kumar
    Email: saytosid@gmail.com
    Date created: 1 Oct 2017
    Date last modified: 1 Oct 2017
    Python Version: 3.0
'''
from framework import Player
import copy
import time
class MyPlayer(Player):


    def __init__(self):
        pass


    def get_move(self,board):
        '''
        :param board: Board object
        :return: (piece,new_position,BoardLeavingMove)
        '''
        if board.turn==2:
            moves = board.get_valid_moves()
            cou=0
            # for it in moves:
            #     print(it,cou)
            #     cou+=1
            board_matrix,turn = board.get_board_config()
            x1=0
            if len(moves)>2:
                x1=3
            else:
                x1=1
            board_copy=copy.deepcopy(board) #deepcopy of object done
            cov=0

            max=0
            j=0
            clones=[0 for mov in board.get_valid_moves()]
            i=0
            t1=time.time()
            moves_exact = board.get_valid_moves()
            for mov in board.get_valid_moves():
                clones[i]=copy.deepcopy(board)
                board_parent=copy.deepcopy(board)
                moves=clones[i].get_valid_moves()

                # print(moves)
                # moves.sort(key=second,reverse=True)
                clones[i].make_move(moves[i])
                # print(board_matrix)
                mat,turn=clones[i].get_board_config()
                # print(mat)

                mov_exact=moves_exact[i]
                k=MINIMAX(2,clones[i],1,board_parent,mov_exact,x1)
                # print("the value of K =",k)
                if(max<=k):#big problem
                    max=k
                    j=i
                i=i+1

            moves = board.get_valid_moves()
            # print( time.time()-t1)
            return moves[j]






        if board.turn==1:
            moves = board.get_valid_moves()
            cou=0
            # for it in moves:
            #     print(it,cou)
            #     cou+=1
            board_matrix,turn = board.get_board_config()
            x1=0
            if len(moves)>2:
                x1=3
            else:
                x1=1
            board_copy=copy.deepcopy(board) #deepcopy of object done
            cov=0

            max=0
            j=0
            clones=[0 for mov in board.get_valid_moves()]
            i=0
            moves_exact = board.get_valid_moves()
            t1=time.time()
            for mov in board.get_valid_moves():
                clones[i]=copy.deepcopy(board)
                board_parent=copy.deepcopy(board)
                moves=clones[i].get_valid_moves()

                # print(moves)
                # moves.sort(key=second3,reverse=True)
                clones[i].make_move(moves[i])
                # print(board_matrix)
                mat,turn=clones[i].get_board_config()
                # print(mat)

                mov_exact=moves_exact[i]
                # print(x1)
                # x1=3
                k=MINIMAX1(2,clones[i],1,board_parent,mov_exact,x1)
                # print("the value of K =",k)
                if(max<k):#big problem
                    max=k
                    j=i
                i=i+1

            moves = board.get_valid_moves()
            # print( time.time()-t1)
            return moves[j]


#
# def second3(ele):
#     return ele[1][0]+ele[1][1]

def second(elem):
    return elem[1][0]

def second1(elem):
    return elem[1][1]


def h(board_matrix,board_parent,mov_exact):

    i1=mov_exact[0].pos[0]
    j1=mov_exact[0].pos[1]

    # print(i1,j1)
    i2=mov_exact[1][0]
    j2=mov_exact[1][1]

    h=0
    if i2<i1:
        h=3000
    elif j2<j1:
        h=2000
    elif j2>j1:
        h=1000



    i=0
    for m in board_matrix:
        j=0
        for p in m:
            if p==2:
                h=h+(i)*100

        i=i+1

    o=0
    for m in board_matrix:

        for p in m:
            if p==2:
                o=o+1


    o=len(board_matrix)-1-o
    o=o*5000

    return h+o

def h1(board_matrix,board_parent,mov_exact):

    i1=mov_exact[0].pos[0]
    j1=mov_exact[0].pos[1]
    # print(i1,j1)
    i2=mov_exact[1][0]
    j2=mov_exact[1][1]

    h=0
    if j2>j1:
        h=3000

    elif i2>i1:
        h=2000

    elif i2<i1:
        h=1000

    i=0


    for m in board_matrix:
        j=0
        for p in m:

            if p==1:
                h=h+(j)*100
            j=j+1


    o=0
    for m in board_matrix:

        for p in m:
            if p==1:
                o=o+1

    o=len(board_matrix)-1-o
    o=o*5000


    return h+o







def MINIMAX(type,board,depth,board_parent,mov_exact,x):

    if depth==1:
        board_matrix,turn = board.get_board_config()
        return h(board_matrix,board_parent,mov_exact)

    if(type==1):
        max=0
        clones=[0 for mov in board.get_valid_moves()]
        i=0
        moves_exact = board.get_valid_moves()
        for mov in board.get_valid_moves():
            clones[i]=copy.deepcopy(board)
            board_parent=copy.deepcopy(board)
            moves=clones[i].get_valid_moves()
            # moves.sort(key=second,reverse=True)
            clones[i].make_move(moves[i])
            mov_exact=moves_exact[i]
            k=MINIMAX(2,clones[i],depth+1,board_parent,mov_exact,x)
            if(max<=k):
                max=k
            i=i+1
        return max

    if(type==2):
        min=0
        clones=[0 for mov in board.get_valid_moves()]
        i=0
        moves_exact = board.get_valid_moves()
        for mov in board.get_valid_moves():
            clones[i]=copy.deepcopy(board)
            board_parent=copy.deepcopy(board)
            moves=clones[i].get_valid_moves()
            # moves.sort(key=second,reverse=True)
            clones[i].make_move(moves[i])
            mov_exact=moves_exact[i]
            k=MINIMAX(1,clones[i],depth+1,board_parent,mov_exact,x)
            if(min<=k):
                min=k
            i=i+1
        return min


def MINIMAX1(type,board,depth,board_parent,mov_exact,x):

    if depth==x:
        board_matrix,turn = board.get_board_config()
        # print(mov_exact)
        return h1(board_matrix,board_parent,mov_exact)

    if(type==1):
        max=0
        clones=[0 for mov in board.get_valid_moves()]
        i=0
        moves_exact = board.get_valid_moves()
        for mov in board.get_valid_moves():
            clones[i]=copy.deepcopy(board)
            board_parent=copy.deepcopy(board)
            moves=clones[i].get_valid_moves()
            # moves.sort(key=second,reverse=True)
            clones[i].make_move(moves[i])
            mov_exact=moves_exact[i]
            k=MINIMAX1(2,clones[i],depth+1,board_parent,mov_exact,x)
            # print(k)
            if(max<=k):
                max=k
            i=i+1
        return max

    if(type==2):
        min=0
        clones=[0 for mov in board.get_valid_moves()]
        i=0
        moves_exact = board.get_valid_moves()
        for mov in board.get_valid_moves():
            clones[i]=copy.deepcopy(board)
            board_parent=copy.deepcopy(board)
            moves=clones[i].get_valid_moves()
            # moves.sort(key=second,reverse=True)
            clones[i].make_move(moves[i])
            mov_exact=moves_exact[i]
            k=MINIMAX1(1,clones[i],depth+1,board_parent,mov_exact,x)
            if(min<=k):
                min=k
            i=i+1
        return min
