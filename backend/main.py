import os
import chess
import chess.engine

from dotenv import load_dotenv

from pydantic import BaseModel

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from tools.engine import analyse_board, make_move
from contextlib import asynccontextmanager

from schemas import GameStateResponse, AnalyseRequest, AnalyseResponse, MoveRequest

load_dotenv()
ENGINE = os.getenv("ENGINE_PATH")

ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = chess.engine.SimpleEngine.popen_uci(ENGINE)
    ml_models["stockfish"] = engine
    
    yield

    engine = ml_models["stockfish"]
    engine.quit()

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/start", response_model=GameStateResponse)
async def start() -> GameStateResponse:
    return GameStateResponse(fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

@app.post("/api/analyse")
async def analyse(request: AnalyseRequest) -> dict:
    try:
        return analyse_board(fen=request.fen, engine=ml_models["stockfish"])
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/api/move", response_model=GameStateResponse)
async def move(request: MoveRequest) -> GameStateResponse:
    try:
        fen = request.fen
        move = request.move
        new_fen = make_move(fen, move)

        return GameStateResponse(fen=new_fen)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))