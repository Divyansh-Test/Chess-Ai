import chess
import time
import random
board=chess.Board()
# print(board.piece_map().values())
mov="a"
def get_move(board):
    legal_moves=board.legal_moves
    legal_moves=list(legal_moves)
    dig=random.randint(0,len(legal_moves)-1)
    return str(list(legal_moves)[dig])
    

def check_victory():
    if board.is_stalemate()or board.is_insufficient_material() or board.is_checkmate():
        print("Reached Here")
        return False
    return True


weight={
     
    "P": 100,    # Pawn
    "N": 320,    # Knight
    "B": 330,    # Bishop
    "R": 500,    # Rook
    "Q": 900,    # Queen
    "K": 20000   # King
}

def evaluate_material(board):
    white_score = 0
    black_score = 0

    for piece in board.piece_map().values():
        value = weight[piece.symbol().upper()]

        if piece.color == chess.WHITE:
            white_score += value
        else:
            black_score += value

    return white_score - black_score





while mov!="q" and check_victory():
    # try:
        
        mov=get_move(board)
        
        board.push_uci(mov)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++" \
        "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\r",board)
        print(evaluate_material(board))
        time.sleep(0.05)
    # except:
        # print("Wrong Move")




