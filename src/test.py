import chess
from ai import AI


board = chess.Board('r1b1kbnr/3p4/2n1q3/8/2p3p1/N7/PPPB4/R3KBNR w Qkq - 0 1')
occupied_squares = board.occupied
# Convert the bitboard to a list of squares
squares = chess.SquareSet(occupied_squares)

k = AI(4, board)
# done
# for square in squares:
#     piece = board.piece_at(square)
#     print(f'piece type{piece.piece_type} score {k.material_eval(piece)}')

# done
# 

# for square in squares:
#     piece = board.piece_at(square)
#     print(f'piece type{piece.piece_type} score {k.material_eval(piece)}')

square = chess.parse_square('a8')
piece = board.piece_at(square)
print(chess.square_rank(square))



print(f'{k.piece_eval(square,piece )}')






