let center = document.createElement('center');
let fen = document.getElementById('fen');
let eval = document.getElementById('eval');
let best_move = document.getElementById('best_move');

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

function addPiece(color, piece, square) {
	const chessmen = document.createElement('img');
	chessmen.setAttribute('src', `/static/images/${color}/${piece}.png`);
	chessmen.style.height = '100%';
	chessmen.style.width = '100%';
	chessmen.style.cursor = 'pointer';
	chessmen.style.zIndex = '5';
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
function initialize(position) {
	let pos_string;
	pos_string = position.textContent.replace(/\s/g, '').replace('[', '').replace(']', '');
	console.log(pos_string);
	let pos_array = pos_string.split(',').map(Number);
	console.log(pos_array);
	
	for(let i = 0; i < pos_array.length; i++) {
		if(pos_array[i] != 0) {
			if (Math.abs(pos_array[i]) == 9) {
				if(pos_array[i] < 0) {
					addPiece('black', 'queen', i);
				} else {
					addPiece('white', 'queen', i);
				}
			} else if (Math.abs(pos_array[i]) == 10) {
					if(pos_array[i] < 0) {
						addPiece('black', 'king', i);
					} else {
						addPiece('white', 'king', i);
					}
			} else if (Math.abs(pos_array[i]) == 3) {
					if(pos_array[i] < 0) {
						addPiece('black', 'knight', i);
					} else {
						addPiece('white', 'knight', i);
					}
			} else if (Math.abs(pos_array[i]) == 4) {
					if(pos_array[i] < 0) {
						addPiece('black', 'bishop', i);
					} else {
						addPiece('white', 'bishop', i);
					}
			} else if (Math.abs(pos_array[i]) == 1) {
					if(pos_array[i] < 0) {
						addPiece('black', 'pawn', i);
					} else {
						addPiece('white', 'pawn', i);
					}
			} else if (Math.abs(pos_array[i]) == 5) {
					if(pos_array[i] < 0) {
						addPiece('black', 'rook', i);
					} else {
						addPiece('white', 'rook', i);
					}
			}
		}
	}
}


initialize(document.getElementById('position'));


let numbers1 = best_move.textContent.match(/\d+/g);
numbers1.map(Number);

squares[numbers1[0]-1].style = 'background-color: red;';
squares[numbers1[1]-1].style = 'background-color: red;';

let numbers = best_move.textContent.match(/\d+/g);
numbers.map(Number);

// Highlight the best move squares in red
squares[numbers[0] - 1].style.backgroundColor = 'red';
squares[numbers[1] - 1].style.backgroundColor = 'blue';

let x0 = squares[numbers[0]-1].offsetLeft;
let x1 = squares[numbers[1]-1].offsetLeft;


let arrow = document.createElement('div');
let angle = Math.atan((((numbers[0]-1) % 8)+1)/(((numbers[1]-1) % 8)+1));

if(x0 < x1) {
	angle += Math.PI/2;
} else if(x0 > x1) {
	angle -= Math.PI/2;
}

arrow.style.width = '0';
arrow.style.height = '0';
arrow.style.borderLeft = '10px solid transparent';
arrow.style.borderRight = '10px solid transparent';
arrow.style.borderBottom = '40px solid rgba(0, 123, 255, 0.7)';
arrow.style.position = 'absolute';
arrow.style.left = '50%';
arrow.style.bottom = '25%';
arrow.style.transform = `translateX(-50%) rotate(${angle}rad)`;
arrow.style.zIndex = '999';

console.log(angle)

squares[numbers[0]-1].appendChild(arrow);