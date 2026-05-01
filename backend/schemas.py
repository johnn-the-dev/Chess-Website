from pydantic import BaseModel

class GameStateResponse(BaseModel):
    fen: str

class AnalyseRequest(BaseModel):
    fen: str

class AnalyseResponse(BaseModel):
    best_move: str | None
    score: float | str

class MoveRequest(BaseModel):
    fen: str
    move: str