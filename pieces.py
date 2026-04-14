from typing import TYPE_CHECKING, List, Tuple, Optional
from constants import ValidMoves, Position, Color

if TYPE_CHECKING:
    from board import Board

class Piece():
    def __init__(self, color: Color, position: Position) -> None:
        self.color = color
        self.position = position

class SlidingPiece(Piece):
    def _get_sliding_moves(self, board: Board, movement: ValidMoves) -> ValidMoves:
        valid_moves = []

        col, row = self.position
        for col_move, row_move in movement:
            for i in range(1, 9):
                new_col = col + col_move * i
                new_row = row + row_move * i

                if board.is_within_bounds(new_col, new_row):
                    target_piece = board.get_piece(new_col, new_row)

                    if target_piece is None:
                        valid_moves.append((new_col, new_row))                                                  #basic move
                    
                    else:
                        if target_piece.color != self.color:
                            valid_moves.append((new_col, new_row))                                              #capture

                        break

                else:
                    break

        return valid_moves

class Queen(SlidingPiece):
    def get_valid_moves(self, board: Board) -> ValidMoves:
        movement = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        return self._get_sliding_moves(board, movement)
    
class Bishop(SlidingPiece):
    def get_valid_moves(self, board: Board) -> ValidMoves:
        movement = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
        return self._get_sliding_moves(board, movement)

class Rook(SlidingPiece):
    def get_valid_moves(self, board: Board) -> ValidMoves:
        movement = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        return self._get_sliding_moves(board, movement)

class Knight(Piece):
    def get_valid_moves(self, board: Board) -> ValidMoves:
        movement = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        valid_moves = []
        
        col, row = self.position
        for col_jump, row_jump in movement:
            new_col = col + col_jump
            new_row = row + row_jump

            if board.is_within_bounds(new_col, new_row):
                target_piece = board.get_piece(new_col, new_row)

                if target_piece is None or target_piece.color != self.color:
                    valid_moves.append((new_col, new_row))                                                      #basic move/capture

        return valid_moves

class Pawn(Piece):
    def get_valid_moves(self, board: Board) -> ValidMoves:
        valid_moves = []
        movement_white = [(0, -1), (-1, -1), (1, -1), (0, -2)]
        movement_black = [(0, 1), (-1, 1), (1, 1), (0, 2)]
        col, row = self.position
        
        color = self.color
        if color == Color.WHITE:
            for col_move, row_move in movement_white:
                new_col = col + col_move
                new_row = row + row_move

                if board.is_within_bounds(new_col, new_row):
                    target_piece = board.get_piece(new_col, new_row)

                    if col_move == 0 and row_move == -2 and row == 6 and target_piece is None:
                        jump_piece = board.get_piece(new_col, new_row + 1)
                        
                        if jump_piece is None:
                            valid_moves.append((new_col, new_row))                                              #first move 2 steps

                    if col_move == 0 and row_move == -1 and target_piece is None:
                        valid_moves.append((new_col, new_row))                                                  #basic move

                    if abs(col_move) == 1 and row_move == -1 and target_piece is not None and target_piece.color != self.color:
                        valid_moves.append((new_col, new_row))                                                  #capture

        else:
            for col_move, row_move in movement_black:
                new_col = col + col_move
                new_row = row + row_move

                if board.is_within_bounds(new_col, new_row):
                    target_piece = board.get_piece(new_col, new_row)

                    if col_move == 0 and row_move == 2 and row == 1 and target_piece is None:
                        jump_piece = board.get_piece(new_col, new_row - 1)

                        if jump_piece is None:
                            valid_moves.append((new_col, new_row))                                              #first move 2 steps

                    if col_move == 0 and row_move == 1 and target_piece is None:
                        valid_moves.append((new_col, new_row))                                                  #basic move

                    if abs(col_move) == 1 and row_move == 1 and target_piece is not None and target_piece.color != self.color:
                        valid_moves.append((new_col, new_row))                                                  #capture

        return valid_moves

class King(Piece):
    def get_valid_moves(self, board: Board) -> ValidMoves:
        valid_moves = []
        movement = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        
        col, row = self.position
        for col_move, row_move in movement:
            new_col = col + col_move
            new_row = row + row_move

            if board.is_within_bounds(new_col, new_row):
                target_piece = board.get_piece(new_col, new_row)

                if target_piece is None:
                    valid_moves.append((new_col, new_row))                                                      #basic move

                else:
                    if target_piece.color != self.color:
                        valid_moves.append((new_col, new_row))                                                  #capture

        return valid_moves
    
