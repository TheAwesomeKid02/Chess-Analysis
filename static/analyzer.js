let center = document.createElement('center');
let fen = document.getElementById('fen');

let num = 1;

// Create a table element 
let ChessTable = document.createElement('table'); 
for (let i = 0; i < 8; i++) { 
		// Create a row 
		let board = document.createElement('tr'); 
		for (let j = 0; j < 8; j++) { 
				//create the cell
				let square = document.createElement('td'); 
				//logic for square color
				if ((i + j) % 2 == 0) { 
					square.setAttribute('class', 'cell whitecell');
					square.setAttribute('id', num);
					board.appendChild(square);
				} 
				else { 
					//create black cells
					square.setAttribute('class', 'cell blackcell'); 
					square.setAttribute('id', num);
					board.appendChild(square); 
				} 
		} 
		ChessTable.appendChild(board); 
} 
center.appendChild(ChessTable);

// Modifying table attribute properties 
ChessTable.setAttribute('cellspacing', '0'); 
ChessTable.setAttribute('width', '675px'); 
document.body.appendChild(center);

const squares = document.querySelectorAll('td');

//the square is a number from 1 to 64
function addPiece(color, piece, square) {
	const chessmen = document.createElement('img');
	chessmen.setAttribute('src', `/static/images/${color}/${piece}.png`);
	chessmen.style.height = '100%';
	chessmen.style.width = '100%';
	chessmen.style = 'cursor: pointer;';
	squares[square].appendChild(chessmen);
}

/**
 * A positive number indicates white and a negative number indicates black
 * 1 is a pawn
 * 3 is a knight
 * 4 is a bishop
 * 5 is a rook
 * 9 is a queen
 * 10 is a king
*/
function initialize() {
	const position = document.getElementById('position');
	let pos_string;
	//remove the spaces and brackets
	pos_string = position.textContent.replace(/\s/g, '').replace('[', '').replace(']', '');
	console.log(pos_string);
	//remove all the commas and make the elements of the list numbers (integers)
	let pos_array = pos_string.split(',').map(Number);
	console.log(pos_array);
	
	for(let i = 0; i < pos_array.length; i++) {
		if(pos_array[i] != 0) { //if the element is not 0, add a piece
			if (Math.abs(pos_array[i]) == 9) {
				if(pos_array[i] < 0) {
					addPiece('black', 'queen', i);
				} else {
					addPiece('white', 'queen', i)
				}
			} else if (Math.abs(pos_array[i]) == 10) {
					if(pos_array[i] < 0) {
						addPiece('black', 'king', i);
					} else {
						addPiece('white', 'king', i)
					}
			} else if (Math.abs(pos_array[i]) == 3) {
					if(pos_array[i] < 0) {
						addPiece('black', 'knight', i);
					} else {
						addPiece('white', 'knight', i)
					}
			} else if (Math.abs(pos_array[i]) == 4) {
					if(pos_array[i] < 0) {
						addPiece('black', 'bishop', i);
					} else {
						addPiece('white', 'bishop', i)
					}
			} else if (Math.abs(pos_array[i]) == 1) {
					if(pos_array[i] < 0) {
						addPiece('black', 'pawn', i);
					} else {
						addPiece('white', 'pawn', i)
					}
			} else if (Math.abs(pos_array[i]) == 5) {
					if(pos_array[i] < 0) {
						addPiece('black', 'rook', i);
					} else {
						addPiece('white', 'rook', i)
					}
			}
		}
	}
}

//call the function
initialize();