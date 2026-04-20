from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.game_logic.board import Board


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
async def test():
    game = Board()
    print("Start:", game.get_fen())
    
    game.execute_move((4, 6), (4, 4))
    
    return ("Po e4:", game.get_fen())