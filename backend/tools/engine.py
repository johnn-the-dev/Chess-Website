import os
import chess
import chess.engine
from dotenv import load_dotenv


load_dotenv()
ENGINE = os.getenv("ENGINE_PATH")

assert isinstance(ENGINE, str)

def analyse_board(fen: str) -> dict:
    engine = chess.engine.SimpleEngine.popen_uci(ENGINE)
    board = chess.Board(fen)

    try:
        limit = chess.engine.Limit(depth=15)
        info = engine.analyse(board, limit)
        best_move = str(info["pv"][0]) if "pv" in info and info["pv"] else None
        score = info["score"].white().score(mate_score=10000) / 100.0 if info["score"].white().score() is not None else "Mate"

        return {
            "best_move": best_move,
            "score": score
        }
    
    except Exception as e:
        return{"error": str(e)}

    finally:
        engine.quit()
