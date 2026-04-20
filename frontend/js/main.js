const currentTheme = 'classic';

const chessAssets = {
    classic: {
        //white
        'K': '../assets/wK.png', 
        'Q': '../assets/wQ.png', 
        'R': '../assets/wR.png', 
        'B': '../assets/wB.png', 
        'N': '../assets/wN.png', 
        'P': '../assets/wP.png',

        //black
        'k': '../assets/bK.png', 
        'q': '../assets/bQ.png', 
        'r': '../assets/bR.png', 
        'b': '../assets/bB.png', 
        'n': '../assets/bN.png', 
        'p': '../assets/bP.png',
    }
};

// SQUARES
// ../assets/sDG.png
// ../assets/sLG.png
// ../assets/sDB.png
// ../assets/sLB.png

const boardElement = document.getElementById("board");

for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 8; col++) {
        let square = document.createElement("div");

        square.id = `square-${col}-${row}`; 

        if ((row + col) % 2 === 0) {
            square.classList.add("white");
        } else {
            square.classList.add("black");
        }
        
        boardElement.appendChild(square);
    }
};
