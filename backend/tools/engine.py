import chess
import chess.engine

def analyse_board(fen: str, engine) -> dict:
    
    board = chess.Board(fen)
    limit = chess.engine.Limit(depth=15)
    info = engine.analyse(board, limit)
    best_move = str(info["pv"][0]) if "pv" in info and info["pv"] else None
    score = info["score"].white().score(mate_score=10000) / 100.0 if info["score"].white().score() is not None else "Mate"

    return {
        "best_move": best_move,
        "score": score
    }

def make_move(fen: str, uci_move: str) -> str:
    board = chess.Board(fen)
    move = chess.Move.from_uci(uci_move)

    if move in board.legal_moves:
        board.push(move)
        return board.fen()
    else:
        raise ValueError(f"Illegal move: {uci_move}")