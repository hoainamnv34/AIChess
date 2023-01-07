import chess
from ai import AI
board = chess.Board('r2k4/pp1ppp1P/8/8/8/5N2/PPPP1P2/RNBQKB1R w - - 0 1')

move = list(board.legal_moves)

print(move)


print(board.is_capture(move[7]))

board.push_uci("h7h8r")

print(board)



# if board.has_castling_rights(chess.WHITE):
#     print("White has the right to castle kingside")
# else:
#     print("White does not have the right to castle kingside")

# Check if white has the right to castle kingside
# if board.castling_rights & chess.BB_H1:
#   print("White has the right to castle kingside")
# else:
#   print("White does not have the right to castle kingside")

# # Check if white has the right to castle queenside
# if board.castling_rights & chess.BB_A1:
#   print("White has the right to castle queenside")
# else:
#   print("White does not have the right to castle queenside")

# # Check if black has the right to castle kingside
# if board.castling_rights & chess.BB_H8:
#   print("Black has the right to castle kingside")
# else:
#   print("Black does not have the right to castle kingside")

# # Check if black has the right to castle queenside
# if board.castling_rights & chess.BB_A8:
#   print("Black has the right to castle queenside")
# else:
#   print("Black does not have the right to castle queenside")


# print(board.turn)

# print(k.mobility_eval())
# print(k.piece_eval())
# # print(board.piece_at(chess.parse_square('h7')))
# print(board.legal_moves)
# board.push_san('Kf2')
# print(board)
# print(board.turn)
# print(chess.WHITE)
# print(k.eval())
# square = 1


# print(chess.square(-1, 1))
# k = chess.SQUARES[1:5]
# print(king_square)

# # for i in board.legal_moves:
# # 	print(i)
# piece = board.piece_at(0)
# print(piece.color)

# board.pieces(1, chess.WHITE)

# move = []

# for move in board.legal_moves:
#     if move.from_square == chess.E2:
#         print(move.to_square)
    
# print(board.legal_moves)
# moves = list(board.legal_moves)
# # board.push_san("e4")
# # board.push_san("e5")
# board.pseudo_legal_moves
# print(board.generate_pseudo_legal_moves())
# print(chess.SQUARE_NAMES[0] + chess.SQUARE_NAMES[30])
# # print(chess.piece_name(piece))


# print(board)
# occupied_squares = board.occupied
# print(occupied_squares)
# # Convert the bitboard to a list of squares
# squares = chess.SquareSet(occupied_squares)

# for square in squares:
#     print(board.piece_at(square))

