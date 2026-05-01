# Chess Analysis API & LLM Assistant

A lightweight web application for deep chess position analysis. This project combines a traditional chess engine (Stockfish) with a Large Language Model (LLM) and Retrieval-Augmented Generation (RAG) to provide both raw engine evaluations and human-readable strategic insights, especially for endgame theory.

## 🚀 Features (WIP)
* **Interactive Chessboard:** Custom Vanilla JS frontend for rendering pieces and handling user moves.
* **FEN String Integration:** Seamless state management using FEN formatting.
* **Stockfish Analysis:** Deep calculation of positions returning best moves and evaluations (mate scores / centipawns).
* **LLM & RAG Integration (Upcoming):** Natural language explanation of positions and automatic retrieval of endgame theory files.

## 🛠 Tech Stack
* **Backend:** Python, FastAPI, `python-chess`
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **AI/Engine:** Stockfish, LLM (via LangChain/LangGraph - planned)

## ⚙️ Quick Start
1. Ensure Stockfish is installed and its path is set in `.env` as `ENGINE_PATH`.
2. Install Python requirements: `pip install fastapi uvicorn python-chess python-dotenv pydantic`
3. Run the backend: `uvicorn main:app --reload`
4. Open `index.html` in your browser.