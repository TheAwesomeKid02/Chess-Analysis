from flask import Flask, render_template, request
import os


full_path = os.path.realpath(__file__)
print(full_path + "\n")


app = Flask(
	__name__ ,
	template_folder='front_end',
	static_folder='static'
)

# Index page
@app.route('/', methods=["GET"])
def index():
	return render_template('index.html')

if __name__ == '__main__':
	# Run the Flask app
	app.run(
		host='0.0.0.0',
		debug=True,
		port=8080
	)