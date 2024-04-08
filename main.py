from flask import Flask, render_template, request
import os
import re
import math

import analysis


full_path = os.path.realpath(__file__)
app = Flask(__name__, template_folder='front_end', static_folder='static')

# THE FOLLOWING JUST ROUTE DIFFERENT TYPES OF REQUESTS TO THE RESPECTIVE PAGES
@app.route('/', methods=["GET"])
def index():
	return render_template('index.html')

@app.route('/analyze', methods=["GET"])
def analyzer_page():
	return render_template('analyze')

@app.route('/', methods=["POST"])
def index_post():
  #initialize the variables for analysis
  
  FEN = request.form['FEN']
  FEN_new = re.sub(r'\s.*', '', FEN)
  turn = FEN[len(FEN_new)+1:]
  turn = re.sub(r'\s.*', '', turn)
  firstlayereval = []
  best_move = analysis.LAGnormal(analysis.bestmovenobrain(FEN_new, turn), FEN_new, turn)
  position = analysis.returnconvert(FEN_new)
  eval = analysis.evaluate(FEN_new)
  modified_string = ''.join([char for char in FEN])
  #export the variables to the html page
  return render_template('analyzer.html', fen=FEN_new, evaluation=eval, pos=position, 
												 best=best_move)
#run the app on the port
if __name__ == '__main__':
	# Run the Flask app
	app.run(host='0.0.0.0', debug=True, port=int(os.environ['PORT']))