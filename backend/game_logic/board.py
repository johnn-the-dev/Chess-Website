from typing import TYPE_CHECKING, List, Optional
from backend.game_logic.constants import ValidMoves, Position, Color, Grid
from backend.game_logic.pieces import Piece, Color, Pawn, King, Queen, Bishop, Knight, Rook

class Board:
    def __init__(self) -> None:
        self.grid: Grid = [[None for _ in range(8)] for _ in range(8)]
        self.move_history: List[dict] = []
        self.setup_board()

    def setup_board(self) -> None:
        for col in range(8):
            self.grid[col][1] = Pawn(Color.BLACK, (col, 1)) #Black
            self.grid[col][6] = Pawn(Color.WHITE, (col, 6)) #White

        other_pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for col, piece_class in enumerate(other_pieces):
            self.grid[col][0] = piece_class(Color.BLACK, (col, 0)) #Black
            self.grid[col][7] = piece_class(Color.WHITE, (col, 7)) #White

    def get_fen(self) -> str:
        piece_to_char = {King: 'k', Queen: 'q', Rook: 'r', Bishop: 'b', Knight: 'n', Pawn: 'p'}
        result = ""

        for row in range(8):
            empty_spot = 0

            for col in range(8):
                piece = self.grid[col][row]

                if piece is None:
                    empty_spot += 1

                else:
                    if empty_spot > 0:
                        result += str(empty_spot)
                        empty_spot = 0

                    char = piece_to_char[type(piece)]

                    if piece.color == Color.WHITE:
                        char = char.upper()

                    result += f"{char}"
            
            if empty_spot > 0:
                result += str(empty_spot)

            if row < 7:
                result += "/"

        return result

    def is_within_bounds(self, col: int, row: int) -> bool:
        return 0 <= col < 8 and 0 <= row < 8
    
    def get_piece(self, col: int, row: int) -> Optional[Piece]:
        if self.is_within_bounds(col, row):
            return self.grid[col][row]
        
        return None

    def find_king(self, color: Color) -> Optional[Position]:
        for col in range(8):
            for row in range(8):
                piece: Optional[Piece] = self.get_piece(col, row)

                if piece:
                    if isinstance(piece, King) and piece.color == color:
                        return piece.position

        return None
    
    def is_square_attacked(self, target_pos: Position, enemy_color: Color) -> bool:
        for col in range(8):
            for row in range(8):
                piece: Optional[Piece] = self.get_piece(col, row)

                if piece and piece.color == enemy_color:
                    valid_moves = piece.get_valid_moves(self)

                    if target_pos in valid_moves:
                        return True

        return False
    
    def is_move_legal(self, start_pos: Position, end_pos: Position, piece_color: Color) -> bool:
        is_in_check = False
        start_col, start_row = start_pos
        end_col, end_row = end_pos
        moving_piece: Optional[Piece] = self.get_piece(start_col, start_row)
        static_piece: Optional[Piece] = self.get_piece(end_col, end_row)

        if not moving_piece:
            return False
        
        self.grid[end_col][end_row] = moving_piece
        self.grid[start_col][start_row] = None
        moving_piece.position = (end_col, end_row)

        king_position = self.find_king(piece_color)
        enemy_color = Color.BLACK if moving_piece.color == Color.WHITE else Color.WHITE
        
        if king_position:
            is_in_check = self.is_square_attacked(king_position, enemy_color)

        self.grid[end_col][end_row] = static_piece
        self.grid[start_col][start_row] = moving_piece
        moving_piece.position = (start_col, start_row)

        if is_in_check:
            return False

        return True
    
    def get_legal_moves(self, piece: Piece) -> ValidMoves:
        possible_moves = piece.get_valid_moves(self)
        legal_moves = []
        
        start_pos = piece.position
        
        for end_pos in possible_moves:
            if self.is_move_legal(start_pos, end_pos, piece.color):
                legal_moves.append(end_pos)
                
        return legal_moves
    
    def execute_move(self, start_pos: Position, end_pos: Position) -> None:
        start_col, start_row = start_pos
        end_col, end_row = end_pos
        moving_piece: Optional[Piece] = self.get_piece(start_col, start_row)
        captured_piece: Optional[Piece] = self.get_piece(end_col, end_row)

        self.grid[end_col][end_row] = moving_piece
        self.grid[start_col][start_row] = None
        moving_piece.position = (end_col, end_row)

        if isinstance(moving_piece, Pawn) and start_col != end_col and captured_piece is None:
            captured_piece = self.get_piece(end_col, start_row)
            self.grid[end_col][start_row] = None
        
        self.move_history.append({
        "piece": moving_piece,
        "start": start_pos,
        "end": end_pos,
        "captured": captured_piece
        })
