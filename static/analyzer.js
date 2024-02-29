let center = document.createElement('center');

let num = 1;

// Create a table element 
let ChessTable = document.createElement('table'); 
for (let i = 0; i < 8; i++) { 

		// Create a row 
		let board = document.createElement('tr'); 
		for (let j = 0; j < 8; j++) { 

				// Create a cell 
				let square = document.createElement('td'); 

				// If the sum of cell coordinates is even 
				// then color the cell white 
				if ((i + j) % 2 == 0) { 
					square.setAttribute('class', 'cell whitecell');
					square.setAttribute('id', num);

					board.appendChild(square);
				} 
				else { 
					// Create a class attribute for all black cells 
					square.setAttribute('class', 'cell blackcell'); 
					square.setAttribute('id', num);

					board.appendChild(square); 
				} 
		} 

		// Append the row 
		ChessTable.appendChild(board); 
} 
center.appendChild(ChessTable);

// Modifying table attribute properties 
ChessTable.setAttribute('cellspacing', '0'); 
ChessTable.setAttribute('width', '675px'); 
document.body.appendChild(center);

const squares = document.querySelectorAll('td');

function addPiece(color, piece, square) {
	const chessmen = document.createElement('img');
	chessmen.setAttribute('src', `/static/images/${color}/${piece}.png`);
	chessmen.style.height = '100%';
	chessmen.style.width = '100%';
	chessmen.style = 'cursor: pointer;';
	squares[square].appendChild(chessmen);
}

function initialize() {
	for(let i = 8; i < 16; i++) {
		const pawn = document.createElement('img');
		pawn.setAttribute('src', '/static/images/black/pawn.png');
		pawn.style.height = '100%';
		pawn.style.width = '100%';
		pawn.style = 'cursor: pointer;';
		squares[i].appendChild(pawn);
	}
	for(let i = 48; i < 56; i++) {
		const pawn = document.createElement('img');
		pawn.setAttribute('src', '/static/images/white/pawn.png');
		pawn.style.height = '100%';
		pawn.style.width = '100%';
		pawn.style = 'cursor: pointer;';
		squares[i].appendChild(pawn);
	}

	//append the black pieces
	addPiece('black', 'rook', 0);
	addPiece('black', 'knight', 1);
	addPiece('black', 'knight', 6);
	addPiece('black', 'bishop', 2);
	addPiece('black', 'bishop', 5);
	addPiece('black', 'king', 4);
	addPiece('black', 'queen', 3);
	addPiece('black', 'rook', 7);


	//append the white pieces
	addPiece('white', 'rook', 56);
	addPiece('white', 'knight', 57);
	addPiece('white', 'knight', 62);
	addPiece('white', 'bishop', 58);
	addPiece('white', 'bishop', 61);
	addPiece('white', 'king', 60);
	addPiece('white', 'queen', 59);
	addPiece('white', 'rook', 63);
}

initialize();