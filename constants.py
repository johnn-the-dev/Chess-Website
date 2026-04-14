from typing import List, Optional, Tuple
from enum import Enum

type Grid = List[List[Optional["Piece"]]]
type ValidMoves = List[Tuple[int, int]]
type Position = Tuple[int, int]

class Color(Enum):
    WHITE = "white"
    BLACK = "black"