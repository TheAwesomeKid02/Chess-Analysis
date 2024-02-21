let center = document.createElement('center');

let num = 1;

let a1 = document.getElementById('1');
let a2 = document.getElementById('2');
let a3 = document.getElementById('3');
let a4 = document.getElementById('4');
let a5 = document.getElementById('5');
let a6 = document.getElementById('6');
let a7 = document.getElementById('7');
let a8 = document.getElementById('8');
let b1 = document.getElementById('9');
let b2 = document.getElementById('10');
let b3 = document.getElementById('11');
let b4 = document.getElementById('12');
let b5 = document.getElementById('13');
let b6 = document.getElementById('14');
let b7 = document.getElementById('15');
let b8 = document.getElementById('16');
let c1 = document.getElementById('17');
let c2 = document.getElementById('18');
let c3 = document.getElementById('19');
let c4 = document.getElementById('20');
let c5 = document.getElementById('21');
let c6 = document.getElementById('22');
let c7 = document.getElementById('23');
let c8 = document.getElementById('24');
let d1 = document.getElementById('25');
let d2 = document.getElementById('26');
let d3 = document.getElementById('27');
let d4 = document.getElementById('28');
let d5 = document.getElementById('29');
let d6 = document.getElementById('30');
let d7 = document.getElementById('31');
let d8 = document.getElementById('32');
let e1 = document.getElementById('33');
let e2 = document.getElementById('34');
let e3 = document.getElementById('35');
let e4 = document.getElementById('36');
let e5 = document.getElementById('37');
let e6 = document.getElementById('38');
let e7 = document.getElementById('39');
let e8 = document.getElementById('40');
let f1 = document.getElementById('41');
let f2 = document.getElementById('42');
let f3 = document.getElementById('43');
let f4 = document.getElementById('44');
let f5 = document.getElementById('45');
let f6 = document.getElementById('46');
let f7 = document.getElementById('47');
let f8 = document.getElementById('48');
let g1 = document.getElementById('49');
let g2 = document.getElementById('50');
let g3 = document.getElementById('51');
let g4 = document.getElementById('52');
let g5 = document.getElementById('53');
let g6 = document.getElementById('54');
let g7 = document.getElementById('55');
let g8 = document.getElementById('56');
let h1 = document.getElementById('57');
let h2 = document.getElementById('58');
let h3 = document.getElementById('59');
let h4 = document.getElementById('60');
let h5 = document.getElementById('61');
let h6 = document.getElementById('62');
let h7 = document.getElementById('63');
let h8 = document.getElementById('64');

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
					square.style.position = 'relative';

					board.appendChild(square);
				} 
				else { 
					// Create a class attribute for all black cells 
					square.setAttribute('class', 'cell blackcell'); 
					square.setAttribute('id', num);
					square.style.position = 'relative';

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

function putPiece(color, piece, square) {
	let chessmen = document.createElement('img');
	chessmen.setAttribute('src', `front_end/images/${color}/${piece}/.png`);
		
}

function initialize() {
	for(let i = 0; i < 8; i++) {
		let chessmen = document.creatElement('img');
		chessmen.setAttribute('src', `front_end/images/white/pawn/.png`);

		let top = 0.5 * (b2.height - chessmen.height);
		let left = 0.5 * (b2.width - chessmen.width);

		chessmen.style = 'top: top; left: left;';
	}	
}

//intialize();