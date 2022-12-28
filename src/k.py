import chess

board = chess.Board()
board_copy = chess.Board()
board_copy.set_fen(board.fen())









# if board.has_castling_rights(chess.WHITE):
#     print("White has the right to castle kingside")
# else:
#     print("White does not have the right to castle kingside")

# Check if white has the right to castle kingside
if board.castling_rights & chess.BB_H1:
  print("White has the right to castle kingside")
else:
  print("White does not have the right to castle kingside")

# Check if white has the right to castle queenside
if board.castling_rights & chess.BB_A1:
  print("White has the right to castle queenside")
else:
  print("White does not have the right to castle queenside")

# Check if black has the right to castle kingside
if board.castling_rights & chess.BB_H8:
  print("Black has the right to castle kingside")
else:
  print("Black does not have the right to castle kingside")

# Check if black has the right to castle queenside
if board.castling_rights & chess.BB_A8:
  print("Black has the right to castle queenside")
else:
  print("Black does not have the right to castle queenside")