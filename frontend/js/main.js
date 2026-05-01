const currentTheme = 'classic';

const chessAssets = {
    classic: {
        //white
        'K': '../assets/wK.svg', 
        'Q': '../assets/wQ.svg', 
        'R': '../assets/wR.svg', 
        'B': '../assets/wB.svg', 
        'N': '../assets/wN.svg', 
        'P': '../assets/wP.svg',

        //black
        'k': '../assets/bK.svg', 
        'q': '../assets/bQ.svg', 
        'r': '../assets/bR.svg', 
        'b': '../assets/bB.svg', 
        'n': '../assets/bN.svg', 
        'p': '../assets/bP.svg',
    }
};

let startMove = null;

const boardElement = document.getElementById("board");

for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 8; col++) {
        let square = document.createElement("div");
        square.addEventListener("click", handleSquareClick);
        square.id = `square-${col}-${row}`;

        if ((row + col) % 2 === 0) {
            square.classList.add("white");
        } else {
            square.classList.add("black");
        }
        
        boardElement.appendChild(square);
    }
};

function handleSquareClick(event) {
    const idParts = event.currentTarget.id.split("-");
    let col = parseInt(idParts[1]);
    let row = parseInt(idParts[2]);

    const files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
    const position = files[col] + (8 - row);

    if (startMove === null) {
        startMove = position;
        event.currentTarget.style.backgroundColor = "rgba(255, 255, 0, 0.5)";
        console.log("Selected:", startMove);
        
    } else {
        const endMove = position;
        const uciMove = startMove + endMove;

        console.log("Player made move:", uciMove);
        //sendMoveToBackend(uciMove);
        startMove = null;
    };
};

function loadFEN(fenString) {
    document.querySelectorAll('.piece').forEach(piece => piece.remove());
    let col = 0;
    let row = 0;

    for (let char of fenString) {
        if (char === "/") {

            row += 1;
            col = 0;
            continue;

        } else if (!isNaN(parseInt(char))) {

            col += parseInt(char);

        } else {
                let square = document.getElementById(`square-${col}-${row}`);
                let img = document.createElement('img');
                img.src = chessAssets[currentTheme][char];
                img.classList.add('piece');
                square.appendChild(img);
                col += 1;
        };
 
    };

};

async function fetchBoardState() {
    try {
        const response = await fetch("http://127.0.0.1:8000/test");
        
        if (!response.ok) {
            throw new Error(`HTTP ERROR! Status: ${response.status}`);
        };

        const data = await response.json();

        loadFEN(data.fen);

    } catch (error) {
        console.error("Could not load the game state:", error);
    };
};
