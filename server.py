import os
from flask import Flask, request, json, render_template, Response
from flask_cors import CORS
from chunker import Chunker

ch = Chunker()

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/chunk', methods = ['POST'])
def chunk():
	data_all = request.get_json()

	kalimat = data_all['kalimat']
	return str(ch.tree_to_str(ch.chunk_me2(kalimat)))

	# _ists = iSTSEngine()
	# return _ists.singleTest()

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000)
