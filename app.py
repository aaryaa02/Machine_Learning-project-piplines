##from crypt import methods
from flask import Flask


app = Flask(__name__)


@app.route('/',methods= ["Get","Post"])

def index():
	return 'First machine learning project.'


if __name__ == '__main__':

	
	app.run(debug=True)
