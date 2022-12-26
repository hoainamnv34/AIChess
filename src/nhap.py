import chess

board = chess.Board()

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
occupied_squares = board.occupied
print(occupied_squares)
# Convert the bitboard to a list of squares
squares = chess.SquareSet(occupied_squares)

for square in squares:
    print(board.piece_at(square))