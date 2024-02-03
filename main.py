from flask import Flask, render_template, request
import os
import math

import analysis


full_path = os.path.realpath(__file__)
print(full_path + "\n")
app = Flask(__name__, template_folder='front_end', static_folder='static')

# Index page
@app.route('/', methods=["GET"])
def index():
	return render_template('index.html')

@app.route('/analyze', methods=["GET"])
def analyzer_page():
	return render_template('analyze')

@app.route('/', methods=["POST"])
def index_post():
	FEN = request.form['FEN']
	turn = request.form['turn']

	eval = analysis.conversion(FEN)
	legalMoves = analysis.findLegal(turn)

	return render_template('analyzer_page.html', fen=FEN, turn=turn, evaluation=analysis.evaluate(), legalMoves=legalMoves)

if __name__ == '__main__':
		# Run the Flask app
		app.run(host='0.0.0.0', debug=True, port=int(os.environ['PORT']))