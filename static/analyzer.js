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
squares[numbers[1] - 1].style.backgroundColor = 'red';


const canvas = document.createElement('canvas');
canvas.width = 300; // Set the canvas width
canvas.height = 100; // Set the canvas height
canvas.style.position = 'absolute'; // Position the canvas absolutely
canvas.style.top = '0'; // Adjust the top position as needed
canvas.style.left = '0'; // Adjust the left position as needed
document.body.appendChild(canvas); // Append the canvas to the DOM

const ctx = canvas.getContext('2d');
ctx.strokeStyle = 'red'; // Arrow color
ctx.lineWidth = 2; // Arrow line width

// Define the starting and ending coordinates for the arrow
const startX = squares[numbers[0] - 1].offsetLeft + squares[numbers[0] - 1].offsetWidth / 2;
const startY = squares[numbers[0] - 1].offsetTop + squares[numbers[0] - 1].offsetHeight / 2;
const endX = squares[numbers[1] - 1].offsetLeft + squares[numbers[1] - 1].offsetWidth / 2;
const endY = squares[numbers[1] - 1].offsetTop + squares[numbers[1] - 1].offsetHeight / 2;

// Draw the arrow line
ctx.beginPath();
ctx.moveTo(startX, startY);
ctx.lineTo(endX, endY);
ctx.stroke();

// Draw the arrowhead (you can customize the arrowhead shape)
const arrowSize = 10; // Adjust the arrowhead size
const angle = Math.atan2(endY - startY, endX - startX);
ctx.beginPath();
ctx.moveTo(endX, endY);
ctx.lineTo(endX - arrowSize * Math.cos(angle - Math.PI / 6), endY - arrowSize * Math.sin(angle - Math.PI / 6));
ctx.lineTo(endX - arrowSize * Math.cos(angle + Math.PI / 6), endY - arrowSize * Math.sin(angle + Math.PI / 6));
ctx.closePath();
ctx.fill();

// Ensure the canvas is positioned above other elements
canvas.style.zIndex = '9999'; // Set a high z-index value

if(parseInt(eval.textContent) > 0) {
	eval.textContent = `White is winning by ${eval.textContent} points.`;
} else if(parseInt(eval.textContent) < 0) {
		eval.textContent = `Black is winning by ${Math.abs(parseInt(eval.textContent))} points.`;
} else {
		eval.textContent = 'Both white and black are equal.';
}