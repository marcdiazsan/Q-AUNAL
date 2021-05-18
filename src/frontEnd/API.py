from flask import Flask, jsonify, request, render_template
import json
import time
from datetime import datetime
import os


app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return render_template('preguntar.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=False, host='0.0.0.0', port=port)
